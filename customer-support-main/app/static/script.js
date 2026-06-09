document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle');
    if (themeToggleBtn) {
        const savedTheme = localStorage.getItem('theme') || 'dark';
        document.documentElement.setAttribute('data-theme', savedTheme);

        themeToggleBtn.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        });
    }

    if (!themeToggleBtn) {
        const savedTheme = localStorage.getItem('theme') || 'dark';
        document.documentElement.setAttribute('data-theme', savedTheme);
    }

    const ticketForm = document.getElementById('ticket-form');
    if (ticketForm) {
        ticketForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const submitBtn = document.getElementById('submit-btn');
            const textInput = document.getElementById('ticket-text').value;
            
            if (!textInput.trim()) return;

            submitBtn.textContent = 'Analyzing...';
            submitBtn.disabled = true;

            try {
                const response = await fetch('/api/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ text: textInput })
                });

                const data = await response.json();

                if (data.success) {
                    document.getElementById('results-container').style.display = 'block';
                    
                    document.getElementById('res-category').textContent = data.category;
                    document.getElementById('res-sentiment').textContent = data.sentiment;
                    
                    const sentimentBadge = document.getElementById('res-sentiment');
                    if (data.sentiment === 'Positive') sentimentBadge.style.color = 'var(--success-text)';
                    else if (data.sentiment === 'Negative') sentimentBadge.style.color = 'var(--danger-color)';
                    else sentimentBadge.style.color = 'var(--text-primary)';

                    document.getElementById('res-summary').textContent = data.summary;
                    
                    const replyBox = document.getElementById('res-reply');
                    if (data.auto_reply) {
                        replyBox.textContent = data.auto_reply;
                    } else {
                        replyBox.textContent = "No auto-reply confidently matched. Requires human agent.";
                        replyBox.style.color = "var(--text-secondary)";
                    }
                }
            } catch (error) {
                console.error("Error submitting ticket:", error);
                alert("Failed to analyze ticket.");
            } finally {
                submitBtn.textContent = 'Analyze Ticket';
                submitBtn.disabled = false;
            }
        });
    }
});
