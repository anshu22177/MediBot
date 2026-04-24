/**
 * Chatbot JavaScript
 * Handles chat interactions and UI updates
 */

document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chatForm');
    const userInput = document.getElementById('userInput');
    const chatMessages = document.getElementById('chatMessages');
    
    // Load chat history on page load
    loadChatHistory();
    
    // Auto-resize textarea
    userInput.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = Math.min(this.scrollHeight, 150) + 'px';
    });
    
    // Handle Enter key (submit) vs Shift+Enter (new line)
    userInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            chatForm.dispatchEvent(new Event('submit'));
        }
    });
    
    // Handle form submission
    chatForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const message = userInput.value.trim();
        if (!message) return;
        
        // Add user message to chat
        addMessage(message, 'user');
        
        // Clear input and reset height
        userInput.value = '';
        userInput.style.height = 'auto';
        
        // Show loading indicator
        const loadingMessage = addMessage('Thinking...', 'bot', true);
        
        try {
            // Send message to backend
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });
            
            const data = await response.json();
            
            // Remove loading message
            loadingMessage.remove();
            
            if (response.ok) {
                // Add bot response
                addMessage(data.response, 'bot');
            } else {
                // Show error
                addMessage('Sorry, there was an error processing your request. Please try again.', 'bot');
            }
        } catch (error) {
            // Remove loading message
            loadingMessage.remove();
            
            // Show error
            addMessage('Sorry, there was an error connecting to the server. Please check your connection and try again.', 'bot');
            console.error('Error:', error);
        }
    });
    
    /**
     * Add a message to the chat
     * @param {string} text - Message text
     * @param {string} type - 'user' or 'bot'
     * @param {boolean} isTemporary - If true, returns the element for removal
     */
    function addMessage(text, type, isTemporary = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}-message`;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        if (type === 'bot') {
            contentDiv.innerHTML = `<strong>Medibot:</strong> ${formatMessage(text)}`;
        } else {
            contentDiv.textContent = text;
        }
        
        messageDiv.appendChild(contentDiv);
        chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        return isTemporary ? messageDiv : null;
    }
    
    /**
     * Format bot message with line breaks and bold text
     * @param {string} text - Raw message text
     * @returns {string} - Formatted HTML
     */
    function formatMessage(text) {
        // Convert markdown-style formatting to HTML
        let formatted = text
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>') // Bold text
            .replace(/\n/g, '<br>'); // Line breaks
        
        return formatted;
    }
    
    /**
     * Load chat history from server
     */
    async function loadChatHistory() {
        try {
            const response = await fetch('/api/history');
            const history = await response.json();
            
            // Reverse to show oldest first (except welcome message)
            history.reverse();
            
            // Add history messages (skip welcome message if it exists)
            history.forEach(item => {
                addMessage(item.user_message, 'user');
                addMessage(item.bot_response, 'bot');
            });
        } catch (error) {
            console.error('Error loading chat history:', error);
        }
    }
    
    // Auto-focus input on page load
    userInput.focus();
});

