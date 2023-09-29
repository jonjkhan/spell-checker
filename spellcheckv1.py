import re
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import nltk
from nltk.corpus import words

# Download NLTK words data
nltk.download("words")


class SpellingChecker:

    def __init__(self):
        # Create the main tkinter window
        self.root = tk.Tk()
        self.root.geometry("600x500")

        # Create a scrolled text widget for text input
        self.text = ScrolledText(self.root, font=("Arial", 14))
        self.text.bind("<KeyRelease>", self.check)
        self.text.pack()

        # Initialize a variable to keep track of space count
        self.old_spaces = 0

        # Start the tkinter main loop
        self.root.mainloop()

    def check(self, event):
        # Get the content of the text widget
        content = self.text.get("1.0", tk.END)

        # Count the number of spaces in the content
        space_count = content.count(" ")

        # Check if space count has changed
        if space_count != self.old_spaces:
            self.old_spaces = space_count

            # Delete existing tags
            for tag in self.text.tag_names():
                self.text.tag_delete(tag)

            # Split the content into words
            for word in content.split(" "):
                # Remove non-alphanumeric characters and convert to lowercase
                cleaned_word = re.sub(r"[^\w]", "", word.lower())

                # Check if the cleaned word is not in NLTK words
                if cleaned_word not in words.words():
                    position = content.find(word)
                    # Add a tag to highlight misspelled word in red
                    self.text.tag_add(word, f"1.{position}", f"1.{position + len(word)}")
                    self.text.tag_config(word, foreground="red")


# Create an instance of the SpellingChecker class
SpellingChecker()
