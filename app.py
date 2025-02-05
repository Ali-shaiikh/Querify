from langchain_ollama import OllamaLLM

ollama = OllamaLLM(base_url="http://localhost:11434", model="sql_gen_model")

import streamlit as st
import pandas as pd
import subprocess
import sys
import locale

sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

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

# Set up the page configuration
st.set_page_config(page_title="Querify", layout="centered")

# Title
st.title("Querify")

# CSV file upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded CSV:")
    st.dataframe(df)

    # Input box for user question
    user_question = st.text_input("What SQL query do you want based on the CSV data?", placeholder="e.g., Show me all students with a grade higher than 90")

    # Button to generate the SQL query
    if st.button("Generate SQL Query"):
        # Prepare the prompt for LLM
        csv_preview = df.head().to_string(index=False)
        prompt = f"Here is a sample of the CSV data:\n\n{csv_preview}\n\nBased on this data, generate a SQL query that answers the following question: {user_question}"
        
        # Get the response from the LLM
        response = query_llm(prompt)
        
        # Display the generated SQL query
        st.markdown("### Generated SQL Query:")
        st.code(response)

        # Optional: Explain the generated SQL query if needed (this can be another call to LLM)
        explanation_prompt = f"Explain the following SQL query:\n{response}"
        explanation = query_llm(explanation_prompt)
        
        # Display the explanation
        st.markdown("### Explanation of the SQL Query:")
        

# Footer
st.markdown("<p style='text-align: center;'> Querify: SQL Query Generator </p>", unsafe_allow_html=True)


