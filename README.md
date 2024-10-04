# Openshift and Openshift AI Test Drive for LLMs. 

## What's needed. This should be already installed.

- Tested on Openshift AI (v2.13) on Openshift Container Platform (v4.16)
- The Ollama model server running in the `ollama` namespace.
  - The following models should be already pulled.
    - `llama3.2` and `all-minillm` models.
- A data science project called `demos` has been created.

### User Setup

- Login as `user5`
- Create and start a data science workbench named `llm-clients` using a small, minimal python 
notebook image.
- Clone this repo (`https://github.com/bkoz/llm-demos.git`)
- Open a terminal within Jupyter and install the python requirements.

```bash
pip install pip -Uq
pip install -r requirements.txt
```

Run the notebooks in order.
