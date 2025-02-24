import os

NUM_LIST_FILE = "data/num_list.txt"

def get_numbers_from_file(quantity):
    """Récupère une quantité spécifique de numéros et les supprime après extraction"""
    try:
        with open(NUM_LIST_FILE, "r") as file:
            lines = file.readlines()

        if len(lines) < quantity:
            return None  # Pas assez de numéros disponibles

        selected_numbers = lines[:quantity]
        remaining_numbers = lines[quantity:]

        with open(NUM_LIST_FILE, "w") as file:
            file.writelines(remaining_numbers)

        return selected_numbers
    except Exception as e:
        print(f"Erreur lors de la lecture/écriture du fichier : {e}")
        return None
