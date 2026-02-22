
import re


class WordSearcher:
    """Class to search for a word in a text string and count its frequency"""

    def __init__(self):
        self.text = input("Enter a text string: ")
        self.search_text = input("Enter the text you want to search for: ")

    def find_word(self):
        """Search for a word in the string and display a message if found"""
        result = re.search(self.search_text, self.text)

        if result is None:
            return f"We did not find the word: {self.search_text}"

        print(f"We found the word: {self.search_text}")

    def count_word(self):
        """Count how many times the word appears in the string"""
        frequency = len(re.findall(self.search_text, self.text))
        print(f"Times the word '{self.search_text}' appears: {frequency}")


if __name__ == "__main__":
    searcher = WordSearcher()
    searcher.find_word()
    searcher.count_word()
