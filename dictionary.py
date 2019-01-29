import json

#loading the dictionary json data
data = json.load(open("data.json"))

#function for getting definitions
def get_def(word):
    return data[word]

input_word = input("Enter a word: ")

print(get_def(input_word))