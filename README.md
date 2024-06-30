
# Gemini Explorer Mission

## Overview
Gemini Explorer is an interactive assistant powered by Google Gemini and built using Streamlit. It allows users to interact with ReX, the assistant, in various communication styles such as Standard, Pirate Speak, and GenZ Speak. This project aims to demonstrate the integration of Google Vertex AI with Streamlit to create a conversational AI application.

## Installation

**### Clone the Repository
-->git clone https://github.com/Bealux007/Gemini-Explorer-Mission.git
-->cd Gemini-Explorer-Mission**

**Install Dependencies
-->pip install -r requirements.txt**

Usage
Running the Application
To start the application, run the following command:

-->streamlit run explorer.py

This will launch the Streamlit application in your default web browser.

Contributing
We welcome contributions to the Gemini Explorer project. To contribute, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -am 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Create a new Pull Request.
License
This project is licensed under the RadicalX License. See the LICENSE file for details.

python
Copy code

### explorer.py

This script sets up a Streamlit interface for interacting with the Gemini model using Vertex AI. It includes the following key functionalities:

1. **Environment Setup**: Loads environment variables and initializes Vertex AI with explicit credentials.
2. **Model Configuration**: Configures the model with specific parameters such as temperature and top_k.
3. **Streamlit Interface**: Sets up the user interface with options for different communication styles, user input, and displays chat history.

```python
import os
import streamlit as st
from google.oauth2 import service_account
import vertexai
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel

# Load environment variables if using .env
from dotenv import load_dotenv
load_dotenv()

# Specify the path to your service account key file
service_account_key_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', 'application_key.json')
credentials = service_account.Credentials.from_service_account_file(service_account_key_path)

# Initialize VertexAI with explicit credentials
project_id = "sample-gemini-explorer-427012"
vertexai.init(project=project_id, credentials=credentials)

# Set up the model configuration
config = generative_models.GenerationConfig(temperature=0.4, top_k=30)
model_name = "gemini-1.0-pro-vision"

# Initialize the model
model = GenerativeModel(model_name=model_name, generation_config=config)

# Define a function to handle the model interaction
def query_model(query):
    if query:
        response = model.generate_content(query)
        return response.text
    return "Please enter a query."

# Streamlit interface setup
st.title("Gemini Explorer")

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Style selection
style = st.selectbox("Choose your communication style:", ["Standard", "Pirate Speak", "GenZ Speak"])

# Define initial messages based on style
initial_messages = {
    "Standard": "Hello! I'm ReX, your assistant powered by Google Gemini. How can I assist you today?",
    "Pirate Speak": "Ahoy matey! Ye be speakin' with ReX, the swashbuckling assistant. What be yer request?",
    "GenZ Speak": "Heyyy, I'm ReX 😎 Just vibin'. What's up? What do you need help with?"
}

# User input
user_input = st.text_input("Type your question here:", key="unique_user_input_key")
output = ""  # Initialize output to ensure it is always defined

if st.button("Send"):
    if not st.session_state.get('messages'):  # Check if the chat history is empty
        output = initial_messages[style]  # Send initial message based on selected style
    else:
        output = query_model(user_input)
    st.write("Response:", output)

    # Update chat history upon sending a query
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    st.session_state.messages.append({"User": user_input, "Gemini": output})

# Display chat history
for index, message in enumerate(st.session_state.messages):
    content = f"User: {message['User']}\nGemini: {message['Gemini']}"
    st.text_area("Chat", value=content, height=300, key=f"chat_history_{index}")

**requirements.txt
List all the dependencies required for your project. This file ensures that all necessary packages are installed when someone sets up your project.**


streamlit
google-cloud-aiplatform
vertexai
python-dotenv
By following these instructions, you'll have a comprehensive README.md file and a well-documented explorer.py script, making it easy for others to understand and use your project.

