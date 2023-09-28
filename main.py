import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    name = input("Enter word: ").upper()
    try:
        nato_name = [nato_dict[letters] for letters in name]
    except KeyError:
        print("Sorry, only letters please")
        generate_phonetic()
    else:
        print(nato_name)


generate_phonetic()
