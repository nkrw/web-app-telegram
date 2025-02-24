from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp
import os
from utils.num_list_manager import get_numbers_from_file  # Tu peux avoir une fonction pour générer des numéros

@dp.callback_query_handler(lambda c: c.data.startswith("buy_num_list_"))
async def process_num_list_purchase(call: types.CallbackQuery):
    """Gère l'achat de numéros de la catégorie 'Num List'"""
    quantity = int(call.data.split("_")[-1])  # Extraire la quantité demandée (par exemple: 1000)

    # Logique de vérification du solde de l'utilisateur
    user_balance = 1000  # Exemple, ici tu dois récupérer le solde réel de l'utilisateur
    price_per_unit = 7.00  # Exemple de prix par unité, adapte selon ta logique
    total_price = price_per_unit * quantity

    if user_balance < total_price:
        await call.message.answer("❌ Vous n'avez pas assez de fonds pour cet achat.")
        return

    # Récupérer les numéros demandés depuis la fonction qui génère les numéros
    numbers = get_numbers_from_file(quantity)

    if numbers is None:
        await call.message.answer("❌ Pas assez de numéros disponibles.")
        return

    # Créer le fichier contenant les numéros
    file_path = f"data/num_list_{quantity}.txt"
    with open(file_path, "w") as file:
        file.writelines(numbers)

    # Envoyer le fichier à l'utilisateur
    await call.message.answer_document(open(file_path, "rb"))

    # Supprimer le fichier temporaire après envoi
    os.remove(file_path)

    await call.message.answer("✅ Votre fichier avec les numéros a été envoyé avec succès. Merci pour votre achat !")
    await call.answer()
