def word_counter():
    '''
        This function converts a sentence to a list and return the number of words in the list.
    '''
    sentence = input('Enter a sentence: ')
    sentence_list = sentence.split(' ')
    word_count = len(sentence_list)

    print('Word count:', word_count)

word_counter()
