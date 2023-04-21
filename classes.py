import random



class sakoulaki:
    def __init__(self, letters):
        self.letters = letters

    def draw_letters(self, num_letters):
        if num_letters > len(self.letters):
            raise ValueError("Not enough letters in the bag")

        letters_drawn = random.sample(self.letters, num_letters)
        for letter in letters_drawn:
            self.letters.remove(letter)
            
        return letters_drawn

    def get_num_letters(self):
        return len(self.letters)
    
    def init_letters(self):
        letter_counts = {
            'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9,
            'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6,
            'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
        }
                
    def shuffle(self):
        random.shuffle(self.letters)


class Player:
    def __init__(self, name):
        self.name = name
        self.letters = []
        
    def get_num_letters(self):
        return len(self.letters)
    
    def show_letters(self):
        print(f"{self.name}'s letters: {' '.join(self.letters)}")
        
class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def play(self, word):
        if len(word) > len(self.letters):
            return False
        for letter in word:
            if letter not in self.letters:
                return False
        for letter in word:
            self.remove_letter(letter)
        return True

class Computer(Player):
    def __init__(self, name):
        super().__init__(name)

    def play(self, word):
        if len(word) > len(self.letters):
            return False
        for letter in word:
            if letter not in self.letters:
                return False
        for letter in word:
            self.remove_letter(letter)
        return True

