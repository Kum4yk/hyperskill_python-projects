import random


class Hangman:
    __possible_words = {'python', 'java', 'kotlin', 'javascript'}
    __attempts = 8

    def __init__(self):
        self.guessed_word = random.choice(tuple(self.__possible_words)).lower()
        self.current_result = list("-" * len(self.guessed_word))
        self.guessed_letters = set(list(self.guessed_word))
        self.words_number = len(self.guessed_letters)
        self.input_words = set()

    def __print_current_result(self):
        print(*self.current_result, sep='')

    def check_result(self):
        if not self.words_number:
            self.__print_current_result()
            print("You guessed the word!\nYou survived!\n")
            return True

    def __char_input(self):
        while True:
            self.__print_current_result()
            char = input("Input a letter: ")
            if len(char) != 1:
                print("You should print a single letter\n")
                continue
            if not char.islower():
                print('It is not an ASCII lowercase letter\n')
                continue
            if char in self.input_words:
                print('You already typed this letter\n')
                continue
            self.input_words.add(char)
            return char

    @staticmethod
    def start():
        while True:
            some = input('Type "play" to play the game, "exit" to quit: ')
            print()
            if some == 'play':
                Hangman().game()
            elif some == 'exit':
                break

    def game(self):
        count = 0
        while count != Hangman.__attempts:
            if self.check_result():
                break
            char = self.__char_input()

            if char in self.guessed_letters:
                for i in range(len(self.guessed_word)):
                    if self.guessed_word[i] == char:
                        self.current_result[i] = char
                self.words_number -= 1
            else:
                print("No such letter in the word")
                count += 1

            if count == Hangman.__attempts and self.words_number != 0:
                print("You are hanged!")
                break
            print()


if __name__ == '__main__':
    # print("H A N G M A N")
    Hangman.start()
