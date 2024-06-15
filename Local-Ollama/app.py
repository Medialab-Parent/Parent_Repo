from flask import Flask, request, jsonify, json
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize a global variable for the model
modelChosen = None

@app.route('/api/pullOllama/<model>', methods=['GET'])
def get_ollama(model):
    global modelChosen  # Declare the global variable
    # Define the API endpoint and the payload
    url = "http://ollama:11434/api/pull"
    payload = {"name":model}

    # Send a POST request to the API
    response = requests.post(url, json=payload)
    print(response.text)

    ollama_response = response.text
    modelChosen = model
    return jsonify(ollama_response)


@app.route('/api/genOllama', methods=['GET', 'POST'])
def genOllama():

    print("Gen Ollama called!")
    global modelChosen
    if modelChosen is None:
        return jsonify({"status": "error", "message": "No model chosen"}), 400
    
    model = modelChosen
    # Extract message and cs_type from the request JSON
    data = request.json
    message = data.get('message')
    cs_type = data.get('cs_type')
    
    # Define the API endpoint and the payload
    url2 = "http://ollama:11434/api/generate"
    prompt = f"This is a hateful comment: '{message}'. Please generate a counter speech max 5 tokens, very short, response of type {cs_type}. Format the response in the following JSON-Format: {{\"Answer\": \"\"}}"
    payload2 = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    # Send a POST request to the API
    response2 = requests.post(url2, json=payload2)
    print("response2", response2)    
    
    print(response2.text)
    
    

    if response2.status_code == 200:
        # Assuming the API returns a JSON object with the key 'Answer'
        ollama_response = response2.text
    else:
        ollama_response = f"Error: {response2.status_code}, {response2.text}"
        
    return jsonify(ollama_response)


if __name__ == '__main__':
    app.run(debug=True,use_reloader=True, host='0.0.0.0', port=6002)