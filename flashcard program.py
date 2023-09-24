import random
import json
import os


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))


def readingsystem():
    with open('database.txt') as f:
        print("Reading database.txt...")
        data = f.read()

    database = json.loads(data)
    print("database.txt successfully read!")
    # print(database)
    return database


"""database = {
    "me": "saya",
    "you": "awak",
    "shop": "kedai",
    "why": "kenapa",
    "how much": "berapa",
    "we": "kami / kita",
    "they": "mereka",
    "age": "umur",
    "clever": "pandai",
    "name": "nama",
    "he/she": "dia",
    "friend": "kawan",
    "want": "mahu",
    ""
    } """

# for i in range()


def flashcardsystem(database):
    while True:
        # convert dictionary into list for index accessing
        databaselist = list(database.items())
        # print(items[0][0])
        sizeofdatabase = len(database)
        # print(sizeofdatabase)

        randomcounter = random.randint(0, sizeofdatabase-1)
        # print(randomcounter)

        question = databaselist[randomcounter][0]
        answer = databaselist[randomcounter][1]
        # print(answer)
        print("What is (", question,
              ") in malay? (type in lowercase. to skip, just press Enter. For menu, key in '0'. To terminate, ctrl+C)")
        userinput = input()

        if userinput == answer:
            prGreen("Correct!")
            print(" It is (", answer, ")")
        elif userinput == "0":
            menu()
        else:
            prRed("Wrong!")
            print(" It is (", answer, ")")


def addtoDatabase():
    print("English word: (To go back menu, enter 0)")
    userEnglishInput = input()
    if userEnglishInput == "0":
        menu()
    else:
        print("Malay Equivalent: (To go back menu, enter 0)")
        userMalayInput = input()
        if userMalayInput == "0":
            menu()
        else:
            with open('database.txt', 'a') as f:
                # f.write("\b") - backspace cmd doesn't work here
                # move cursor one byte (character) backwards
                # f.seek(-1, io.SEEK_END) this parameter combi does not work due to some reason
                f.seek(0, os.SEEK_END)  # unable to backspace due to this code
                # f.seek(f.tell() - 1, os.SEEK_SET)
                f.write(",\n")  # overwrite existing "}"
                f.write(" ")
                f.write("\"")
                f.write(userEnglishInput)
                f.write("\"")
                f.write(":")
                f.write("\"")
                f.write(userMalayInput)
                f.write("\"")
                f.write("}")
            print("Addition successful! Remember to delete the } at the end")


def menu():
    print("=========================")
    print("""-------------------------
flashcard learning system
-------------------------""")
    print("Select the following options:")
    print("1: Do the questions")
    print("2: Add to vocublary database (beta, have to manually delete the duplicate '}'s at the end of each new addition to follow JSON format)")
    print("=========================")
    userInput = input()
    match(userInput):
        case "1":
            database = readingsystem()
            flashcardsystem(database)
        case "2":
            while True:
                addtoDatabase()

        case _:
            print("error! please select the appropriate options")
            menu()


def main():

    menu()


main()
