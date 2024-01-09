import requests
import numpy as np
import streamlit as st
import pickle

# Function to load model from a URL using pickle
def load_model_from_url(url):
    response = requests.get(url)
    model = pickle.loads(response.content)
    return model
    

# Load the model from the GitHub URL
import pickle

# Replace 'path/to/trained_modelIntell.sav' with the actual path to the downloaded file
model_path = 'https://github.com/Niihaad/ML_Algorithms/blob/main/trained_modelIntell.sav'

# Load the model using pickle
with open(model_path, 'rb') as file:
    loaded_model = pickle.load(file)

def smartness_prediction(input_data):
    predicted_outcome = loaded_model.predict(input_data)
    return 'You are ' + str(predicted_outcome[0])

def main():
    st.title('Test Your Level of Smartness By Nihad ')
    
    usingGpt = st.text_input('On a scale from 0 to 1, how frequently do you use ChatGPT ?')
    usingGoogle = st.text_input('On a scale from 0 to 1, how often do you rely on Google ?')
    usingMind = st.text_input('On a scale from 0 to 1, how frequently do you engage your mind ?')
    
    total = ''
    if st.button("Predict Smartness"):
        try:
            gpt_val = float(usingGpt)
            google_val = float(usingGoogle)
            mind_val = float(usingMind)
            input_data = np.array([gpt_val, google_val, mind_val]).reshape(1, -1)
            total = smartness_prediction(input_data)
        except ValueError as e:
            st.error(f"Error: {e}. Please enter valid numerical values.")
            total = "Please enter valid numerical values."

    st.success(total)
    
if __name__=='__main__':
    main()
