import re, random
from colorama import Fore, init

# Initialize colorama (autoreset ensures each print reset after use)
init(autoreset=True)

# Destiation & joke data
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountaions", "Himalayas"],
    "cities": ["Tokyo", "Paris","New York"]
}
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# Helper function to normalize user input (remove extra spaces, make lowercase)
def normalize_input(text):
    return re.sub(r"\s+"," ", text.strip().lower())

# Provide travel recommendations (recurive if user rejects suggestions)
def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountaions, or cities?")
    preference=input(Fore.YELLOW+"You: ")