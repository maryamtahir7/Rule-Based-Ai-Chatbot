"""
Project 1: Rule-Based AI Chatbot
----------------------------------
A simple rule-based chatbot that responds to predefined user inputs
using if-else logic and runs in a continuous loop.

Key Requirements covered:
- Handle greetings and exit commands
- Use if-else logic for responses
- Run in a continuous loop

Key Skills demonstrated:
- Control flow
- Decision-making logic
- Basic AI concepts (pattern matching / rule-based response)
"""

import random
from datetime import datetime

# ---------------------------------------------------------
# Predefined response rules
# Each key is a list of trigger keywords, each value is a
# list of possible responses (chosen randomly for variety).
# ---------------------------------------------------------

GREETINGS = ["hi", "hello", "hey", "hii", "helo", "namaste", "yo"]
EXIT_COMMANDS = ["bye", "exit", "quit", "goodbye", "stop", "close"]
THANKS = ["thanks", "thank you", "thnx", "thankyou"]
HOW_ARE_YOU = ["how are you", "how r u", "how are u", "whats up", "what's up"]
NAME_QUESTIONS = ["your name", "who are you", "what are you"]
HELP_QUESTIONS = ["help", "what can you do", "commands", "options"]
TIME_QUESTIONS = ["time", "what time is it", "current time"]
DATE_QUESTIONS = ["date", "what is the date", "today's date", "todays date"]

BOT_NAME = "RuleBot"


def get_response(user_input: str) -> str:
    """
    Core decision-making function.
    Uses if-elif-else logic to match user input against
    predefined rules and return an appropriate response.
    """
    text = user_input.lower().strip()

    # Rule 1: Exit commands
    if any(word in text for word in EXIT_COMMANDS):
        return "EXIT"

    # Rule 2: Greetings
    elif any(word in text for word in GREETINGS):
        responses = [
            "Hello there! How can I help you today?",
            "Hi! Nice to see you.",
            "Hey! What can I do for you?"
        ]
        return random.choice(responses)

    # Rule 3: How are you
    elif any(phrase in text for phrase in HOW_ARE_YOU):
        return "I'm just a program, but I'm running smoothly! How about you?"

    # Rule 4: Thanks
    elif any(word in text for word in THANKS):
        return "You're welcome! Happy to help."

    # Rule 5: Name / identity questions
    elif any(phrase in text for phrase in NAME_QUESTIONS):
        return f"I'm {BOT_NAME}, a simple rule-based chatbot built with Python."

    # Rule 6: Help / capabilities
    elif any(phrase in text for phrase in HELP_QUESTIONS):
        return ("I can chat with basic greetings, tell you the time/date, "
                "respond to thanks, and say goodbye. Try saying 'hi', "
                "'time', 'date', or 'bye'.")

    # Rule 7: Time
    elif any(phrase in text for phrase in TIME_QUESTIONS):
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

    # Rule 8: Date
    elif any(phrase in text for phrase in DATE_QUESTIONS):
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."

    # Rule 9: Empty input
    elif text == "":
        return "You didn't type anything. Please say something!"

    # Default / fallback rule
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."


def run_chatbot():
    """
    Runs the chatbot in a continuous loop until the user
    types an exit command.
    """
    print("=" * 50)
    print(f" {BOT_NAME} - Rule-Based AI Chatbot ")
    print("=" * 50)
    print(f"{BOT_NAME}: Hello! Type 'help' to see what I can do, or 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)

        if response == "EXIT":
            print(f"{BOT_NAME}: Goodbye! Have a great day. 👋")
            break
        else:
            print(f"{BOT_NAME}: {response}")


if __name__ == "__main__":
    run_chatbot()
