import os
from pathlib import Path

import streamlit as st
from datetime import datetime

from dotenv import load_dotenv, find_dotenv

from services.gpt_service import GPTService
from services.prompt_chain_service import ChainPromptsService
from utils import list_files_in_directory, find_first_python_code

_ = load_dotenv(find_dotenv())
PROMPT_TEMPLATE_DIR = os.environ["PROMPT_TEMPLATE_DIR"]

st.set_page_config(page_title="GPT Response Generator")

html_temp = """<div style="background-color:{};padding:1px"></div>"""
with st.sidebar:
    st.markdown(
        """
    ## About 
    GPT Response Generator is an easy-to-use tool that quickly generates meaningful responses to any given topic. 
    """
    )
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"), unsafe_allow_html=True)

    st.markdown(
        """
    ## How does it work?
    Simply enter the topic of interest into the text field and the GPT algorithm will use its vast knowledge of language to generate relevant responses.
    """
    )
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"), unsafe_allow_html=True)

    st.markdown(
        """
    ## Options 
    """
    )
    template_file_name = st.selectbox(
        "Template:", list_files_in_directory(PROMPT_TEMPLATE_DIR)
    )

    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"), unsafe_allow_html=True)

    st.markdown(
        """
    Made by Eugene Bokach
    """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
# GPT Response Generator
"""
)

input_text = st.text_area(
    "Topic of interest (press Ctrl-Enter once you have completed your inquiry)",
    disabled=False,
    placeholder="What topic you would like to ask?",
)

if input_text:
    prompt = str(input_text)
    if prompt:
        if st.button("Submit"):
            template_file_path = Path(PROMPT_TEMPLATE_DIR) / Path(template_file_name)
            with open(template_file_path) as f:
                output = ChainPromptsService(
                    prompts_templates=f.read(),
                    gpt_service=GPTService(),
                ).generate(
                    initial_text=prompt,
                )

            today = datetime.today().strftime("%Y-%m-%d")
            topic = input_text + "\n@Date: " + str(today) + "\n" + output

            st.info(output)
            filename = "Response_" + str(today) + ".txt"
            btn = st.download_button(
                label="Download Text", data=topic, file_name=filename
            )

            first_python_code = find_first_python_code(output)

            # Выполнение сгенерированного кода
            st.markdown("### Executing Generated Code")
            try:
                exec_globals = {}
                exec(first_python_code)
                st.success("Code executed successfully.")
                st.write(exec_globals)
            except Exception as e:
                st.error(f"Error executing code: {e}")
