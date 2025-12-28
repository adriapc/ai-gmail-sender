import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise RuntimeError("OPENAI_API_KEY not found in environment")

client = OpenAI(api_key=API_KEY)


def generate_email(prompt_text: str, sender_name: str) -> dict:
    """
    Generates an email subject and body using OpenAI.
    Returns a dict: { "subject": str, "body": str }
    """

    try:
        body_instruction = (
            "You are an expert email copywriter. "
            "Write a clear, professional, and engaging email. "
            "Keep the response short. "
            f"The sender's name is {sender_name}. "
            "Write a greeting at the start and a closing at the end. "
            "Do NOT write the subject."
        )

        body_response = client.responses.create(
            model="gpt-4o-mini",
            instructions=body_instruction,
            temperature=0.3,
            input=prompt_text
        )

        subject_instruction = (
            "You are an expert email copywriter. "
            "Write a compelling email subject line. "
            "Keep it under 5 words. "
            "Make it clear and relevant. "
            "Avoid spammy words. "
            "Do not use emojis. "
            "Return only the subject line."
        )

        subject_response = client.responses.create(
            model="gpt-4o-mini",
            instructions=subject_instruction,
            temperature=0.3,
            input=prompt_text
        )

        return {
            "subject": subject_response.output_text.strip(),
            "body": body_response.output_text.strip()
        }

    except Exception as e:
        raise RuntimeError(f"Failed to generate email: {e}")
