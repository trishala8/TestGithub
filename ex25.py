def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0) # Prints the first word after popping it off
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)  #This function will break up words for us.
    return sort_words(words) #sords the words

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)  #breaks the words for us
    #Prints the first and last words of the sentence.
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)  #sorts sentence
    #Sorts the words then prints the first and last one
    print_first_word(words)
    print_last_word(words)
