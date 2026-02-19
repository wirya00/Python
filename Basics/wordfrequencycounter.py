text = input('Put your text that you want the words to counted: ')

#Lower text to prevent counting 'Apple' and 'apple' as different words.
text = text.lower()

#Example of text: Apple banana apple, splitting it to: 'apple', 'banana', 'apple'. Turning text into a list called words.
words = text.split()

#Empty dictionary
frequency = {}

#Looping for in words as a list
for word in words:
    #If one fo the word in words is in frequency, it adds one to the value.
    if word in frequency:
        frequency[word] = frequency[word] + 1
    #If one of the word in words is not in frequency, it adds/creates one in frequency with inserting one as the value and the word as the key.
    else:
        frequency[word] = 1

#Looping for each word in frequency and printing variable word and a string of '=' and the value of the word in frequency dictionary
for word in frequency:
    print(word, '=', frequency[word])