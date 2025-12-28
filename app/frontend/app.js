document.addEventListener("DOMContentLoaded", () => {

  const generateBtn = document.getElementById('generateBtn');
  const regenerateBtn = document.getElementById('regenerateBtn');
  const sendBtn = document.getElementById('sendBtn');

  async function generateEmail() {
    const recipientEmail = document.getElementById('recipientEmail').value;
    const senderName = document.getElementById('senderName').value;
    const promptText = document.getElementById('promptText').value;

    if (window.pywebview) {
      const result = await window.pywebview.api.generate_email({
        recipient: recipientEmail,
        sender: senderName,
        prompt: promptText
      });

      document.getElementById('generatedSubject').value = result.subject;
      document.getElementById('generatedBody').value = result.body;
    } else {
      document.getElementById('generatedSubject').value = "Example Subject";
      document.getElementById('generatedBody').value = "This is a sample email body.";
    }
  }

  async function sendEmail() {
    const recipient = document.getElementById('recipientEmail').value;
    const subject = document.getElementById('generatedSubject').value;
    const body = document.getElementById('generatedBody').value;

    if (!subject || !body) {
      alert("Please generate the email first.");
      return;
    }

    if (window.pywebview) {
      const response = await window.pywebview.api.send_email({
        recipient,
        subject,
        body
      });
      alert(response.message || response);
    } else {
      alert("Email sent (dummy).");
    }
  }

  generateBtn.addEventListener('click', generateEmail);
  regenerateBtn.addEventListener('click', generateEmail);
  sendBtn.addEventListener('click', sendEmail);

});
