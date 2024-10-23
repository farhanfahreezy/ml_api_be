from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity
import joblib
import numpy as np

from src.middleware.jwt_auth import jwt_auth

class PredictController(Resource):
    @jwt_auth
    def post(self):
        # Load the trained model
        try:
            identity = get_jwt_identity()
            user_id = identity['id']  
            model = joblib.load(f'./public/{user_id}/best_model.pkl')
       
            # Get request body
            body = request.get_json()
            if not body or 'input' not in body:
                return {"error": "Input data is required."}, 400
            

            input_data = body['input']

            # If input is a single list
            if isinstance(input_data[0], (int, float)):  # Check if first item is a number
                input_data = np.array(input_data).reshape(1, -1)  # Reshape for single sample
            # If input is a list of lists
            elif isinstance(input_data[0], list):
                input_data = np.array(input_data)  # Convert to numpy array directly
            else:
                return {"error": "Invalid input format."}, 400
            
            prediction = model.predict(input_data)

            # Return the prediction as JSON
            return jsonify({"prediction": prediction.tolist()})
    
        except FileNotFoundError:
            return {"error": "No trained model found. Please train a model first."}, 404
    
        except Exception as e:
            # Catch any other exception
            return {"error": f"An error occurred: {str(e)}"}, 500
