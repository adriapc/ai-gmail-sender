document.addEventListener("DOMContentLoaded", () => {

  const recipientInput = document.getElementById('recipientEmail');
  const senderInput = document.getElementById('senderName');
  const promptInput = document.getElementById('promptText');

  const generateBtn = document.getElementById('generateBtn');
  const sendBtn = document.getElementById('sendBtn');

  const outputArea = document.querySelector('.output');
  const generatedSubject = document.getElementById('generatedSubject');
  const generatedBody = document.getElementById('generatedBody');

  // Validation 
  function validateForm() {
    const recipient = recipientInput.value.trim();
    const sender = senderInput.value.trim();
    const prompt = promptInput.value.trim();

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const emailValid = emailPattern.test(recipient);

    return recipient && sender && prompt && emailValid;
  }

  function updateUI() {
    const valid = validateForm();

    generateBtn.disabled = !valid;

    // Only show output & send button if email has been generated
    if (valid && generatedSubject.value) {
      outputArea.classList.remove('hidden');
      sendBtn.classList.remove('hidden');
    } else {
      outputArea.classList.add('hidden');
      sendBtn.classList.add('hidden');
    }
  }

  async function generateEmail() {
    if (!validateForm()) return;

    generateBtn.disabled = true;
    generateBtn.textContent = "Generating...";

    const recipientEmail = recipientInput.value.trim();
    const senderName = senderInput.value.trim();
    const promptText = promptInput.value.trim();

    try {
      let result;
      if (window.pywebview) {
        result = await window.pywebview.api.generate_email({
          recipient: recipientEmail,
          sender: senderName,
          prompt: promptText
        });
      } else {
        result = {
          status: 'ok',
          subject: "Example Subject",
          body: "This is a sample email body."
        };
      }

      if (result.status === 'ok' || !result.status) {
        generatedSubject.value = result.subject;
        generatedBody.value = result.body;
        outputArea.classList.remove('hidden');
        sendBtn.classList.remove('hidden');
      } else {
        alert("Error: " + result.message);
      }
    } catch (err) {
      alert("Unexpected error: " + err);
    }

    generateBtn.textContent = "Generate Email";
    generateBtn.disabled = false;
  }

  async function sendEmail() {
    const recipient = recipientInput.value.trim();
    const subject = generatedSubject.value.trim();
    const body = generatedBody.value.trim();

    if (!subject || !body) {
      alert("Please generate the email first.");
      return;
    }

    sendBtn.disabled = true;
    sendBtn.textContent = "Sending...";

    try {
      let response;
      if (window.pywebview) {
        response = await window.pywebview.api.send_email({
          recipient,
          subject,
          body
        });
      } else {
        response = { status: 'ok', message: "Email sent (dummy)." };
      }

      alert(response.message || response);
    } catch (err) {
      alert("Unexpected error: " + err);
    }

    sendBtn.textContent = "Send Email";
    sendBtn.disabled = false;
  }

  [recipientInput, senderInput, promptInput].forEach(input => {
    input.addEventListener('input', updateUI);
  });

  generateBtn.addEventListener('click', generateEmail);
  sendBtn.addEventListener('click', sendEmail);

  // Initial state 
  generateBtn.disabled = true;
  sendBtn.classList.add('hidden');
  outputArea.classList.add('hidden');

});