import json

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
    else: 
        return ("The word you entered was not found.")

#input from the user
input_word = input("Enter a word: ")

print(get_def(input_word))

