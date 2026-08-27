import streamlit as st


def main():
    st.set_page_config(page_title="Chat with multiple pdfs",page_icon=":books")
    st.header("Chat with multiple pdfs :books")
    st.text_input("ask question about the documents")
    with st.sidebar:
        st.subheader("Your documents")
        
    

if __name__=='__main__':
    main()