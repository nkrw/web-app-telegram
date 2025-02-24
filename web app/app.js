// Récupérer les informations du client via des paramètres URL
function getUserData() {
    const urlParams = new URLSearchParams(window.location.search);
    const username = urlParams.get('username') || 'Invité';
    const userId = urlParams.get('user_id') || 'Non spécifié';

    document.getElementById('welcomeMessage').innerHTML = `Bonjour ${username}!<br>Votre ID: ${userId}`;
}

// Fonction pour rediriger vers la boutique
function redirectToStore() {
    window.location.href = '/boutique';  // Ici, tu peux mettre le lien vers ta page de boutique.
}

// Appeler la fonction pour afficher les infos du client
window.onload = getUserData;
