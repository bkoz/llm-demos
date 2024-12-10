from openai import OpenAI
import gradio as gr
import os

ollama_api_endpoint = os.getenv("OLLAMA_HOST", "http://ollama.ollama")
ollama_model = os.getenv("OLLAMA_MODEL", "granite3-dense:8b")
print(f'ollama_api_endpoint: {ollama_api_endpoint}')

client = OpenAI(
    base_url=f'{ollama_api_endpoint}/v1/',
    # required but ignored
    api_key='ollama',
)

def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})
  
    response = client.chat.completions.create(model=ollama_model,
    messages= history_openai_format,
    temperature=1.0,
    stream=True)

    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
              partial_message = partial_message + chunk.choices[0].delta.content
              yield partial_message

with gr.Blocks() as demo:

    gr.Markdown("# Chat with Lllama3!")
    gr.ChatInterface(predict)

demo.launch(server_name='0.0.0.0', server_port=8081, share=True)
