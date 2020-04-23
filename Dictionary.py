import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def translation(word):
    if word in data.keys():
        return data[word]
    elif(len(get_close_matches(word, data.keys(), n=1, cutoff=0.8)) > 0):
        simllar = get_close_matches(word, data.keys(), n=1, cutoff=0.8)[0]
        Q = input("did you mean \"%s\" insted [y/n] : " % simllar)
        if (Q == 'y'):
            return data[simllar]
        elif (Q == 'n'):
            return "The word doesn't exist , please double check your word "
        else:
            return "sorry we couldn't understand your Query"
    else:
        return "The word doesn't exist , please double check your word "


word = input("Enter a word: ")
word = word.lower()
message = translation(word)

if type(message) == list:
    for item in message:
        print(item)

else:
    print(message)
