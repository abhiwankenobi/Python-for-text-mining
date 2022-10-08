from utils_3a import preprocess
def count(text):
    punctuations = []
    user_input = " "
    exit_char = " "
    while exit_char != "n":
        user_input = input("enter the punctuation you want removed ")
        punctuations.append(user_input)
        print("To continue press y, else press n")
        exit_char = input("enter y or n ")
    for punctuation in punctuations:
        text=preprocess(text,punctuation)
    
    words = text.split()
    counts = {}
    for word in words:
        counts[word]=words.count(word)
    return counts
