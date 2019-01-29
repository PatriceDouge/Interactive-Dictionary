import json
import difflib
from difflib import get_close_matches

#loading the dictionary json data
data = json.load(open("data.json"))

#function for getting definitions
def get_def(word):

    #making word all lowercase
    word = word.lower()

    #check if word is in dictionary
    if word in data:
        return data[word]

    #checking if the word w/capital letter is in dict
    elif word.title() in data:
        return data[word.title()]

    #checking if the word w/all capital letters is in dict
    elif word.upper() in data:
        return data[word.upper()]

    #checking for a similar word 
    elif len(get_close_matches(word, data.keys())) > 0:
        ans =  input("Did you mean %s? [Yes or No]: " % get_close_matches(word, data.keys())[0])
        ans = ans.lower()

        if (ans == "yes"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (ans == "no"):
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return ("Yes or No")

    else: 
        return ("The word you entered was not found.")

#input from the user
input_word = input("Enter a word: ")

output = get_def(input_word)

if type(output) == list:
    for item in output:
        print("-", item)

else:
    print("-", output)


