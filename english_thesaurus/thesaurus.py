import re
import json
import difflib

info = json.load(open("data.json"))

# convert key names into lowercase
data = {x.lower(): info[x] for x in info.keys()}


def get_user_input():
    word = input("Enter word: ").lower()
    if re.search(r"\d", word) or re.search(r"\W", word):
        return False
    return word


def suggest_close_word(error_word):
    return difflib.get_close_matches(error_word, data.keys())[0]


def get_definition():
    word = get_user_input()
    while True:
        if not word:
            return "Search cannot include numbers/special characters"
        if word in data.keys():
            answer = ""
            for item in data[word]:
                answer += item + "\n"
            return answer
        elif suggest_close_word(word) is not None:
            new_suggest = input(f"Did you mean {suggest_close_word(word)} instead? Y/N? ").lower()
            if new_suggest == "y":
                word = suggest_close_word(word)
                continue
        return "The word does not exist"


print(get_definition())
