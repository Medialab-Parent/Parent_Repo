from flask import Flask, request, jsonify, json
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def hello():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Flask Buttons</title>
        <script>
            function fetchData(endpoint) {
                fetch(endpoint)
                    .then(response => response.json())
                    .then(data => {
                        const dataParsed = JSON.parse(data);
                        console.log(dataParsed);
                        console.log(dataParsed.response);
                        document.getElementById('data').innerText = `Message from backend: ${dataParsed.pull_response}. Ollama message: ${dataParsed.response}`;
                    })
                    .catch(error => console.error('Error:', error));
            }
        </script>
    </head>
    <body>
        <h4>Pulling Ollama Locally: MUST always when wanting to use Local Ollama</h4>
        <button onclick="fetchData('/api/pullOllama')">Fetch pullOllama</button>
        <h4>Ollama Generate: Only for testing, debugging purposes</h4>
        <button onclick="fetchData('/api/genOllama')">Fetch DataGen (only for testing, debugging purposes)</button>
        <div id="data"></div>
    </body>
    </html>
    '''
    return html_content


@app.route('/api/pullOllama', methods=['GET', 'POST'])
def get_ollama():

    # Define the API endpoint and the payload
    url = "http://ollama:11434/api/pull"
    payload = {"name": "mistral"}

    # Send a POST request to the API
    response = requests.post(url, json=payload)
    print(response.text)

    ollama_response = response.text
    return jsonify(ollama_response)


@app.route('/api/genOllama', methods=['GET', 'POST'])
def genOllama():

    print("Gen Ollama called at least!")
    # Extract message and cs_type from the request JSON
    data = request.json
    message = data.get('message')
    cs_type = data.get('cs_type')

    # Define the API endpoint and the payload
    url2 = "http://ollama:11434/api/generate"
    prompt = f"This is a hateful comment: '{message}'. Please generate a counter speech max 5 tokens, very short, response of type {cs_type}. Format the response in the following JSON-Format: {{\"Answer\": \"\"}}"
    payload2 = {
        "model": "mistral",
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
    app.run(host='0.0.0.0', port=6002)