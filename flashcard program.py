import random
import json
import os


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))


def readingsystem1():
    with open('databaseWk1-7.txt') as f:
        print("Reading databaseWk1-7.txt...")
        data = f.read()

    database = json.loads(data)
    print("database.txt successfully read!")
    # print(database)
    return database


def readingsystem2():
    with open('databaseWk8-13.txt') as f:
        print("Reading databaseWk8-13.txt...")
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


def addtoDatabase1():
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
            with open('databaseWk1-7.txt') as f:
                data = f.read()                # string
            dataDict = json.loads(data)    # from string to dictionary
            dataDict.update({userEnglishInput: userMalayInput})
            # from dictionary to JSON
            dataJSON = json.dumps(dataDict, indent=2)
            dataString = str(dataJSON)  # from JSON to string
            with open('databaseWk1-7.txt', "w") as f:
                f.write(dataString)
            f.close()
            prGreen("Addition successful!")
            # print("Remember to delete the } at the end")


def addtoDatabase2():
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
            with open('databaseWk8-13.txt') as f:
                data = f.read()                # exact string
            dataDict = json.loads(data)    # from string to dictionary
            dataDict.update({userEnglishInput: userMalayInput})
            # from dictionary to JSON
            dataJSON = json.dumps(dataDict, indent=2)
            dataString = str(dataJSON)  # from JSON to string
            with open('databaseWk8-13.txt', "w") as f:
                f.write(dataString)
            f.close()
            prGreen("Addition successful!")
            # print("Remember to delete the } at the end")
    """print("English word: (To go back menu, enter 0)")
    userEnglishInput = input()
    if userEnglishInput == "0":
        menu()
    else:
        print("Malay Equivalent: (To go back menu, enter 0)")
        userMalayInput = input()
        if userMalayInput == "0":
            menu()
        else:
            with open('databaseWk8-13.txt', 'a') as f:
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
            prGreen("Addition successful!")
            print("Remember to delete the } at the end")"""


def menu():
    print("=========================")
    print("""-------------------------
flashcard learning system
-------------------------""")
    print("Select the following options:")
    print("1: Do the questions (Wk 1-7)")
    print("2: Do the questions (Wk 8-13)")
    print("3: Add to vocublary database (Wk1-7)")
    print("4: Add to vocublary database (Wk8-13)")
    print("5: Search word (coming soon)")
    print("=========================")
    userInput = input()
    match(userInput):
        case "1":
            database = readingsystem1()
            flashcardsystem(database)
        case "2":
            database = readingsystem2()
            flashcardsystem(database)
        case "3":
            while True:
                addtoDatabase1()
        case "4":
            while True:
                addtoDatabase2()
        case _:
            prRed("Error!")
            print("please select the appropriate options")
            menu()


def main():

    menu()


main()
