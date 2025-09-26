import os 
import streamlit as st 
import google.generativeai as genai 

from dotenv import load_dotenv, find_dotenv

def ask_and_get_answer(prompt, img):
    model=genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_contentm([prompt, img])
    return response.text 

def st_image_to_pil(st_image):
    import io
    from PIL import Image
    image_data = st.image.read()
    pil_image = Image.open(io.BytesIO(image_data))
    return pil_image

if __name__ == '__main__':
    load_dotenv(find_dotenv(), override=True)
    genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

    st.image('gemini.png')
    st.subheader('Talking with an Image')

    img = st.file_uploader('Select an Image: ', type=['jpg', 'jpeg', 'png', 'gif'])
    if img:
        st.image(img, caption='Talk with this image.')

        prompt = st.text_area('Ask a question about this image: ')
        if prompt:
            pil_image = st_image_to_pil(img)
            with st.spinner('Runnging...'):
                answer = ask_and_get_answer(prompt, pil_image)
                st.text_area('Gemini Answer: ', value=answer)

            st.divider()
            