import random
import webbrowser
import os
import sys

class hangman:
    
    def __init__(self):
        self.secretWord = self.getRandomWord()
        self.life = 6
        self.showWord = self.createShowWord()
    
    def getRandomWord(self):
        f = open(os.path.join(sys.path[0], "words_alpha.txt"), "r")
        wordlist = f.readlines()
        f.close()
        word = wordlist[random.randrange(0,len(wordlist))]
        word = word[:-1]
        return word

    def showWordSate(self):
        print(self.showWord)

    def createShowWord(self):
        word = ""
        for i in self.secretWord:
            word += "_ "
        return word[:-1]
    
    def run(self):
        win = False
        while not win and self.life > 0:
            print(self.life)
            self.showWordSate()
            guessed = input("guess a letter: ")
            if guessed in self.secretWord:
                for i in range(len(self.secretWord)):
                    if self.secretWord[i] == guessed:
                        letterList = list(self.showWord)
                        letterList[i*2] = guessed
                        self.showWord = "".join(letterList)
                if "_" not in self.showWord.split(" "):
                    win = True
                    self.showWordSate()
                    print("YOU WON!!")
            else:
                print("wrong letter")
                self.life -= 1
        if self.life == 0:
            print("YOU LOST: " + self.secretWord)
        if input("google it? y/n: ") == "y":
            webbrowser.open_new_tab("https://www.google.com.tr/search?q="+self.secretWord)

if __name__ == "__main__":
    hangmanGame = hangman()
    hangmanGame.run()