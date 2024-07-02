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
    # test