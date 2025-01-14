import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

        def extract_jobs(self, cleaned_text):
            prompt_extract = PromptTemplate.from_template(
                """
                                ### SCRAPED TEXT FROM WEBSITE:
                                {page_data}
                                ### INSTRUCTION:
                                The scraped text is from the career's page of a website.
                                Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
                                Only return the valid JSON.
                                ### VALID JSON (NO PREAMBLE):
                                """
                        )

            chain_extract = prompt_extract | self.llm
