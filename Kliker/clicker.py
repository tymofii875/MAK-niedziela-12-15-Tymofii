import tkinter as tk
from PIL import Image

root = tk.Tk()
root.title("KfCclicker")
root.geometry("400x400")

points = 0
points_per_click = 1

# Function to handle click
def click():
    global points
    points += points_per_click
    points_label.config(text=f"Punkty: {points}")

# Function to buy an upgrade
def buy_upgrade(cost, upgrade_name, increase_per_click):
    global points, points_per_click
    if points >= cost:
        points -= cost
        points_per_click += increase_per_click
        points_label.config(text=f"Punkty: {points}")
        upgrade.button.config(state="disabled")  # Disable button after purchase
        upgrade.button.config(text=f"{upgrade_name} - Kupiono!")

# Load and resize image
original_image = Image.open("button.png")
resized_image = original_image.resize((100, 100))
click_image = tk.PhotoImage(file="button.png")
resized_image = click_image.subsample(3, 3)

# Labels
points_label = tk.Label(root, text=f"Punkty: {points}", font=("Helvetica", 16))
points_label.pack(pady=10)

# Click button
click_button = tk.Button(root, image=click_image, command=click, font=("Helvetica", 16))
click_button.pack(pady=10)

# Upgrades (e.g., "Upgrade 1", "Upgrade 2")
upgrade_1_cost = 100
upgrade_2_cost = 500

upgrade_button_1 = tk.Button(root, text=f"Upgrade 1 - Koszt: {upgrade_1_cost}", font=("Helvetica", 12),
                             command=lambda: buy_upgrade(upgrade_1_cost, "Upgrade 1", 1))
upgrade_button_1.pack(pady=5)

upgrade_button_2 = tk.Button(root, text=f"Upgrade 2 - Koszt: {upgrade_2_cost}", font=("Helvetica", 12),
                             command=lambda: buy_upgrade(upgrade_2_cost, "Upgrade 2", 2))
upgrade_button_2.pack(pady=5)

root.mainloop()
