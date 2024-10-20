from flask_restful import Resource
import joblib

class StatusController(Resource):
    def get(self):
        # Load the trained model
        try:
            model = joblib.load('./public/best_model.pkl')
        
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
                "status": "Model is trained.",
                "model_type": model_type,
                "best_params": best_params,
                "num_classes": num_classes
            }, 200
    
        except FileNotFoundError:
            return {"error": "No trained model found. Please train a model first."}, 404
        
        except Exception as e:
            # Catch any other exception
            return {"error": f"An error occurred: {str(e)}"}, 500