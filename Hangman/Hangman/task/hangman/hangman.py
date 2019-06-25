import random


class Hangman:
    __possible_words = {'python', 'java', 'kotlin', 'javascript'}
    __attempts = 8

    def __init__(self):
        self.guessed_word = random.choice(tuple(self.__possible_words)).lower()
        self.current_result = list("-" * len(self.guessed_word))
        self.guessed_letters = dict.fromkeys(self.guessed_word, True)
        self.words_number = len(self.guessed_letters)

    def test2(self):
        count = 0
        while count < Hangman.__attempts:
            print(*self.current_result, sep='')
            char = input("Input a letter: ").lower()

            if self.guessed_letters.get(char) is not None:
                if self.guessed_letters[char]:
                    for i in range(len(self.guessed_word)):
                        if self.guessed_word[i] == char:
                            self.current_result[i] = char
                    self.guessed_letters[char] = False
                    self.words_number -= 1
                else:
                    print("No improvements")
                    count += 1
            else:
                print("No such letter in the word")
                count += 1
            print()
            if self.words_number == 0:
                print("You guessed the word!\nYou survived!")
                break
        if count == Hangman.__attempts and self.words_number != 0:
            print("You are hanged!")
        """
        print("Thanks for playing!\n"
              "We'll see how well you did in the next stage")
        """


if __name__ == '__main__':
    # print()
    game = Hangman()
    game.test2()
