function toggleLoginModal() {
    const modal = document.getElementById('loginModal');
    modal.style.display = modal.style.display === 'block' ? 'none' : 'block';
}

window.onclick = function(event) {
    const modal = document.getElementById('loginModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
}
