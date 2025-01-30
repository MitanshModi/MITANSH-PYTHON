import random

# Define a dictionary of simple responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I assist you?"],
    "how are you": ["I'm good, thank you!", "I'm doing great! How about you?", "I'm fine, how can I help?"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "what is your name": ["I'm a Python chatbot.", "You can call me Chatbot!", "I'm just a friendly chatbot!"],
    "default": ["Sorry, I didn't understand that.", "Could you please clarify?", "I'm not sure how to respond to that."]
}


# Function to handle chatbot responses
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Check if the user's input matches any predefined response
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    # If no match is found, return a default response
    return random.choice(responses["default"])


# Function to interact with the chatbot
def start_chat():
    print("Chatbot: Hello! How can I assist you today?")

    while True:
        user_input = input("You: ")

        # Exit the chatbot if the user types 'bye'
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Get the chatbot's response and print it
        response = chatbot_response(user_input)
        print("Chatbot:", response)


# Run the chatbot
if __name__ == "__main__":
    start_chat()
