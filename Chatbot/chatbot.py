import gradio as gr # type: ignore
import textwrap
import google.generativeai as genai # type: ignore
import os
import re


def chat_with_gemini(question):
    genai.configure(api_key='AIzaSyDGswQUJ4egHNRMpCht_k1fHBNmtp54sMg')
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    
    prompt = textwrap.dedent(f"""
    please give me answer of provided question in a professional way. and in the end write a thanks sentence.
    question;{question}
    """)
    
    try:
        response = model.generate_content(
            prompt,
            generation_config={'response_mime_type': 'application/json'}
        )
        print("API Response....:", response)

        text = response.text
        text = re.sub(r'{"answer":\s*', '', text)  # Remove "answer": at the start
        text = text.replace('\n', ' ')     # Replace newline characters with spaces
        text = text.replace('}', '')       # Remove closing curly brace
        text = text.replace('"', '')       # Remove double quotes
        text = text.strip()          
        return text
    except Exception as e:
        return f"An error occurred: {str(e)}"
    

def format_history(msg:str, history:list[list[str,str]], system_promt:str):
    chat_history = [{'role':'user', 'System':system_promt}]
    for query, response in history:
        chat_history.append({'role':'user','content':query})
        chat_history.append({'role':'assistant','content':response})
    chat_history.append({'role':'user','content':msg})
    return chat_history


def generate_response(msg:str, history:list[list[str,str]], system_promt:str):
    
    chat_history = format_history(msg, history, system_promt)
    ai_response = chat_with_gemini(msg)
    yield ai_response

# Custom CSS for avatar image size
css = """
.avatar {
    width: 120px;
    height: 120px;
}
"""

chatbot = gr.ChatInterface(
    generate_response,
    chatbot=gr.Chatbot(
        avatar_images = ['Chatgpt.jpg','user.jpg'],
        height = '120vh'
    ),
    additional_inputs=[gr.Textbox('behaviour as if you are professioal writer',label='System Prompt',lines=5)],
    title='Basic Chatbot',
    description='Feel free to ask about your Problems and queries!',
    show_progress=True,
    theme='soft',
    submit_btn='Send ➙',
    retry_btn='🔄 Generate Response',
    undo_btn='↪ Delete Previous',
    clear_btn='🗑 Clear Chat',
    css=css
)

chatbot.launch()
