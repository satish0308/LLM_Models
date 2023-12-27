from dotenv import load_dotenv


load_dotenv() ## load all the env variables from env

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# function to load Gemini Pro Vision

model=genai.GenerativeModel('gemini-pro-vision')

def get_gemini_reponse(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
                {
                      "mime_type": uploaded_file.type,
                      'data':bytes_data 

                }

        ]
        return image_parts
    else:
        raise FileExistsError("No File Loaded")


st.set_page_config(page_title="Multilanguage Invoice Extractor")

st.header("Gives Image Details")

input=st.text_input("Input Prompt:" ,key="input")
uploaded_file=st.file_uploader('Choose a file to upload',type=['jpg', 'png','jpeg'])

image=""

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption='Uploaded Images',use_column_width=True)

submit=st.button('Tell me about the Image')


input_prompt="""
        You are an expert in animals and its behaviors.you will be able to asnwer all questions about it
"""


# if submit is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_reponse(prompt=input_prompt,image=image_data,input=input)

    st.subheader("The Reponse is")
    st.write(response)

st.header("Generate Images")
input2=st.text_input("Input Prompt:" ,key="input2")

def get_gemini_reponse_image(input,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([input,prompt])
    return response


input_prompt_image="""
        You are an expert image generaing and generates image 
"""

submi_image=st.button('Create a Image for me')
if submi_image:
    #image_data=input_image_setup(uploaded_file)
    response=get_gemini_reponse_image(prompt=input_prompt_image,input=input2)

    st.subheader("The Generated Image is")
    response_image_data = response.output.image.data

# Create a BytesIO object to read the image data
    image_bytes_io = BytesIO(response_image_data)

    # Open the image using PIL
    image = Image.open(image_bytes_io)

# Open the image using PIL
    image = Image.open(image_bytes_io)
    st.write(image)






