"""
Louis Fletcher
Superhero Name Generator
V2 - Saves names to txt file
"""

import tkinter as tk
from tkinter import ttk

class SuperheroNameGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Superhero Name Generator")
        self.root.geometry("400x520")
        
        # Configure colors
        self.bg_color = "white"
        self.text_color = "black"
        self.accent_purple = "#8E24AA" 
        
        self.root.configure(bg=self.bg_color)
        
        # Variables
        self.selected_adjective = tk.StringVar(value="Awesome")
        
        # UI layout
        self.create_widgets()

    def create_widgets(self):
        # Header Frame
        self.header_frame = tk.Frame(self.root, bg=self.accent_purple, height=45)
        self.header_frame.pack(fill="x", side="top")
        self.header_frame.pack_propagate(False)
        
        self.header_label = tk.Label(
            self.header_frame, 
            text="Hero name generator", 
            fg="white", 
            bg=self.accent_purple, 
            font=("Arial", 14, "bold")
        )
        self.header_label.pack(pady=8)

        # Adjective Section (Radio Buttons)
        self.lbl_adj = tk.Label(self.root, text="Choose an adjective...", font=("Arial", 11, "bold"), bg=self.bg_color, fg=self.text_color)
        self.lbl_adj.pack(pady=(20, 5))
        
        adjectives = ["Happy", "Awesome", "Outgoing", "Funky"]
        for adj in adjectives:
            rb = tk.Radiobutton(
                self.root, 
                text=adj, 
                variable=self.selected_adjective, 
                value=adj,
                bg=self.bg_color,
                fg=self.text_color,
                selectcolor=self.bg_color,
                activebackground=self.bg_color,
                activeforeground=self.text_color,
                font=("Arial", 10)
            )
            rb.pack(anchor="w", padx=110)

        # Colour Section (Entry Box)
        self.lbl_color = tk.Label(self.root, text="Enter a colour", font=("Arial", 11, "bold"), bg=self.bg_color, fg=self.text_color)
        self.lbl_color.pack(pady=(15, 5))
        
        self.entry_color = tk.Entry(self.root, width=25, font=("Arial", 11), bd=1, relief="solid")
        self.entry_color.pack(pady=5)

        # Animal Section (Combobox / Dropdown)
        self.lbl_animal = tk.Label(self.root, text="Pick an animal", font=("Arial", 11, "bold"), bg=self.bg_color, fg=self.text_color)
        self.lbl_animal.pack(pady=(15, 5))
        
        self.combo_animal = ttk.Combobox(self.root, width=23, font=("Arial", 11), state="readonly")
        self.combo_animal['values'] = ("Beaver", "Tortoise", "Gorilla", "Dog", "Bear")
        self.combo_animal.set("Beaver") 
        self.combo_animal.pack(pady=5)

        # Generate Button
        self.btn_go = tk.Button(
            self.root, 
            text="GO!", 
            command=self.generate_name, 
            font=("Arial", 11, "bold"),
            bg="white", 
            fg="black",
            bd=1, 
            relief="solid",
            padx=20
        )
        self.btn_go.pack(pady=25)

        # Output Result Label
        self.lbl_result = tk.Label(
            self.root, 
            text="", 
            font=("Arial", 12, "bold"), 
            bg=self.bg_color, 
            fg=self.accent_purple
        )
        self.lbl_result.pack(pady=10)

    def generate_name(self):
        # Gather information from inputs
        adj = self.selected_adjective.get()
        colour = self.entry_color.get().strip()
        animal = self.combo_animal.get()
        
        # Fallback capitalisation logic if user leaves color blank
        if not colour:
            colour = "Invisible"
        else:
            colour = colour.capitalize()
            
        # Update output string
        result_text = f"You are the {adjective} {colour} {animal}!"
        self.lbl_result.config(text=result_text)
        
        # Saves the result to a text file, NEW CODE
        try:
            with open("superheo_names.txt", "a") as file:
                file.write(result_text + "\n")
        except Exception as e:
            print(f"Error saving to file: {e}")

# Executing main app
if __name__ == "__main__":
    root = tk.Tk()
    app = SuperheroNameGenerator(root)
    root.mainloop()