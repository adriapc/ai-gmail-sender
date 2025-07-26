import re 
import sys
import yagmail
import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()


def main():
    print('-' * 27)
    print('Welcome to AI Gmail Sender!')
    print('-' * 27)
    recipient = get_address(input('Who do you want to send it to? ').strip())
    body, subject = elaborate_text(input('What do you want to send? '))
    send_email(recipient, subject, body)


def get_address(s):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    match = re.search(pattern, s)
    if match:
        return s
    else:
        sys.exit('Not a valid email address')


def elaborate_text(t):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    instruction = '''You are writing emails based on the prompt you are given. Keep the responses short. Write a greeting at the start, but not at the end, according to the formality of the email, without any name, but don't write the subject.'''  # noqa: E501
    body = client.responses.create(
        model="gpt-4o-mini",
        instructions=instruction,
        temperature=0.3,
        input=t
    )

    subject = client.responses.create(
        model="gpt-4o-mini",
        instructions="Write the subject of the email. It has to be really short. Maximum 5 words",  # noqa: E501
        temperature=0.3,
        input=t
    )

    return body.output_text, subject.output_text


def send_email(recipient, subj, content):
    yag = yagmail.SMTP(os.getenv('GMAIL_ADDRESS'), os.getenv('GMAIL_KEY'))
    try:
        yag.send(to=recipient, subject=subj, contents=content)
    except:  # noqa: E722
        sys.exit('Error occurred❌')
    print('The email has been sent correctly✅')


if __name__ == '__main__':
    main()