# python_ai_agent

An AI agent built with Python and Google's Gemini AI.

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/JohnLouiene/python_ai_agent
cd ./file_path
```

### 2. Create a Virtual Environment *(optional but recommended)*
```bash
# Using uv
uv venv

# Or using standard Python
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

The agent requires a Gemini API key to function. See `.env.example` for reference.

1. Create a `.env` file in the root directory.
2. Add your API key:
```env
GEMINI_API_KEY=your_actual_key_here
```

---

## Usage

### Run the Agent
```bash
# Standard
python3 main.py "Your prompt here"

# With a virtual environment (uv)
uv run main.py "Your prompt here"
```

### Verbose Flag *(optional)*

Shows token usage and message loop contents.
```bash
python3 main.py --verbose "Your prompt here"
```

---

## Project Structure

| Folder | Description |
|---|---|
| `calculator/` | A sample project directory — replace with your actual files |
| `functions/` | Tools available to the model: read, write, and run files |