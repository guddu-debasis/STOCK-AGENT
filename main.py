
from memory_handler import load_memory_from_file
from prompt_template import chat_template
from model_setup import get_model
from tool_handler import tools
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.messages import HumanMessage, AIMessage

def run_chat():
    
    memory = [] 
    
    model = get_model() 
    agent = create_tool_calling_agent(model, tools, chat_template)
    
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=True, 
        handle_parsing_errors=True
    )

    print("🤖 Stock Agent ready! Type 'exit' or 'quit' to leave.")

    while True:
        query = input("You: ")
        if query.lower() in ["exit", 'quit']:
            print("Goodbye!")
            break

        try:
         
            response = agent_executor.invoke({
                "input": query,
                "chat_history": memory
            })
            ai_response = response.get('output', 'Sorry, I encountered an error.')
        except Exception as e:
            ai_response = f"An error occurred: {e}"

        print(f"AI: {ai_response}")

      
        memory.append(HumanMessage(content=query))
        memory.append(AIMessage(content=ai_response))

if __name__ == "__main__":
    run_chat()