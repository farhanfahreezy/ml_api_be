from flask_restful import Resource
import joblib
from flask_jwt_extended import get_jwt_identity

from src.middleware.jwt_auth import jwt_auth

class StatusController(Resource):
    @jwt_auth
    def get(self):
        # Load the trained model
        try:
            identity = get_jwt_identity()
            user_id = identity['id']  
            model = joblib.load(f'./public/{user_id}/best_model.pkl')
        
            # Extract model details
            model_type = type(model).__name__
            if hasattr(model, 'get_params'):
                best_params = model.get_params()
            else:
                best_params = "No parameters available."

            if hasattr(model, 'n_classes_'):
                num_classes = model.n_classes_
            else:
                num_classes = "Not available."

            # Return model status
            return {
                "status": "Trained",
                "model_type": model_type,
                "best_params": best_params,
                "num_classes": int(num_classes)
            }, 200
    
        except FileNotFoundError:
            return {"status": "NotTrained"}, 202
        
        except Exception as e:
            # Catch any other exception
            return {"status": f"An error occurred: {str(e)}"}, 500