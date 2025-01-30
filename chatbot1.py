from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"  # You can use other models like "gpt2-medium", "gpt2-large", or "gpt2-xl"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Ensure the model is in evaluation mode
model.eval()


# Function to generate response
def chatbot_response(input_text):
    # Encode the input text
    inputs = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")

    # Generate the response
    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_length=150,  # You can adjust the length of the response
            num_beams=5,  # Beam search to improve the quality of the responses
            no_repeat_ngram_size=2,  # Prevent repetition of n-grams
            top_p=0.95,  # Top-p sampling to control diversity
            temperature=0.7,  # Controls the randomness of the output
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id,
            early_stopping=True
        )

    # Decode the generated response and return it
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response


# Chatbot loop
def chat():
    print("Hello! I am a GPT-2 chatbot. Type 'quit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        response = chatbot_response(user_input)
        print("Chatbot: " + response)


# Start the chatbot
if __name__ == "__main__":
    chat()
