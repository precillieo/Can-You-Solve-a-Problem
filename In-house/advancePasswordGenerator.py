import random

def smallLetter(num):
    char = ""
    for i in range(num):
        char += chr(random.choice(range(97, 123)))

    return char

def capitalLetter(num):
    char = ""
    for i in range(num):
        char += chr(random.choice(range(65, 91)))

    return char

def numbers(num):
    char = ""
    for i in range(num):
        char += str(random.choice(range(0, 10)))

    return char

def specialChar(num):
    char = ""
    for i in range(num):
        char += chr(random.choice(range(33, 44)))

    return char


if __name__ == "__main__":
    small_letters = int(input("Enter the number of Small letters in your password: "))
    capital_letters = int(input("Enter the number of Capital letters in your password: "))
    nums = int(input("Enter the number of Number in your password: "))
    special_characters = int(input("Enter the number of Special characters in your password: "))
    
    password = f"{smallLetter(small_letters)}{capitalLetter(capital_letters)}{numbers(nums)}{specialChar(special_characters)}"
    
    updatedPass = ''.join(random.sample(password, len(password)))
    # print(password)
    print('\n')
    print(f"Your new secured password is: {updatedPass}")