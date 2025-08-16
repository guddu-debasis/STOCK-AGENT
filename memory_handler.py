
import json
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

def load_memory_from_file(file_path="chat_history.txt"):
    history = InMemoryChatMessageHistory()
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            for msg in data:
                if msg["type"] == "human":
                    history.add_user_message(msg["content"])
                elif msg["type"] == "ai":
                    history.add_ai_message(msg["content"])
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        print("⚠️ Corrupted chat history file, starting fresh.")
    return history

def save_memory_to_file(history, file_path="chat_history.txt"):
    data = []
    for msg in history.messages:
        data.append({
            "type": msg.type,
            "content": msg.content
        })
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
