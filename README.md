    # Password Genertor
    #### Video Demo:  https://youtu.be/kHCB05_6NuU
    #### Description:
    The password generator software will generate random passwords based on user-specified criteria. It will allow users to define the length of the password and choose whether to include numbers, symbols, uppercase letters, and lowercase letters. The software will generate a unique password each time it is executed.

    The password generator will have the following features:
    User input for password length
    Options to include numbers, symbols, uppercase letters, and lowercase letters
    Random generation of passwords based on user specifications
    Display of the generated password to the user

    The password generator can be executed in a console interface. Users will run the program, specify their desired password criteria, and the program will generate a password accordingly. The generated password will be displayed on the console for the user to see.

    Creating strong passwords is of paramount importance as it serves as a vital line of defense against unauthorized access and protects sensitive information. Strong passwords significantly reduce the risk of successful hacking attempts, mitigating the impact of data breaches and safeguarding personal accounts, financial details, and private communications. By preventing unauthorized access, strong passwords ensure the security of online presence, compliance with security best practices, and prevention of identity theft, unauthorized transactions, and reputational damage. Investing in strong passwords is an essential practice to maintain the integrity and confidentiality of personal accounts and data in an increasingly interconnected digital landscape.

    I used the proposed structure from the task, which included one main function and three custom functions. In the first function, "password_generator," I passed all the user-specified arguments such as length, numbers, symbols, uppercase letters, and lowercase letters. After gathering the user's choices, I stored all the characters in a variable called "characters." Then, using a while loop, I randomly selected characters from the "characters" variable and checked if they met the criteria, such as being a digit or symbol. The loop continued to randomly select characters until the generated password's length was not less than the specified length.

    In the get_length function, we check the length of the password, and we do not allow the user to enter a length less than 4. Additionally, if the user mistakenly enters a letter or symbol instead of a number, they will receive a ValueError. In such cases, we will ask the user again for the length using the keyword pass.


    And finally, we have the get_letters function that checks whether the user wants uppercase or lowercase letters in the password. In the case where the user chooses "no" for both lowercase and uppercase letters, we will reject the input and ask the user again. We will send a message stating that they need to choose at least one letter case or both of them.

