import os
import google.generativeai as genai

# Configure your Gemini API key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Function to generate text with the Gemini API
def generate_text(prompt):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([prompt])
    return response[0].get('text', '') if response else "I'm sorry, I couldn't process that request."

# Main function to handle conversation
def start_conversation():
    context = "AI: Hello! How can I help you today?"
    print("AI: Hello! Type '/start' to begin the conversation or '/end' to end it.")
    conversation_started = False

    while True:
        try:
            user_input = input("You: ")
            print(f"User input: {user_input}")

            if user_input.strip().lower() == "/start":
                conversation_started = True
                context = "AI: Conversation started! You can start typing your questions."
                print(context)
            elif user_input.strip().lower() == "/end":
                print("AI: Conversation ended. Goodbye!")
                break
            elif conversation_started:
                context += "\nYou: " + user_input
                response = generate_text(context)
                
                # Split the response into lines and take only the first relevant AI response
                ai_responses = [line for line in response.split("\n") if line.startswith("AI:")]
                if ai_responses:
                    ai_response = ai_responses[0].strip()
                else:
                    ai_response = "I'm sorry, I couldn't process that request."

                print(f"AI: {ai_response}")
                context += "\n" + ai_response

                # Truncate context if it becomes too long
                if len(context.split()) > 500:
                    context = "AI: How can I help you further?"

            else:
                print("AI: Please type '/start' to begin the conversation or '/end' to end it.")
        except Exception as e:
            print(f"Error during conversation: {e}")

# Example usage
if __name__ == "__main__":
    try:
        start_conversation()
    except Exception as e:
        print(f"Unexpected error: {e}")
