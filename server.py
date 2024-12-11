from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import logging

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Load pre-trained Transformer model for text classification
try:
    app.logger.info("Loading Transformer model...")
    classifier = pipeline("text-classification", model="distilbert-base-uncased")
    app.logger.info("Transformer model loaded successfully.")
except Exception as e:
    app.logger.error(f"Error loading Transformer model: {e}")
    raise

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Endpoint to analyze email content.
    """
    try:
        # Get email content from the POST request
        data = request.json.get('data', '')
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Optional: Truncate large input to prevent issues
        if len(data) > 512:
            app.logger.warning("Input truncated to 512 characters.")
            data = data[:512]

        # Perform classification using the Transformer model
        result = classifier(data)
        app.logger.info(f"Analysis result: {result}")

        # Return the classification result
        return jsonify({'label': result[0]['label'], 'score': result[0]['score']})
    except Exception as e:
        app.logger.error(f"Error during analysis: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the server on localhost and port 4000
    app.run(debug=True, port=4000)
