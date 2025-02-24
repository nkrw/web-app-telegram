import os

def handle_number_purchase(quantity: int) -> str:
    file_path = 'num_list.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()

    selected_numbers = lines[:quantity]
    remaining_numbers = lines[quantity:]

    with open(file_path, 'w') as file:
        file.writelines(remaining_numbers)

    purchase_file_path = f'purchase_{quantity}.txt'
    with open(purchase_file_path, 'w') as file:
        file.writelines(selected_numbers)

    return purchase_file_path