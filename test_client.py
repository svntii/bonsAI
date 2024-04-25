import requests

def start_conversation():
    response = requests.post("http://127.0.0.1:8000/chat")
    data = response.json()
    conversation_id = data["id"]
    bot_message = data["response"]
    print(bot_message + "\n")
    print("suggested: " + str(data["suggested_responses"]))
    return conversation_id

def continue_conversation(conversation_id, user_input):
    response = requests.post(f"http://127.0.0.1:8000/chat/{conversation_id}", json={"prompt": user_input})
    data = response.json()
    bot_message = data["response"]
    print("\nSteddie: " + bot_message + "\n")
    print("suggested: " + str(data["suggested_responses"]) + "\n")
    print("sources: " + str(data["sources"]))

def main():
    conversation_id = start_conversation()
    
    while True:
        user_input = input("You: ")
        continue_conversation(conversation_id, user_input)

if __name__ == "__main__":
    main()