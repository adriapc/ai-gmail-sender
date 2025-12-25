import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

def generate_email(t, name):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    body_instruction = f'''You are an expert email copywriter. Write a clear, professional, and engaging email. Keep the responses short. 
                        The senders name is {name}. Write greetings at the start and at the end. Don't write the subject.
                        ''' 
    body = client.responses.create(
        model="gpt-4o-mini",
        instructions=body_instruction,
        temperature=0.3,
        input=t
    )

    subject_instruction = f'''You are an expert email copywriter.
                        Write a compelling email subject line based on the following information:
                        - Keep it under 5 words
                        - Make it clear and relevant
                        - Avoid spammy words (free, urgent, guarantee, etc.)
                        - Do not use emojis unless explicitly requested
                        - Return only the subject line
                        '''
    subject = client.responses.create(
        model="gpt-4o-mini",
        instructions=subject_instruction,  
        temperature=0.3,
        input=t
    )

    return body.output_text, subject.output_text

text = "Meeting tomorrow at 10am at my office to discuss business growth."
name = "Adrià"

body, subj = generate_email(text, name)
print(subj, "\n", body)