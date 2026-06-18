import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="HSE AI Analyst", layout="wide")

# تنظیم کلید API
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

st.title("🛡️ سیستم آنالیز هوشمند HSE")

uploaded_file = st.file_uploader("یک عکس از محیط کار بارگذاری کنید...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='عکس بارگذاری شده', use_container_width=True)
    
    if st.button("شروع تحلیل"):
        with st.spinner('در حال بررسی ایمنی...'):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = "تو یک کارشناس HSE هستی. این عکس را تحلیل کن و خطرات و راهکارهای پیشگیری را لیست کن."
            response = model.generate_content([prompt, image])
            st.markdown(response.text)
