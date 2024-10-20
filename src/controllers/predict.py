from flask import request, jsonify
from flask_restful import Resource
import joblib
import numpy as np

class Predict(Resource):
    def post(self):
        # Load the trained model
        try:
            model = joblib.load('./public/best_model.pkl')
        except FileNotFoundError:
            return {"error": "No trained model found. Please train a model first."}, 400
        
        # Get request body
        body = request.get_json()
        if not body or 'input' not in body:
            return {"error": "Input data is required."}, 400
        

        input_data = body['input']

        # Handle both single and multiple input cases
        try:
            # If input is a single list
            if isinstance(input_data[0], (int, float)):  # Check if first item is a number
                input_data = np.array(input_data).reshape(1, -1)  # Reshape for single sample
            # If input is a list of lists
            elif isinstance(input_data[0], list):
                input_data = np.array(input_data)  # Convert to numpy array directly
            else:
                return {"error": "Invalid input format."}, 400
            
        except Exception as e:
            return {"error": str(e)}, 500

        # Make the prediction
        try:
            prediction = model.predict(input_data)
        except Exception as e:
            return {"error": str(e)}, 500

        # Return the prediction as JSON
        return jsonify({"prediction": prediction.tolist()})
