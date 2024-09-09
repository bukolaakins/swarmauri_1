from dotenv import load_dotenv
import os
import gradio as gr
from swarmauri.standard.llms.concrete.GroqModel import GroqModel
from swarmauri.standard.messages.concrete.SystemMessage import SystemMessage
from swarmauri.standard.agents.concrete.SimpleConversationAgent import SimpleConversationAgent
from swarmauri.standard.conversations.concrete.MaxSystemContextConversation import MaxSystemContextConversation

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")


llm = GroqModel(api_key=API_KEY)

allowed_models = llm.allowed_models

conversation = MaxSystemContextConversation()

def load_model(selected_model):
    return GroqModel(api_key=API_KEY, name=selected_model)

def converse(input_text, history, system_context, model_name):
    print(f"sysem_context: {system_context}")
    print(f"Select_model: {model_name}")
    
    llm = load_model(model_name)
    
    agent = SimpleConversationAgent(llm=llm, conversation=conversation)
    
    agent.conversation.system_context = SystemMessage(content=system_context)
    
    
    input_text = str(input_text)
    print(conversation.history)
    #Execute input command with the agent
    result = agent.exec(input_text)
    print(result, type(result))
    
    #return the result as a string
    return str(result)


# Set up the Gradio ChatInterface with a dropdwon for model selection

demo = gr.ChatInterface(
    fn=converse,
    additional_inputs=[
        gr.Textbox(label="system Context"),
        gr.Dropdown(label="Model Name", choices=allowed_models, value=allowed_models[0])
    ],
    title="A system Context Conversation",
    description="Interact with the agent using the selected model and system context."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8000)
