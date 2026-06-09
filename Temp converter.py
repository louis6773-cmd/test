"""
Temperature converter 
9/6/2026
"""
# Style constants
FONT_MAIN_TITLE = "Verdana 16 bold"
FONT_HEADING = "Verdana 12 bold"
FONT_DEFAULT = "Verdana 12"

class TemperatureConverter:
    # Class constants for absolute zero validation
    ABS_ZERO_CELSIUS = -273.15
    ABS_ZERO_FAHRENHEIT = -459.67

    def is_valid_float(text):
        text = text.strip()
        if not text:
            return False
            
        # Strip a single leading negative sign if present
        if text.startswith('-'):
            text = text[1:]
            
        # Count decimal points and ensure all remaining characters are digits
        if text.count('.') <= 1 and text.replace('.', '', 1).isdigit():
            return True
        return False

    def fahrenheit_to_celsius(temp_str):
        # Converts Fahrenheit to Celsius with validation.
        # Check if the input is a valid float number string
        if not TemperatureConverter.is_valid_float(temp_str):
            return "Please enter a number"

        fahrenheit = float(temp_str)

        # Check against absolute zero
        if fahrenheit < TemperatureConverter.ABS_ZERO_FAHRENHEIT:
            return "Temperature too low"

        # Perform conversion and return formatted string
        celsius = (fahrenheit - 32) * 5 / 9
        return f"{round(celsius, 1)} degrees Centigrade"

    def celsius_to_fahrenheit(temp_str):
        # Converts Celsius to Fahrenheit with validation.
        # Check if the input is a valid float number string
        if not TemperatureConverter.is_valid_float(temp_str):
            return "Please enter a number"

        celsius = float(temp_str)

        # Check against absolute zero
        if celsius < TemperatureConverter.ABS_ZERO_CELSIUS:
            return "Temperature too low"

        # Perform conversion and return formatted string
        fahrenheit = (celsius * 9 / 5) + 32
        return f"{round(fahrenheit, 1)} degrees Fahrenheit"
    
class ConverterGUI:
    # Sets up the GUI
    
    def __init__(self, root):
        self.converter = TemperatureConverter()
        # Main window
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("400x150")
        
        # Container for frames
        self.container = Frame(self.root)
        self.container.grid(row=0, column =0, sticky="nsew")
        
        # Dictionary to hold frames
        # Key is the frame name and value is the method that creates the frame
        self.frames = {}
        
        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["cMainFrame"] = self.create_to_c_frame()
        self.frames["fMainFrame"] = self.create_to_f_frame()
        
        # Show the initial frame
        self.show_frame("MainFrame")
        
    def show_frame(self, name):
        # Displays the required frame from the dictionary 
        frame = self.frames[name] # Square brackets here
        frame.tkraise() # Move the frame to the top of the stack

        


