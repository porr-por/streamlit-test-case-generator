import streamlit as st
import openai
import os

# Retrieve the API key from the environment variable
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client with the API key
openai.api_key = OPENAI_API_KEY

# Define the function to generate test cases
def generate_test_cases(requirement):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant capable of generating software test cases."},
            {"role": "user", "content": requirement}
        ]
    )
    return response.choices[0].message.content

# Streamlit app layout
st.title('AI-powered Test Case Generator')
st.write('Enter your software requirement to generate test cases.')

# Text area for user to enter the software requirement
requirement = st.text_area("Requirement", height=150)

# Button to generate test cases
if st.button('Generate Test Cases'):
    if requirement:
        with st.spinner('Generating...'):
            try:
                test_cases = generate_test_cases(requirement)
                st.success('Generated Test Cases')
                st.write(test_cases)
            except Exception as e:
                st.error('An error occurred while generating test cases.')
                st.error(e)
    else:
        st.error('Please enter a requirement to generate test cases.')
