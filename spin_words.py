#Write a function that takes in a string of one or more words, and returns the same string, 
# but with all words that have FIVE OR <PRE letters REVERSED (Just like the name of this Kata). 
# Strings passed in will consist of only letters and spaces. 
# Spaces will be included only when more than one word is present.
#Examples:

#"Hey fellow warriors"  --> "Hey wollef sroirraw" 
#"This is a test        --> "This is a test" 
#"This is another test" --> "This is rehtona test"

def spin_words(sentence):
    strings = []
    current_string = ""

    for ch in sentence:
        if ch.isalpha(): #keep letters
            current_string += ch
        else:
            if current_string:
                strings.append(current_string)
                current_string= "" #reset for next word
                strings.append(ch) #for adding spaces
    if current_string:
        strings.append(current_string)

#now it returns all words separated inside a list
#i.e ["Hey"," ","fellow"," ", "warriors"]
#this allows us to take every word as an item and play around with them if necessary

    new_strings = [] #this will store our new words after processing
    for word in strings:
        if len(word) >= 5 and word.isalpha():
            new_word = word[-1:-(len(word)+1):-1]
            #new_word = word[-1:-len(word)+1:-1] is the appropriate format
            new_strings.append(new_word)
        else:
            new_strings.append(word) #for spaces
    return "".join(new_strings)

print(spin_words("Hey fellow warriors"))