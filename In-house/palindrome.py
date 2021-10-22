def palindrome_checker():
    '''This function converts any string entered to lowercase and checks it against a reversed string'''
    string = input('Enter a string: ').lower()
    if (string == string[::-1]):
        print('This is a palindrome')
    else:
        print('Not a palindrome')

palindrome_checker()
