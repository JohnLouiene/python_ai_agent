# python_ai_agent
- An A.I. agent made using the python language and Google's Gemini A.I

# Installation and Setup
- Clone the Repository

# git clone https://github.com/JohnLouiene/python_ai_agent
- open a terminal
- cd ./file_path

# Create a Virtual Environment (Doing this is optional but is good practice to do so)
- uv venv

# python3 -m venv venv
- source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install Dependencies
- pip install -r requirements.txt

# Environment Variables
- The agent requires an API key from google to function.
- See .env.example
- Create a .env file in the root directory.
- Add your Gemini API key:
- GEMINI_API_KEY=your_actual_key_here


# Run the Agent
- python3 main.py "Your prompt here"
# Run the Agent (If you have a virtual environment)
- uv run main.py "Your prompt here"

# Verbose flag (Optional to see how many tokens is used or to see what the message loop's contents are)
- (run the agent) main.py --verbose "Your prompt here"