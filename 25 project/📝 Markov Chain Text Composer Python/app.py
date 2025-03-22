import numpy as np
import random

class MarkovChain:
    def __init__(self):
        self.word_dict = {}

    def train(self, text):
        words = text.split()
        for i in range(len(words) - 1):
            word, next_word = words[i], words[i + 1]
            if word not in self.word_dict:
                self.word_dict[word] = []
            self.word_dict[word].append(next_word)

    def generate_text(self, length=20, start_word=None):
        if not self.word_dict:
            return "No data to generate text."
        
        if start_word is None or start_word not in self.word_dict:
            start_word = random.choice(list(self.word_dict.keys()))

        current_word = start_word
        result = [current_word]

        for _ in range(length - 1):
            next_words = self.word_dict.get(current_word, [])
            if not next_words:
                break
            current_word = random.choice(next_words)
            result.append(current_word)

        return " ".join(result)

# Sample Training Data (Song Lyrics)
text_data = """
Shine bright like a diamond
Find light in the beautiful sea
I choose to be happy
You and I, you and I
We're like diamonds in the sky
"""

# Create Markov Chain Model
markov = MarkovChain()
markov.train(text_data)

# Generate New Lyrics
generated_text = markov.generate_text(length=15, start_word="Shine")
print("Generated Lyrics:\n", generated_text)
