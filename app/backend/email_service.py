import re 
import yagmail
import os
from dotenv import load_dotenv
load_dotenv()

address = os.getenv('GMAIL_ADDRESS')
gmail_key = os.getenv('GMAIL_KEY')

if not address:
    raise RuntimeError("GMAIL_ADDRESS not found in environment")

if not gmail_key:
    raise RuntimeError("GMAIL_KEY not found in environment")

yag = yagmail.SMTP(address, gmail_key)

def get_address(s):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    match = re.search(pattern, s)
    if match:
        return s
    else:
        raise ValueError('Invalid email address')


def send_email(recipient, subj, content):
    recipient = get_address(recipient)

    if not subj.strip():
        raise ValueError("Email subject is empty")

    if not content.strip():
        raise ValueError("Email body is empty")

    try:
        yag.send(
            to=recipient,
            subject=subj,
            contents=content
        )
    except Exception as e:
        raise RuntimeError(f"Failed to send email: {e}")