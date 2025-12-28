# AI GMAIL SENDER

## Description:
A desktop application that generates and sends professional emails using AI. Built with Python, PyWebView, and OpenAI API, with Gmail SMTP for sending emails.

## Features
- Generate email subject and body using AI based on your prompt.
- Input validation: email, sender name, and prompt required.
- Sends emails directly through Gmail securely.
- Polished UI with desktop experience.

## Preview

![User's interface of desktop app](./assets/app_ui.png)

***

## Folder Structure
```
ai-email-sender/
├─ app/
│  ├─ frontend/
│  │  ├─ index.html
│  │  ├─ styles.css
│  │  └─ app.js
│  ├─ backend/
│  │  ├─ api.py
│  │  ├─ email_service.py
│  │  └─ openai_client.py
│  └─ main.py
├─ assets/
├─ .env
└─ requirements.txt
```

## Requirements
- Python 3.10+
- Gmail account with App Password (for SMTP)
- OpenAI API key


## Installation

1. Clone the repository:
```bash
git clone https://github.com/adriapc/ai-gmail-sender.git
cd ai-gmail-sender
```

2. Create a virtual environment
```bash
python -m venv .venv
```

3. Activate the virtual environment
- Windows:
```bash
.venv/Scripts/activate
```
- MacOS/Linux:
```bash
source .venv/bin/activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Create a ```.env``` file in the root folder
```.env
OPENAI_API_KEY=your OpenAI key
GMAIL_KEY=your Google App key
GMAIL_ADDRESS=example@gmail.com
```


## Usage
Type the following command in your terminal window:
```
python main.py
```
- The app window will open
- Fill in all fields
- Click **Generate Email** -> output appears
- You can click **Generate Email** again to regenerate the output
- Click **Send Email** to send it

