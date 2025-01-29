import requests
import json

# Define the API endpoint of your locally running Ollama model (or local interface)
url = 'http://localhost:5000/query'  # Replace with your model's actual URL

# Function to query the Ollama model
def query_ollama_model(prompt):
    payload = {'input': prompt}
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Adjust based on the model's response structure
    else:
        print(f"Error: {response.status_code}")
        return None

# Query the model with a prompt
prompt = "What are the benefits of using AI models for data analysis?"
response = query_ollama_model(prompt)

if response:
    print(response)
