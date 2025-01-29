Project Overview:
This project is designed to generate SQL queries based on user-provided CSV data using a local language model (LLM). The application utilizes Streamlit for the user interface, allowing users to upload CSV files and input specific questions to generate SQL queries.

File Summaries:
'app.py'
This file serves as the main application script, leveraging Streamlit to create a web interface. It allows users to upload a CSV file and input a question regarding SQL queries based on the data. Key functionalities include:
CSV Upload: Users can upload their CSV files for processing.
SQL Query Generation: Based on user input, the app generates SQL queries using the local LLM.
Query Explanation: Users can request explanations for the generated SQL queries.


'main.py'
This script focuses on querying the LLM via an API endpoint. It defines a function that sends prompts to the LLM and retrieves responses. The main features include:
API Interaction: It posts requests to a specified URL where the LLM is running.
Prompt Handling: It constructs a prompt about the benefits of AI models for data analysis and retrieves the response.


'backend.ipynb'
This Jupyter Notebook provides an interactive environment to set up and test functionalities related to the LLM. It includes:
Installation Commands: Instructions for installing necessary packages like ollama and streamlit.
Model Initialization: Code snippets to initialize the LLM with specified parameters.
Data Handling: Functions to read CSV files, construct SQL queries from data types, and generate SQL commands like CREATE TABLE and INSERT INTO.


'model.py'
This file defines parameters and instructions for the LLM to generate SQL queries. It includes:
Model Configuration: Specifies using the llama3 model with a temperature setting of 0 for deterministic outputs.
System Instructions: Directs the model to act as a "SQL query master," generating SQL queries based on natural language questions about CSV data, along with brief explanations of those queries.




*Getting Started*

1.Clone the repository.
*note: Creating a virtual environment (venv) is mandatory*
    
  python -m venv venv

  .\venv\Scripts\activate


2.Install required packages using pip:
  
  pip install -r requirements.txt
  
3.Run the Streamlit application:
  
  streamlit run app.py



Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.# Querify
