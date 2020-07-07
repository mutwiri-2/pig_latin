# pig_latin.py - a program to translate English words to pig latin

def pig_latin(text):

    VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

    pig_latin_words_list = [] 
    for word in text.split():
        prefix_non_letters = '' # non-letter characters at the beginning of the word
        while len(word) > 0 and not word[0].isalpha(): 
            prefix_non_letters += word[0]
            word = word[1:]
        # if the whole word is made of non-letters, add it to the pig_latin_words_list and continue to next word
        if len(word) == 0:
            pig_latin_words_list.append(prefix_non_letters)
            continue

        suffix_non_letters = '' # non-letter characters at the end of the word
        while not word[-1].isalpha():
            suffix_non_letters += word[-1]
            word = word[:-1]
        
        # Remember if word was uppercase or titlecase to convert back later
        was_upper = word.isupper()
        was_title = word.istitle()

        word = word.lower() # convert word to lowercase for translation

        prefix_consonants = '' # consonant sounds that appear at the beginning of the word
        while len(word) > 0 and word[0] not in VOWELS:
            prefix_consonants += word[0]
            word = word[1:]

        # translate word to Pig Latin
        if prefix_consonants != '':
            word += prefix_consonants + 'ay'
        else:
            word += 'yay'

        # convert word back to original case
        if was_upper:
            word = word.upper()
        if was_title:
            word = word.lower()
        
        # add converted word to pig latin list
        pig_latin_words_list.append(prefix_non_letters + word + suffix_non_letters)

    return ' '.join(pig_latin_words_list) # return the new translated text
