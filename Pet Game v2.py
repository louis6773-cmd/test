"""
Louis Fletcher
Pet Game v2
"""


from tkinter import *
from tkinter import messagebox
 
OVERWEIGHT = 200
MIN_UNITS = 1
MAX_UNITS = 200
 
 
class Pet:
   def __init__(self, name=None, weight=0):
       self.name = name.title()
       self.weight = weight
 
   def feed(self, units):
       if self.weight > 0:
           self.weight += units
       return self.weight
 
   def exercise(self, units):
       if self.weight > 0:
           self.weight -= units
       return self.weight
 
   def __str__(self):
       if self.weight <= 0:
           return f"RIP {self.name}"
       elif self.weight > OVERWEIGHT:
           return f"{self.name} :-("
       else:
           return f"{self.name} now weighs {self.weight}"
 
 
class PetGUI:
   def __init__(self, root):
       self.root = root
       self.root.title("Virtual Pet")
      
       self.pet = None
      
       # Pet Name
       Label(self.root, text="Pet Name").grid(row=0, column=0)
       self.name_entry = Entry(self.root)
       self.name_entry.grid(row=0, column=1)
      
       # Starting Weight
       Label(self.root, text="Starting Weight").grid(row=1, column=0)
       self.weight_entry = Entry(self.root)
       self.weight_entry.grid(row=1, column=1)
      
       # Create Pet Button
       self.create_btn = Button(self.root, text="Create Pet", command=self.create_pet)
       self.create_btn.grid(row=2, column=0, columnspan=2)
      
       # Units
       Label(self.root, text="Units").grid(row=3, column=0)
       self.units_entry = Entry(self.root)
       self.units_entry.grid(row=3, column=1)
      
       # Feed and Exercise Buttons
       self.feed_btn = Button(self.root, text="Feed", command=self.feed_pet)
       self.feed_btn.grid(row=4, column=0)
      
       self.exercise_btn = Button(self.root, text="Exercise", command=self.exercise_pet)
       self.exercise_btn.grid(row=4, column=1)
      
       # Status Label
       self.status_label = Label(self.root, text="Create a pet to begin.")
       self.status_label.grid(row=5, column=0, columnspan=2)
  
   def create_pet(self):
      # name check
      name = self.name_entry.get()
      if name == "":
          messagebox.showerror("Error", "Please enter a valid name.")
          return
           
      # Weght check
      try:
         weight = float(self.weight_entry.get())
         if weight <=0:
            messagebox.showerror("Error", "Weight must be positive.")
            return
      except ValueError:
         messagebox.showerror("Error", "Please enter a valid number for weight.")
         return
            
      # Connection
      self.pet = Pet(name, weight)
      self.status_label.config(text=str(self.pet))
      
   def get_units(self):
         
      
           
      

           
  
 