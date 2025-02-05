from langchain_ollama import OllamaLLM
import streamlit as st
import pandas as pd
import subprocess
import sys
import locale

# Set up the page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Querify", layout="centered")

# Add custom CSS for styling with updated background color and glowing text effects
st.markdown("""
    <style>
        .stApp {
            background-color: #ffe8d4;  /* Soft peach background */
            color: #0a0908;  /* Dark text for contrast */
            padding: 20px;
        }
        h1 {
            color: #49111c;  /* Glowing reddish color for the title */
            font-family: 'Arial', sans-serif;
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 40px;
            font-weight: 900;  /* Making the main heading bolder */
            text-shadow: 0 0 10px #49111c, 0 0 20px #49111c, 0 0 30px #49111c;  /* Glowing effect */
        }
        .stButton>button {
            background-color: #49111c;  /* Glowing reddish button */
            color: white;
            border-radius: 8px;
            font-size: 16px;
            padding: 10px 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 100%;
            margin-top: 20px;
        }
        .stButton>button:hover {
            background-color: #3e0f18;  /* Darker reddish shade on hover */
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
            transform: scale(1.05);  /* Scale effect */
        }
        .stFileUploader {
            background-color: #ffe8d4;  /* Matching background color of page */
            padding: 20px;
            border-radius: 12px;
            border: 2px solid #e1e1e1;
            margin-bottom: 40px;
        }
        .stFileUploader label {
            color: #49111c;  /* Glowing reddish label color */
            font-size: 18px;
            text-shadow: 0 0 10px #49111c, 0 0 20px #49111c, 0 0 30px #49111c;
        }
        .stMarkdown {
            font-size: 18px;
            font-family: 'Verdana', sans-serif;
            color: #0a0908;  /* Dark text */
        }
        .stTextInput input {
            background-color: #FFFFFF;
            color: #0a0908;  /* Dark text for input */
            border: 1px solid #e1e1e1;
            border-radius: 8px;
            font-size: 16px;
            width: 100%;
            padding: 10px;
        }
        .stTextInput input:focus {
            border-color: #49111c;  /* Glowing red border on focus */
        }
        .stTextInput input::placeholder {
            color: #000000;  /* Black placeholder text */
        }
        .stTextInput label {
            color: #49111c;  /* Glowing reddish label text */
            text-shadow: 0 0 10px #49111c, 0 0 20px #49111c, 0 0 30px #49111c;
        }
        .stCode {
            background-color: #f4f4f9;
            color: #333333;
            border-radius: 8px;
            padding: 20px;
            margin-top: 20px;
        }
        .stMarkdown p {
            color: #0a0908;  /* Dark text */
            font-size: 16px;
        }
        .stAlert {
            background-color: #49111c;
            color: white;
            border-radius: 8px;
            padding: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        footer p {
            font-weight: 800;  /* Making footer text bolder */
            color: #0a0908;
        }
    </style>
""", unsafe_allow_html=True)

# Set up encoding and locale
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

# Initialize the Ollama model for SQL generation
ollama = OllamaLLM(base_url="http://localhost:11434", model="sql_gen_model")

# Function to interact with the local LLM
def query_llm(prompt):
    try:
        # Prepare and run the subprocess to interact with the local LLM
        process = subprocess.Popen(
            ['ollama', 'run', 'sql_gen_model'],  
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Prompt is sent to LLM
        stdout, stderr = process.communicate(prompt)
        
        if process.returncode == 0:
            return stdout.strip()
        else:
            return f"Error: {stderr.strip()}"
    except Exception as e:
        return f"An exception occurred: {str(e)}"

# Title (with emoji added and made bolder)
st.markdown("<h1 style='font-weight: 900; text-align: center;'>Querify📊</h1>", unsafe_allow_html=True)

# File upload widget
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Show CSV preview
    st.write("Preview of uploaded CSV:")
    st.dataframe(df)

    # Display the question input after CSV upload
    user_question = st.text_input("What SQL query do you want based on the CSV data?", placeholder="e.g., Show me all students with a grade higher than 90")

    # Button to generate the SQL query
    if st.button("Generate SQL Query"):
        # Prepare the prompt for LLM
        csv_preview = df.head().to_string(index=False)
        prompt = f"Here is a sample of the CSV data:\n\n{csv_preview}\n\nBased on this data, generate a SQL query that answers the following question: {user_question}"
        
        # Query the model (assuming you've set up the query_llm function already)
        response = query_llm(prompt)
        
        # Display the generated SQL query
        st.markdown("### Generated SQL Query:")
        st.code(response)

        # Optional: Explain the generated SQL query if needed
        explanation_prompt = f"Explain the following SQL query:\n{response}"
        explanation = query_llm(explanation_prompt)
        
        st.markdown("### Explanation of the SQL Query:")
        st.write(explanation)

# Add field for SQL help questions
sql_question = st.text_input("Questions regarding SQL?", placeholder="e.g., What are joins?")

# Button to get the answer to SQL questions
if sql_question:
    sql_answer = query_llm(sql_question)
    st.markdown("### Answer to Your SQL Question:")
    st.write(sql_answer)

# Footer with bold text
st.markdown("<p style='text-align: center; font-weight: 800;'>Querify: SQL Query Generator</p>", unsafe_allow_html=True)
