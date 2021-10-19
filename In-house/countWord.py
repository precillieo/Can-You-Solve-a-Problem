def countSentence():
    """
    countSentence() return the word count entered by the user.

    Variables: sentence: str

    """
    # take input from the user
    sentence = input("Enter a sentence: ")

    #removes space

    sentence = sentence.strip()

    #define a variable to count the sentence and set to zero
    count = 0

    # for loops to iterate the sentence and count

    for i in sentence:

        count = count+1

    print(f"The total count of your sentence is {count}.")


countSentence()
