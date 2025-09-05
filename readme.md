# Querify: SQL Query Generator for CSV Data

## Project Overview
Querify is a web application that generates SQL queries based on user-provided CSV data using a local language model (LLM). The application is built with **Streamlit** for the user interface, allowing users to upload CSV files and input natural language questions to generate SQL queries.

---

## Features
- **CSV Upload**: Upload CSV files for processing.
- **SQL Query Generation**: Generate SQL queries using a local LLM based on user input.
- **Query Explanation**: Get explanations for the generated SQL queries.

---

## Project Structure

### `app.py`
Main application script built with Streamlit.  
Functions:
- Upload CSV files.
- Input questions to generate SQL queries.
- Display generated queries and their explanations.

### `main.py`
Handles communication with the LLM via an API endpoint.  
Functions:
- Sends requests to the local LLM.
- Builds prompts for SQL query generation.

### `backend.ipynb`
Jupyter Notebook for testing and setup.  
Includes:
- Installation instructions for `ollama`, `streamlit`, and other dependencies.
- Code for initializing the LLM.
- Functions for reading CSV files and generating SQL commands (`CREATE TABLE`, `INSERT INTO`, etc.).

### `model.py`
Defines model parameters and system instructions.  
Includes:
- **Model Configuration**: Uses `llama3` with temperature `0` for deterministic outputs.
- **System Instructions**: Guides the model to act as a "SQL query master" for generating queries and explanations.

---

## Libraries Used
- **pandas**: Data manipulation and CSV handling.
- **streamlit**: Web interface.
- **requests**: API interaction with the LLM.
- **subprocess**: Running local LLM processes.
- **sys**: System-level configurations.
- **locale**: Locale-specific data formatting.
- **json**: JSON data handling.
- **langchain_ollama**: Integration with the Ollama model.

---

## Getting Started

### Clone the repository
```bash
git clone <repository_url>
cd <repository_folder>
```
```bash
python -m venv venv
.\venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux
```
```bash
pip install -r requirements.txt
```
```bash
streamlit run app.py
```

