document.addEventListener("DOMContentLoaded", function () {
  const sidebar = document.getElementById("sidebar");
  const toggleButton = document.getElementById("toggleSidebar");

  toggleButton.addEventListener("click", function () {
    sidebar.classList.toggle("expanded");
  });
});

function getCurrentTime() {
  const now = new Date();
  const hours = now.getHours().toString().padStart(2, '0');
  const minutes = now.getMinutes().toString().padStart(2, '0');
  return `${hours}:${minutes}`;
}


document.getElementById('message-form').addEventListener('submit', function(e) {
  e.preventDefault(); // Отменяем стандартную отправку формы
  
  const messageInput = document.getElementById('message-input');
  const message = messageInput.value.trim();
  
  if (message) {
      console.log('Отправлено сообщение:', message);
      messageInput.value = '';
      
      const messageContainer = document.createElement('div');
      messageContainer.className = 'd-flex flex-column align-items-end mb-2';

      const messageCard = document.createElement('div');
      messageCard.className = 'card d-inline-block p-2 bg-primary text-white';
      messageCard.innerText = message;

      messageContainer.appendChild(messageCard);

      const messageTime = document.createElement('div');
      messageTime.className = 'text-muted small';
      messageTime.innerText = getCurrentTime();

      messageContainer.appendChild(messageTime);

      const chatContainer = document.getElementById('chat-container');

      console.log(chatContainer.children)
      chatContainer.prepend(messageContainer); 
      console.log('Добавлено сообщение:', message);
  }
});