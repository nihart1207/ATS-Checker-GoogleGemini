from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import base64
import os
import io
from PIL import Image
import fitz  # PyMuPDF
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, pdf_content, prompt):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([input_text, pdf_content[0], prompt])
        return response.text
    except Exception as e:
        return f"Error: {e}"

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        first_page = pdf_document.load_page(0)  # load the first page
        pix = first_page.get_pixmap()
        img_byte_arr = io.BytesIO()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# STREAMLIT APP

st.set_page_config(page_title="ATS Resume Bot")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload Resume in PDF format", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell me about the details resume")
submit2 = st.button("How can I improve my skills based on job description?")
submit3 = st.button("What are the key skills/keywords required for this job?")
submit4 = st.button("What percentage of my resume matches the job description?")

input_prompt1 = """
You are an experienced technical human resource manager with tech experience in the field of Data Science, Full Stack Web Development, Big Data Engineering, DevOPS, Data Analyst. Your task is to review the provided resume against the job description for these profiles. Kindly share your professional evaluation on whether the candidate's profile aligns with the given job description.
Highlight the strengths and weaknesses of the applicant in relation to the given job description.
"""
input_prompt2 = """
You are a technical human resource manager with tech experience in the field of Data Science, Full Stack Web Development, Big Data Engineering, DevOPS, Data Analyst. Your role is to scrutinize the resume in light of the job description provided.
Share your thoughts and insights on the candidate's suitability for the role from an HR perspective.
Additionally, offer advice on enhancing the candidate's skills and identify areas to improve.
"""
input_prompt3 = """
You are a technical human resource manager with tech experience in the field of Data Science, Full Stack Web Development, Big Data Engineering, DevOPS, Data Analyst. Your role is to scrutinize the resume in light of the job description provided.
Share your thoughts on the key skills that are required for the given job description.
"""
input_prompt4 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of Data Science, Full Stack Web Development, Big Data Engineering, DevOPS, Data Analyst, and deep ATS functionality. Your task is to evaluate the resume against the provided job description.
Give me the percentage match of the resume with the job description after evaluating the job description. First, the output should come as a percentage, and then keywords missing and final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_prompt1)
        st.subheader("The response is : ")
        st.write(response)
    else:
        st.write("Please upload a PDF file")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_prompt2)
        st.subheader("The response is : ")
        st.write(response)
    else:
        st.write("Please upload a PDF file")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_prompt3)
        st.subheader("The response is : ")
        st.write(response)
    else:
        st.write("Please upload a PDF file")

elif submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_prompt4)
        st.subheader("The response is : ")
        st.write(response)
    else:
        st.write("Please upload a PDF file")
