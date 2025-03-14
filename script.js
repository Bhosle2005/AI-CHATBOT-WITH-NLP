const form = document.getElementById("chat-form");
const chatBox = document.getElementById("chat-box");

form.onsubmit = async (e) => {
    e.preventDefault(); // Prevent form reload
    const messageInput = document.getElementById("message");
    const userMessage = messageInput.value;

    // Validate input
    if (userMessage.trim() === "") {
        alert("Please enter a message!");
        return;
    }

    // Display user message
    chatBox.innerHTML += `<div class='message user-message'>${userMessage}</div>`;
    messageInput.value = "";

    try {
        // Send message to Flask server
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: `message=${encodeURIComponent(userMessage)}`,
        });

        if (response.ok) {
            const botMessage = await response.text();
            // Display bot response
            chatBox.innerHTML += `<div class='message bot-message'>${botMessage}</div>`;
        } else {
            chatBox.innerHTML += `<div class='message bot-message'>Error: Unable to connect to server.</div>`;
        }
    } catch (error) {
        chatBox.innerHTML += `<div class='message bot-message'>Error: ${error.message}</div>`;
    }
};
