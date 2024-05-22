from flask import Flask, request, render_template
from roberta import load_model, predict
import logging
import os
from datetime import datetime


app = Flask(__name__)

# Load the model and tokenizer once at startup
tokenizer, model = load_model()

# Get the directory of the current file
current_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the log file path
log_file_path = os.path.join(current_directory, 'FLASKUSER_LOG.log')

# Configure logging
logging.basicConfig(filename=log_file_path, level=logging.INFO, 
                    format='%(asctime)s / %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Suppress the default Flask logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form.get('text', None)
        
        if text is None:
            return render_template('index.html', error="No text provided")
        
        results = predict(tokenizer, model, text)
        
        # Format predictions for logging
        predictions_formatted = ', '.join([label for word, label in results])
        
        # Log the interaction in the desired format
        logging.info(f'Input: {text} / Predicted Label: {predictions_formatted}')
        
        return render_template('index.html', results=results)
    return render_template('index.html')

if __name__ == '__main__':
    print("Starting Flask server, navigate to http://127.0.0.1:5000/ to use the application.")
    app.run(debug=True)
