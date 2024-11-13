# Openshift and Openshift AI Test Drive for LLMs. 

## What's needed. This should be already installed.

- Tested on Openshift AI (v2.13) on Openshift Container Platform (v4.16)
- The [Ollama model server](https://github.com/bkoz/ollama) running in the `ollama` namespace.
  - The following models should be already pulled.
    - `llama3.2` and `all-minillm` models.

### User Setup

- Login 
- Create a Data Science Project called `llm-demos`.
- Create and start a data science workbench named `llm-clients` using a small, minimal python 
notebook image.
- Clone this repo (Main Menu: Git -> Clone a Repository)

Run the notebooks in order.

`01-chat-llama.ipynb` - A simple chatbot that interacts with an LLM via
an OpenAI compatible python SDK.

`03-weaviate.ipynb` - A simple RAG application that imports 1000 Jeopardy
questions and creates a user interface.
The data import will take a minute or so to complete. The application allows the user
to search the vector database for objects similar to a natural language query then asks the LLM to 
summarize the results. 

If any code changes are made to the notebook after the gradio app is run, the notebook kernel
will need to get restarted.


