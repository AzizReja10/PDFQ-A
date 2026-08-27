import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from PyPDF2 import PdfReader
def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text
def main():
    st.set_page_config(page_title="Chat with multiple pdfs",page_icon=":books")
    st.header("Chat with multiple pdfs :books")
    st.text_input("ask question about the documents")
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs=st.file_uploader("upload your pdf",accept_multiple_files=True)
        if st.button("process"):
            with st.spinner("processing"):
                raw_text=get_pdf_text(pdf_docs)


if __name__=='__main__':
    main()