import random


class Hangman:
    possible_words = ('python', 'java', 'kotlin', 'javascript')

    def test(self):
        guessed_word = random.choice(self.possible_words)
        some = "-" * len(guessed_word)
        some = guessed_word[:3] + some[3:]
        if guessed_word ==\
                input("Guess the word {}: ".format(some)).casefold():
            print("You survived!")
        else:
            print("You are hanged!")


if __name__ == '__main__':
    print("H A N G M A N")
    Hangman().test()
