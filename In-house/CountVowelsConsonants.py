def countVowelsConsonants(string:str)-> tuple:
    """
    This function returns the number of vowels and consonants in a string.
    -> (no_vowels, no_consonants)
    """
    vowels = ['a','e', 'i', 'o', 'u']
    consonants = ['b','c','d','f','g','h','j','k','l','m',
              'n','p','q','r','s','t','v','w','x','y','z']
    no_vowels: int = 0
    no_consonants: int = 0
    for char in string:
        char = char.lower() #so the char can match the letters in the list
        #check if the char is part of list of vowels
        if char in vowels:
            no_vowels += 1
        #check if the char is part of list of consonants
        elif char in consonants:
            no_consonants += 1
    return no_vowels, no_consonants

no_vowels, no_consonants = countVowelsConsonants("Beautiful")
print(f"The number of vowels is {no_vowels} and consonants is {no_consonants} in 'beautiful'")

    
