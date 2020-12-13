# User enters a word to see the definition

import json
import difflib

info = json.load(open("data.json"))

# convert key names into lowercase
data = {x.lower():info[x] for x in info.keys()}

user_word = input("Enter word: ").lower()


def suggest_word(error_word):
    return difflib.get_close_matches(error_word, data.keys())[0]


def find_meaning(word):
    while True:
        try:
            meaning = ""
            for definition in data[word]:
                meaning += definition + "\n"
            return meaning
        except KeyError:
            if suggest_word(word):
                suggestion = input(f"Did you mean {suggest_word(word)} instead? \n"
                                   f"Enter Y if yes, or N if no: ")
                if suggestion == 'Y'.lower():
                    word = suggest_word(word)
                    continue
                return "Entry not understood."
            return "The word doesn't exist. Please double check it."


print(find_meaning(user_word))
