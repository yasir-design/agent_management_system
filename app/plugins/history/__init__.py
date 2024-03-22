import os
import logging
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.commands import Command

class MovieExpertChat(Command):
    def __init__(self):
        super().__init__()
        self.name = "counselor"
        self.description = "Talk to AI College Admissions Counselor to get guidance on college applications"
        self.history = []
        load_dotenv()
        API_KEY = os.getenv('OPEN_AI_KEY')
        # you can try GPT4 but it costs a lot more money than the default 3.5
        self.llm = ChatOpenAI(openai_api_key=API_KEY, model="gpt-4-0125-preview")  # Initialize once and reuse
        # This is default 3.5 chatGPT
        # self.llm = ChatOpenAI(openai_api_key=API_KEY)  # Initialize once and reuse

    def calculate_tokens(self, text):
        # More accurate token calculation mimicking OpenAI's approach
        return len(text) + text.count(' ')

    def interact_with_ai(self, user_input, character_name):
        # Generate a more conversational and focused prompt
        prompt_text = "You are a large language model, named Spike AI, specializing in college admissions. You are given a user question, and please write clean, concise and accurate answer to the question. Please give as much explicit, specific details from the context as is relevant to the question. Your answer must be correct, accurate and written by an expert using an unbiased and professional tone. Focus solely on college admissions and counseling. If the provided contexts lack enough information to answer a query, prompt the user to ask a more specific question related to their college application by saying, 'Please ask a question related to your college application!' followed by a suggested topic. DO NOT EVER TALK ABOUT ANYTHING OTHER THAN COLLEGE ADMISSONS & COLLEGE COUNSELING EVER!!"
        prompt = ChatPromptTemplate.from_messages(self.history + [("system", prompt_text)])
        
        output_parser = StrOutputParser()
        chain = prompt | self.llm | output_parser

        response = chain.invoke({"input": user_input})

        # Token usage logging and adjustment for more accurate counting
        tokens_used = self.calculate_tokens(prompt_text + user_input + response)
        logging.info(f"OpenAI API call made. Tokens used: {tokens_used}")
        return response, tokens_used

    def execute(self, *args, **kwargs):
        character_name = kwargs.get("character_name", "Admissions Counselor")
        print(f"Hello, I am your college admissions counselor! Ask away anything related to your application. Type 'done' to exit anytime.")

        while True:
            user_input = input("You: ").strip()
            if user_input.lower() == "done":
                print("Thank you for using the College Admissions Counselor Chat. Goodbye!")
                break

            self.history.append(("user", user_input))
            
            try:
                response, tokens_used = self.interact_with_ai(user_input, character_name)
                print(f"College Admissions Counselor: {response}")
                print(f"(This interaction used {tokens_used} tokens.)")
                self.history.append(("system", response))
            except Exception as e:
                print("Sorry, there was an error processing your request. Please try again.")
                logging.error(f"Error during interaction: {e}")

