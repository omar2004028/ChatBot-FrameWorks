document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.chat-input-area');
    const input = form.querySelector('input[type="text"]');
    const messages = document.querySelector('.chat-messages');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const pregunta = input.value.trim();
        if (!pregunta) return;

        // Mostrar mensaje del usuario
        const userMsg = document.createElement('div');
        userMsg.classList.add('message', 'user');
        userMsg.textContent = `🧑 Tú: ${pregunta}`;
        messages.appendChild(userMsg);

        input.value = '';

        try {
            const response = await fetch('http://127.0.0.1:8000/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ pregunta })
            });

            const data = await response.json();

            const botMsg = document.createElement('div');
            botMsg.classList.add('message', 'bot');
            botMsg.textContent = `🤖 Bot: ${data.respuesta}`;
            messages.appendChild(botMsg);
        } catch (error) {
            const errorMsg = document.createElement('div');
            errorMsg.classList.add('message', 'error');
            errorMsg.textContent = `⚠️ Error: ${error.message}`;
            messages.appendChild(errorMsg);
        }

        messages.scrollTop = messages.scrollHeight;
    });
});
