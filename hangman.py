anims = (    " ┏━━━━━━┓\n ┃\n ┃\n ┃\n ┃\n━┻━",
    " ┏━━━━━━┓\n ┃      ☺\n ┃\n ┃\n ┃\n━┻━",
    " ┏━━━━━━┓\n ┃      ☺\n ┃      │\n ┃\n ┃\n━┻━",
    " ┏━━━━━━┓\n ┃      ☺\n ┃      │\n ┃      │\n ┃\n━┻━",
    " ┏━━━━━━┓\n ┃      ☺\n ┃     ╱│\n ┃      │\n ┃\n━┻━",
    " ┏━━━━━━┓\n ┃      ☺\n ┃     ╱│╲\n ┃      │\n ┃\n━┻━",
    " ┏━━━━━━┓\n ┃      ☺\n ┃     ╱│╲\n ┃      │\n ┃     ╱\n━┻━",
    " ┏━━━━━━┓\n ┃      ☺\n ┃     ╱│╲\n ┃      │\n ┃     ╱ ╲\n━┻━")

def customInput():
    newInput = ""

    while len(newInput) != 1:
        newInput = input("input letter: ")

    return newInput

def game():
    word = input("input word: ")
    current = list("_"*len(word))
    wrong = 0
    foundWords = ""

    while word != "".join(current) and wrong != len(anims)-1:
        print(anims[wrong])
        print("".join(current))
        res = customInput()
        
        if res in foundWords:
            print("Word already found")
            continue

        if res in word:
            foundWords += res
            
            for i,v in enumerate(word):
                if v == res:
                    current[i] = res
        else:
            wrong += 1

    if word == "".join(current):
        print(f"{anims[wrong]}\n{"".join(current)}\nYou won")
    
    if wrong == len(anims)-1:
        print(f"{anims[len(anims)-1]}\nYou lost\nWord: {word}")
        
game()
