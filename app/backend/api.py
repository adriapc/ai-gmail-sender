from backend.email_service import send_email
from backend.openai_client import generate_email

class Api:
    def generate_email(self, data):
        try:
            result = generate_email(
                prompt_text=data['prompt'],
                sender_name=data['sender'])
            
            return {
                'status': 'ok',
                'subject': result['subject'],
                'body': result['body']
            }
        
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    

    def send_email(self, data):
        try:
            send_email(
                recipient=data["recipient"],
                subject=data["subject"],
                content=data["body"]
            )

            return {"status": "ok", "message": "Email sent successfully"}
        
        except Exception as e:
            return {"status": "error", "message": str(e)}