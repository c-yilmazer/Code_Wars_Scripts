#Write a function that takes a string and turns any and all "words" (see below) within that string of length 4 or greater into an abbreviation, following these rules:

#A "word" is a sequence of alphabetical characters. By this definition, any other character like a space or hyphen (eg. "elephant-ride") will split up a series of letters into two words (eg. "elephant" and "ride").
#The abbreviated version of the word should have the first letter, then the number of removed characters, then the last letter (eg. "elephant ride" => "e6t r2e").

def abbrv(s):  #s for string
    strings = []
    current_string = ""
    
    for ch in s:
        if ch.isalpha(): #keep letters
            current_string += ch
        else:
            if current_string:
                strings.append(current_string)
                current_string = "" #reset for next word
                strings.append(ch)
    if current_string:
        strings.append(current_string)
    
    # now it should return all words separated inside a list
    #i.e ["elephant","-", "rides","", "are","", "really","","fun","!"]
    new_strings = []
    for word in strings:
        if len(word)>=4 and word.isalpha(): #turn into abbr 
            new_word = word[0] + str(len(word)-2) + word[-1] #take the first and last character of a word, then turn the length of remaining 
            #into a string and add to the middle of the new word
            new_strings.append(new_word)
        elif word == "." or word == ";" or word == "," or word == ":": #separators get space after
            new_strings.append(word +" ")
        
        else:
            new_strings.append(word)
    return "".join(new_strings)

print(abbrv("the,cat d4e-b6d-"))