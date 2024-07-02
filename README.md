
# Gemini Explorer Mission
Create a user-friendly chat interface using Streamlit that connects with Google's state-of-the-art large language model, Gemini. The goal is to provide an accessible platform for exploring and showcasing the capabilities of advanced language models. This project aims to serve as an educational and practical introduction to integrating large language models with intuitive interfaces.

• Mission Workflow:

• Task 1: 🌐 Enable Google Cloud

• Task 2: 🧬 Google Cloud Initialization

• Task 3: ☁️ Setting up Google Gemini

• Task 4: 📊 Streamlit Integration

• Task 5: 🗣️ Adding Initial System Messages

• Task 6: 📄 Preparing Submission

## Overview
Gemini Explorer is an interactive assistant powered by Google Gemini and built using Streamlit. It allows users to interact with ReX, the assistant, in various communication styles such as Standard, Pirate Speak, and GenZ Speak. This project aims to demonstrate the integration of Google Vertex AI with Streamlit to create a conversational AI application.

## Installation & Clone the Repository
• git clone

• cd Gemini-Explorer-Mission

## Install Dependencies
• pip install -r requirements.txt

## Usage & Running the Application
To start the application, run the following command:
• streamlit run explorer.py

## Mission Workflow:

## Task 1: 🌐 Enable Google Cloud

![Screenshot 2024-06-20 075839](https://github.com/Bealux007/Gemini-Explorer-Mission/assets/102096427/6ae469cf-bae0-4c7e-a0e8-f02ce93fb21a)

• Go to Google Cloud Platform and start a free trial.

• Sign in and complete the setup, including billing requirements.

• Create a new project (e.g. "Sample-Gemini-Explorer").

• Enable Vertex AI and its recommended APIs.


## Task 2: 🧬 Google Cloud Initialization

![Screenshot 2024-06-23 144745](https://github.com/Bealux007/Gemini-Explorer-Mission/assets/102096427/1e1cda6d-3790-4134-882f-029b6c774752)

• Install the[ Google SDK ](https://cloud.google.com/sdk?hl=en)from here.

• Initialize the SDK: gcloud init

• Sign in and configure your project and compute region.

## Task 3: ☁️ Setting up Google Gemini

![Screenshot 2024-06-23 171135](https://github.com/Bealux007/Gemini-Explorer-Mission/assets/102096427/6a3e80c2-496a-430d-a909-7ba3e7d0823a)

• Install Streamlit: pip install streamlit

• Refer to the[ Streamlit Documentation ](https://docs.streamlit.io/)for examples.

• Use the project ID instead of the project name from google cloud to avoid permission issues:
project = "project-id"

## Task 4: 📊 Streamlit Integration

![Screenshot 2024-06-25 111846](https://github.com/Bealux007/Gemini-Explorer-Mission/assets/102096427/b7e7d170-3309-4a9a-baf4-c5295973b105)

• Create llm_function for Gemini-model that can take input and show response by use of integrating Streamlit.

• Run the application: streamlit run explorer.py

## Task 5: 🗣️ Adding Initial System Messages

![Screenshot 2024-06-26 231909](https://github.com/Bealux007/Gemini-Explorer-Mission/assets/102096427/c34eb498-f6ce-44f7-8f53-d753b7853879)

• Set up initial system messages to introduce the assistant using different styles (Standard, Pirate Speak, GenZ Speak).

## Task 6: 📄 Preparing Submission

• Create a GitHub repository for the project containing all the project files.

• Record a Loom video representing the overall approach.[ Loom Link ](https://www.loom.com/share/375ebbf3c55541e38bf11056435846b1?sid=20166afc-a464-486c-a7e8-9ed6f51d39ea)

## Issues Faced
⚠️ Issue 403: Permission Denied Error
• Cause: This happens if you use the project name instead of the project ID or if the service account is not correctly configured.
• Solution: Use the project ID and ensure the service account has the necessary permissions.

⚠️ Google Authentication Error
• Cause: Missing or incorrect service account credentials.
• Solution: Ensure the GOOGLE_APPLICATION_CREDENTIALS environment variable is set correctly with the path to the service account key file.

⚠️ Model Error
• Cause: Configuration issues or incorrect API usage.
• Solution: Verify the model configuration and API calls according to the documentation.

## Acknowledgements
Thanks to Talha Sabri and Mikhail Ocampo for the opportunity to complete this AI mission.


### explorer.py

This script uses Vertex AI to set up a Streamlit interface for interacting with the Gemini model. It includes the following key functionalities:

1. **Environment Setup**: Loads environment variables and initializes Vertex AI with explicit credentials.
2. **Model Configuration**: Configures the model with specific parameters such as temperature and top_k.
3. **Streamlit Interface**: Sets up the user interface with options for different communication styles, user input, and displays chat history.


## Requirements.txt
List all the dependencies required for your project. This file ensures that all necessary packages are installed when someone sets up your project.

• streamlit

• google-cloud-aiplatform

• vertexai

• python-dotenv


By following these instructions, we can have a comprehensive README.md file and a well-documented explorer.py script, making it easy for others to understand and use your project.

