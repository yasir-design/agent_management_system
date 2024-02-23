import os
import sys
from app.commands import Command
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


class BobCommand(Command):
    def execute(self):
        print("Type 'done' to exit.")
        load_dotenv()
        API_KEY=os.getenv('OPEN_AI_KEY')
        while True:  #REPL Read, Evaluate, Print, Loop
            llm = ChatOpenAI(openai_api_key="")
            prompt = ChatPromptTemplate.from_messages([
            ("system", "Your name is George and you love vanilla ice cream"),
            ("user", "{input}")
        ])
            output_parser = StrOutputParser()
            chain = prompt | llm | output_parser
            user_input = input("George: ").strip()
            if user_input == "done":
                break
            x = chain.invoke({"input": user_input})
            print(x)