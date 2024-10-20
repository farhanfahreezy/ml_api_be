from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

from src.middleware.jwt_auth import jwt_auth

class TrainController(Resource):
    @jwt_auth
    def post(self):
        try:
            # Get request body
            body = request.get_json()
            algorithm = body.get('algorithm')
            param_grid = body.get('param_grid')

            if not algorithm or not param_grid:
                return {"error": "Algorithm and parameter grid are required."}, 400

            # Initialize the model based on the requested algorithm
            if algorithm == 'decision_tree':
                model = DecisionTreeClassifier()
            elif algorithm == 'random_forest':
                model = RandomForestClassifier()
            else:
                return {"error": "Unsupported algorithm. Choose 'decision_tree' or 'random_forest'."}, 400

            # Load the iris dataset
            iris = load_iris()
            X = iris.data
            y = iris.target

            # Perform GridSearchCV for hyperparameter optimization
            grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
            grid_search.fit(X, y)

            # Get the best parameters, accuracy, and cross-validation results
            best_params = grid_search.best_params_
            best_model = grid_search.best_estimator_
            cv_results = grid_search.cv_results_

            # Extract mean test scores for each hyperparameter combination
            cv_summary = {
                'params': cv_results['params'],  # The hyperparameter combinations
                'mean_test_score': cv_results['mean_test_score'].tolist(),  # Mean accuracy across folds
                'std_test_score': cv_results['std_test_score'].tolist()  # Standard deviation of accuracy
            }

            identity = get_jwt_identity()
            user_id = identity['id']
            directory = f'./public/{user_id}'
            os.makedirs(directory, exist_ok=True)

            # Save the model
            joblib.dump(best_model, os.path.join(directory, 'best_model.pkl'))

            return jsonify({
                "best_params": best_params,
                "best_score": grid_search.best_score_,
                "cv_results": cv_summary
            })

        except ValueError as e:
            # Handle any ValueErrors (e.g., unknown parameters in param_grid)
            return {"error": f"ValueError: {str(e)}"}, 400

        except Exception as e:
            # Catch any other exception
            return {"error": f"An error occurred: {str(e)}"}, 500