"""
Pet game v1 - Feed and exercise a pet to keep it alive
Louis Fletcher
"""

MAX_WEIGHT = 100
MIN_WEIGHT = 0

class Pet:
    def __init__(self, name=None, weight=0):
        # Typecasting inputs ensures data types are correct from the start
        self.name = str(name)
        self.weight = int(weight)
        
    def feed(self, units):
        # Only allow feeding if the pet's weight falls within healthy boundaries
        if MIN_WEIGHT < self.weight <= MAX_WEIGHT:
            self.weight += units
        
    def exercise(self, units):
        # Only allow exercise if the pet is currently alive
        if MIN_WEIGHT < self.weight <= MAX_WEIGHT:
            self.weight -= units
            # Floor constraint: prevent weight from dropping into negative numbers
            if self.weight < MIN_WEIGHT: 
                self.weight = MIN_WEIGHT
        
    def __str__(self):
        # Custom string representation to automatically format how a pet prints
        if self.weight <= MIN_WEIGHT:
            return f"{self.name} is dead from starvation or over-exercise."
        elif self.weight > MAX_WEIGHT:
            return f"{self.name} is dead from being overweight."
        else:
            return f"{self.name} weighs {self.weight} units."
        
# MAIN PROGRAM 

# Master list to track all instances of Pet objects
pet_list = []

# Data Entry Loop: Collect user input to initialize pets until 'xxx' is typed
name = input("Enter the name of the pet (xxx to end): ").title()
while name != "Xxx":
    weight = int(input("Enter the weight of the pet: "))
    
    # Instantiate a new Pet object and append it directly to our tracking list
    my_pet = Pet(name, weight)
    pet_list.append(my_pet)
    
    # Priming input check for the next iteration of the loop
    name = input("Enter the name of the pet (xxx to end): ").title()
    
# MAIN GAMEPLAY LOOP
keep_playing = True
while keep_playing: 
    # Iterate through every pet each round
    for pet in pet_list:
        # Guard Clause: Skip turn interactions if the pet is already deceased
        if pet.weight <= MIN_WEIGHT or pet.weight > MAX_WEIGHT:
            print(f"\n{pet.name} is already dead. You cannot interact with them.")
            continue  # Skips the rest of this loop iteration, moves to next pet
            
        # Display current health metrics to help player decision-making
        print(f"\n-{pet.name} currently weighs {pet.weight}/{MAX_WEIGHT} units-")
        option = input(f"Enter F to feed, E to exercise or Q to quit game for {pet.name}: ").lower()
        
        # Action Tree based on user selection
        if option == "f":
            amount = int(input(f"How many units of food for {pet.name}? "))
            pet.feed(amount)
            # Check for immediate health consequences post-feeding
            if pet.weight > MAX_WEIGHT:
                print(f"{pet.name} over-ate and died.")
            
        elif option == "e":
            amount = int(input(f"How many units of exercise for {pet.name}? "))
            pet.exercise(amount)
            # Check for immediate health consequences post-exercise
            if pet.weight <= MIN_WEIGHT:
                print(f"Oh no! {pet.name} exercised too much and starved.")
            
        elif option == "q":
            # Set flag to stop the outer loop and break the inner pet loop immediately
            keep_playing = False
            break 
            
        else:
            # Fallback error handling for incorrect string inputs
            print("Invalid option selected.")
            
    # Post-round check: If 'q' was hit inside the pet loop, exit gameplay entirely
    if not keep_playing:
        break

    # Prompt player to decide whether to advance to the next round of turns
    play = input("\nPress n to stop. Press any other key to keep playing. ").lower()
    if play == "n":
        keep_playing = False
        
# END GAME SUMMARY
print("\n Final Status of Pets ")

# Leverages the __str__ method inside the Pet class to print cleanly formatted statuses
for pet in pet_list:
    print(pet)