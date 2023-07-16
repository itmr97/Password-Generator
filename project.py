import random
import string

def main():
    min_length=get_length()
    has_uppercase,has_lowercase=get_letters()
    has_number= input ("Do you want to have numbers (y/n)? ").lower() =="y"
    has_special= input ("Do you want to have special characters (y/n)? ").lower()=="y"
    pwd =generate_password(min_length, has_number, has_special,has_lowercase,has_uppercase)
    print("The generated password is:", pwd)

def generate_password(min_Length, numbers=True, special_characters=True,lower=True,upper=True):

    # get the all letter in upper and lower case and the all numbers from 0 to 9 and special characters
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits= string.digits
    special= string.punctuation
    uppercase = uppercase_letters
    lowercase=lowercase_letters
    characters=""

    # check if the user choose uppercase or lowercase or both
    if upper:
        characters+=uppercase
    if lower:
         characters+=lowercase
    #check if the user want number or special characters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    #check if the password meets criteria and choose random from the characters
    pwd=""
    meets_criteria= False
    has_number =False
    has_special= False

    while not meets_criteria or len(pwd) < min_Length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria= True
        if numbers:
            meets_criteria= has_number
        if special_characters:
            meets_criteria= meets_criteria and has_special
    return pwd

def get_letters():
    while True :
        print("you have choose at least one letter case ")
        has_uppercase= input ("Do you want to have uppercase letters (y/n)? ").lower() =="y"
        has_lowercase= input ("Do you want to have lowercase letters (y/n)? ").lower() =="y"
        if not has_uppercase and not has_lowercase:
            continue
        else:
            return has_uppercase,has_lowercase

def get_length():
    while True:
        try:
            length= int(input("Enter the minimum length:"))
            if length<4:
                print("the length should be at least 4")
                continue
            return length

        except ValueError:
            pass

if __name__ == "__main__":
    main()