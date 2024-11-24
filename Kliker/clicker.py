import tkinter as tk
from PIL import Image

root = tk.Tk()
root.title("KfCclicker")
root.geometry("300x300")

points = 0

def click():
    global points
    points += 1
    points_label.config(text=f"Punkty: {points}")
    
original_image = Image.open("button.png")
resized_image = original_image.resize((100, 100))   
click_image =tk.PhotoImage(file= "button.png")
resized_image = click_image.subsample(3, 3)    

points_label= tk.Label(root, text = "Punkty: 0", font = ("Helvetica", 16))
points_label.pack(pady = 10)

click_button = tk.Button(root, image = click_image, command = click,font = ("Helvetica", 16))
click_button.pack(pady= 10)

root.mainloop()