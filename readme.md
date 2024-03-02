# Project: Agent Management System

## Introduction

This project is a demo of an in memory history for a movie agent.  

## Assignment

Take this code and make a new plugin to become an expert in something else.

## Midterm Suggestions:
1.  Implement Retrieval Augmented Generation (RAG) with some type of custom data.

[watch this to start](https://www.youtube.com/watch?v=tcqEUSNCn8I)


2.  Install different local modals and compare the quality of their output using a standardized process of questions / interactions.

[Intall Local Model](https://www.youtube.com/watch?v=VPW6mVTTtTc)

3.  Come up with your own project?

## Project Setup

1. Clone the repository.
2. CD into the project folder.
3. Create and activate the virtual environment (VE).
4. Install the required libraries.
5.  Signup for OpenAI Api Key.  Make .env file and put the key in as "open_ai_key=YOUR_KEY"

## Testing Commands

- Run all tests with `pytest`.
- To test a specific file, use `pytest tests/test_main.py`.
- For linting and coverage, `pytest --pylint --cov` commands can be used separately.

## Installed Libraries

1. [Pytest](https://docs.pytest.org/en/8.0.x/)
2. [Faker](https://faker.readthedocs.io/en/master/)
3. [Pytest Coverage](https://pytest-cov.readthedocs.io/en/latest/readme.html)
4. [Pytest Pylint](https://pylint.readthedocs.io/en/stable/development_guide/contributor_guide/tests/launching_test.html)
5. [Langchain](https://python.langchain.com/docs/get_started/quickstart)


## Adding a Library

1. Ensure you're in the correct VE; if unsure, run "deactivate".
2. Activate the VE.
3. Update the requirements file with `pip freeze > requirements.txt`.

