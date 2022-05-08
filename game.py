from wordleClass import wordle
from colorama import Fore, Back, Style
import random


def main():
    print("Hello Wordle!")
    words = set()
    with open("data/sgb-words.txt", "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            words.add(word)

    answer = random.choice(list(words))
    wordle_obj = wordle(answer)

    wordle_obj.display()

    while wordle_obj.attempt():
        word = input("Enter your guess >> ")
        word = word.upper()
        if not wordle_obj.validLength(word):
            wordle_obj.display()
            continue

        if not word in words:
            print(f"{Fore.RED}{word} is not a valid word!{Fore.RESET}")
            wordle_obj.display()
            continue

        wordle_obj.check(word)
        wordle_obj.display()

        if wordle_obj.validate():
            break


if __name__ == '__main__':
    main()
