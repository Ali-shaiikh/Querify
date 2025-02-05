Querify: SQL Query Generator for CSV Data 📊💻
Project Overview 🌟
Querify is a web application designed to generate SQL queries based on user-provided CSV data using a local language model (LLM). The application utilizes Streamlit for the user interface, allowing users to upload CSV files and input specific questions to generate SQL queries.

Features ✨
CSV Upload: Users can upload CSV files for processing. 📤
SQL Query Generation: Based on user input, the app generates SQL queries using the local LLM. 📝
Query Explanation: Users can request explanations for the generated SQL queries. ❓
Files 📂
app.py
The main application script that leverages Streamlit to create a user interface. It allows users to:

Upload CSV files. 📁
Input questions to generate SQL queries based on the data. 🗨️
View the generated SQL queries. 🔍
Get explanations for the queries. 📜
main.py
This script interacts with the LLM via an API endpoint. It handles:

API Interaction: Sends requests to the URL where the LLM is running. 🌐
Prompt Handling: Constructs a prompt to query the benefits of AI models for data analysis and retrieves responses. 🤖
backend.ipynb
A Jupyter Notebook designed for testing and setting up LLM functionalities. It includes:

Installation instructions for necessary packages like ollama and streamlit. 📦
Code for initializing the LLM with the required parameters. ⚙️
Functions for reading CSV files, constructing SQL queries, and generating SQL commands like CREATE TABLE and INSERT INTO. 🛠️
model.py
Defines the model parameters and instructions for generating SQL queries. It includes:

Model Configuration: Specifies using the llama3 model with a temperature setting of 0 for deterministic outputs. 🌡️
System Instructions: Instructs the model to act as a "SQL query master" to generate SQL queries based on natural language questions about CSV data, along with brief explanations. 🎓
Libraries Used 📚
pandas: For data manipulation and processing, especially for reading and handling CSV files. 📊
streamlit: For building the web interface to upload CSV files and display SQL queries. 🌐
requests: To make HTTP requests to the LLM API, enabling interaction with the model. 🌍
subprocess: Allows spawning new processes to run the local LLM for SQL query generation. 🔄
sys: Provides system-specific parameters, like encoding and locale settings for proper data handling. ⚙️
locale: Configures locale for data formatting (dates, numbers, etc.). 🗓️
json: Used for handling JSON data when sending requests to the LLM API. 📄
langchain_ollama: For integrating with the Ollama model, which generates SQL queries based on user input. 🔗
Getting Started 🚀
Clone the repository:

bash
git clone <repository_url>
cd <repository_folder>
Create a virtual environment (venv):

bash
python -m venv venv
.\venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
Install required packages:

bash
pip install -r requirements.txt
Run the Streamlit application:

bash
streamlit run app.py
Contributing 🤝
Contributions are welcome! To contribute:

Fork the repository. 🍴
Create a new branch for your feature or fix. 🌱
Submit a pull request with your changes. 🔀
