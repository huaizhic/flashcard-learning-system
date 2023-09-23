import random
import json


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


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
        print("What is (", question, ") in malay? (type in lowercase)")
        userinput = input()

        if userinput == answer:
            prGreen("Correct!")
            print(" It is (", answer, ")")
        else:
            prRed("Wrong!")
            print(" It is (", answer, ")")


def main():
    database = readingsystem()
    print("To skip question, just press Enter")
    flashcardsystem(database)


main()
