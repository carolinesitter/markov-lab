"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # read the entire contents of file as a string using .read() method
    contents = open(file_path).read()

    #return 'Contents of your file as one long string'
    return contents

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # split each word by whitespace 
    words = text_string.split() # words = list of strings

    for index in range(len(words)-2):
        #print(words[word], words[word + 1])
        bi_grams = (words[index], words[index + 1])
        value = words[index + 2]
        #print(bi_grams)

        if bi_grams in chains:
            chains[bi_grams].append(value) # creating key value set for bi_grams already in dict
        
        elif bi_grams not in chains:
            chains[bi_grams] = [value] # adding key value set for bi_grams not in dict


    #for bi_grams, value in chains.items(): # printing out dictionary so it looks pretty :) 
        #print(f'{bi_grams} : {value}')   


# EXAMPLE FOR WORKING WITH RANGE AND INDEX (I.E. LINE 50, 53) - not relevant to function!

#hello = ["h", "e", "l", "l", "o"]

#range(len(hello)-2)
#range(3)


    return chains


def make_text(chains):
    """Return text from chains."""

    #words = []
    # your code goes here
    
    #choice((list(chains.keys()))
    bi_grams_list = list(chains.keys())
    key = choice(bi_grams_list)
    #key = choice(list(chains.keys()))

    #words = [key[0], key[1]]
    words = []
    random_word = choice(chains[key])

    while True:
        key = (key[1], random_word)
        
        if key in chains:
            words.append(random_word)
            random_word = choice(chains[key])

        else:
            break
    
    words.append(random_word)
    
        #random_key = choice((list(chains.keys())))
        #choice((list(chains.keys())))


    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
