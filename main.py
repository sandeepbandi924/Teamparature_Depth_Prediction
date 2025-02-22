import streamlit as st
import numpy as np

import tensorflow as tf
# from tensorflow.keras.losses import MeanSquaredError
import pickle

# Cache model loading to prevent reloading on every interaction
@st.cache_resource
def load_scaler(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

@st.cache_resource
def load_model_file(model_path):
    return tf.keras.models.load_model(model_path, custom_objects={'mse': tf.keras.losses.MeanSquaredError})

# Load scalers once at startup
SCALERS = {
    'Texas': load_scaler('scaler_texas.pkl'),
    'New York': load_scaler('scaler_newYork.pkl')
}

# Model configuration
MODEL_FILES = {
    'New York': 'model_newYork.h5',
    'Texas': 'model_texas.h5'
}

# UI setup
st.title('Weather Prediction Model')

model_choice = st.selectbox(
    'Choose a model:',
    options=list(MODEL_FILES.keys()),
    index=0
)

# Load selected model
model = load_model_file(MODEL_FILES[model_choice])

def predict_values(inputs, model_choice, model):
    """Make predictions based on user inputs and return as a labeled dictionary."""
    input_array = np.array([inputs], dtype=np.float32)
    scaler = SCALERS[model_choice]
    scaled_input = scaler.transform(input_array)
    predictions = model.predict(scaled_input, verbose=0)[0].tolist()  # Get the list of predictions

    # 🎯 Customize output labels based on model choice
    if model_choice == 'Texas':
        prediction_labels = ['Temp_0.9m', 'Temp_1.8']
    elif model_choice == 'New York':
        prediction_labels = ['Temp_0.3m_C', 'Temp_0.6m_C', 'Temp_0.91m_C', 'Temp_1.21m_C']
    else:
        prediction_labels = [f'Output_{i+1}' for i in range(len(predictions))]

    return dict(zip(prediction_labels, predictions))

# Input fields with better organization
with st.form(key='prediction_form'):
    col1, col2, col3 = st.columns(3)
    with col1:
        input1 = st.number_input('Air Temp (°C)', step=0.1)
    with col2:
        input2 = st.number_input('Rainfall (inch)', step=0.01)
    with col3:
        input3 = st.number_input('Day of Year', min_value=1, max_value=366, step=1)
    
    submit_button = st.form_submit_button(label='Predict')

# Process prediction and display results
if submit_button:
    try:
        inputs = [input1, input2, input3]
        predictions = predict_values(inputs, model_choice, model)
        
        # 🎯 Display the predictions in the requested format
        st.subheader('Prediction Tempratures are: ')
        st.json(predictions)  # Pretty JSON-like output with keys and values

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
