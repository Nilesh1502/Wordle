from statusClass import status
from colorama import Fore, Back, Style

MAX_ATTEMPTS = 6
MAX_LENGTH = 5


class wordle:

    def __init__(self, answer: str):
        answer = answer.upper()
        self.answer = answer
        self.attempt_words = []
        self.words_status = []

    def attempt(self):
        attempt_left = MAX_ATTEMPTS-len(self.attempt_words)
        if attempt_left:
            if attempt_left > 1:
                print(f"\n{Fore.BLUE}You have {attempt_left} attempts remaining!{Fore.RESET}")
            else:
                print(f"\n{Fore.BLUE}You have only 1 attempt!{Fore.RESET}")
            return True
        else:
            print(f"\n{Fore.BLUE}No attempts remaining!")
            print(f"The correct word was {self.answer}{Fore.RESET}")
            return False

    def validLength(self, word: str):
        if len(word) == MAX_LENGTH:
            return True
        else:
            print(f"{Fore.RED}Word must be {MAX_LENGTH} letters long!{Fore.RESET}")
            return False

    def check(self, word: str):
        state = status(self.answer, word)
        self.words_status.append(state)
        self.attempt_words.append(word)

    def display(self):
        s="┌"+"───┬"*4+"───┐\n"
        for i in range(MAX_ATTEMPTS):
            if i < len(self.attempt_words):
                word = self.attempt_words[i]
                for j in range(len(word)):
                    if self.words_status[i].isCorrect[j]:
                        s+=f"│ {Fore.GREEN}{word[j]}{Fore.RESET} "
                    elif self.words_status[i].isPresent[j]:
                        s+=f"│ {Fore.YELLOW}{word[j]}{Fore.RESET} "
                    else:
                        s+=f"│ {Style.DIM}{word[j]}{Style.RESET_ALL} "
                s+="│\n"
            else:
                s+="│   "*5+"│\n"
            if i<MAX_ATTEMPTS-1:
                s+="├"+"───┼"*4+"───┤\n"
            else:
                s+="└"+"───┴"*4+"───┘"
        print(s)

    def validate(self):
        if self.attempt_words[-1] == self.answer:
            print(f"{Fore.GREEN}Congratulations you have guessed the correct word {self.answer}!")
            print(f"Total attempt used: {len(self.attempt_words)}{Fore.RESET}")
            return True
        return False
