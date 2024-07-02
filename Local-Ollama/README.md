# How to run Local Ollama

Docker is used and through docker it takes approximately 2 min 15s to download Local Ollama, approximately 2 min to generate a first response and approximately 1min 30s to regenerate it. On different devices Local Ollama in Docker might run faster.

## How to setup and start using

1. Take from llm_backend.py line "GENERATING_CS_LLM": "localOllama" and paste it to config.json instead "GENERATING_CS_LLM": "openaiORgroq". This makes you use the local ollama instead of OpenAI or Groq for generating CS. (The choice between the last mentioned ones is in CSGeneration.py and can be set by switching llm_groq with llm_openai and opposite).
   
2. Download desktop Ollama (https://ollama.com/)
   
3. Run in CMD: ollama pull mistral
   
4. Run docker-compose up –build in the project
   
5. Go to http://localhost:6002/api/pullOllama/mistral in your Chrome Browser (works also on other browsers, but Chrome is our default choice). Now in the docker downloading a mistral model started. You can see “download” in docker under Ollama container or in VS Code terminal.
   
6. If you can see either in docker or in VS Code terminal after waiting for up to 5 min ollama “success” then the model was downloaded successfully to the docker

7. Start using the plug-in as normal (but expect long generating times). Note that generation uses always the latest model you locally downloaded, it is stored in a global variable in app.py inside LocalOllama folder/container.

## How to use Local Ollama with different Ollama models

Instead of http://localhost:6002/api/pullOllama/mistral you can write http://localhost:6002/api/pullOllama/llama3 or http://localhost:6002/api/pullOllama/llama2 or http://localhost:6002/api/pullOllama/{myDesiredModel}. It is important to check https://ollama.com/library for models and more information. It is also important to follow the previous steps including the CMD step. The Local Ollama was tested with mistral and llama3, and both work 16.06.2024 locally on developers machine.

## License
- This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
- For any questions or issues, please contact [cc211002@fhstp.ac.at].

