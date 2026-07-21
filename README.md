# Project 1: Rule-Based AI Chatbot 🤖

## Goal
Create a simple rule-based chatbot that responds to predefined user inputs.

## Key Requirements
- ✅ Handle greetings and exit commands
- ✅ Use if-else logic for responses
- ✅ Run in a continuous loop

## Key Skills Demonstrated
- Control flow
- Decision-making logic
- Basic AI concepts (pattern/rule matching)

## Files
- `chatbot.py` — Main chatbot program

## How to Run
1. Make sure Python 3 is installed on your system.
2. Open a terminal in this project folder.
3. Run the following command:
   ```
   python3 chatbot.py
   ```
4. Start chatting! Type things like:
   - `hi` / `hello` — greeting
   - `how are you`
   - `your name` — bot introduces itself
   - `time` — current time
   - `date` — today's date
   - `thanks`
   - `help` — list of things the bot can respond to
   - `bye` / `exit` / `quit` — ends the chat

## How It Works
The chatbot uses a function called `get_response()` which takes the user's
message, converts it to lowercase, and checks it against several predefined
keyword lists using `if / elif / else` statements. Based on which keywords
match, it returns an appropriate response. If nothing matches, a default
fallback message is shown.

The `run_chatbot()` function contains a `while True:` loop that keeps asking
the user for input until an exit command (`bye`, `exit`, `quit`, etc.) is
typed, at which point the loop breaks and the program ends.

## Possible Extensions (Optional Ideas)
- Add more keyword rules (jokes, weather, FAQs)
- Store conversation history in a file
- Add a simple GUI using `tkinter`
- Convert it into a web chatbot using Flask