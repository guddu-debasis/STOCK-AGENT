
import chainlit as cl
from prompt_template import chat_template
from model_setup import get_model
from tool_handler import tools
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.messages import HumanMessage, AIMessage

@cl.on_chat_start
async def start_chat():
    """
    This function initializes the agent when a new chat session starts.
    """
    model = get_model() 
    agent = create_tool_calling_agent(model, tools, chat_template)
    
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=True, 
        handle_parsing_errors=True
    )

   
    cl.user_session.set("agent_executor", agent_executor)
    cl.user_session.set("memory", [])

   

@cl.on_message
async def main(message: cl.Message):
    """
    This function is called every time a user sends a message.
    """
    agent_executor = cl.user_session.get("agent_executor")
    memory = cl.user_session.get("memory")

    callback_handler = cl.LangchainCallbackHandler(stream_final_answer=False)

    
    response = await agent_executor.ainvoke(
        {
            "input": message.content,
            "chat_history": memory
        },
        callbacks=[callback_handler]
    )

    ai_response = response.get('output', 'Sorry, I encountered an error.')
    
   
    await cl.Message(content=ai_response).send()
    
   
    memory.append(HumanMessage(content=message.content))
    memory.append(AIMessage(content=ai_response))