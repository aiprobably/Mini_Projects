First, we have to import two libraries, string, and random. The string module is used to get the ASCII values of the letters and digits, whereas the random module is used to perform random generations.

Using the string module, we first store ASCII values of letters in variable Letters, digits in variable numbers, and special characters in symbols. We then combine ASCII values of all the letters, numbers, and symbols in the variable All.

We then display a prompt using a print statement welcoming the user to the password generator.

The while loop then begins with a true condition followed by two prompts asking the user to enter the length of the password and number of passwords required and store them into password_length and password_count, respectively.

Then the for loop begins in the range of password_count; this loop is for the number of passwords followed by initializing the value of the variable string to empty.

The next for loop then starts and generates random passwords where the range is from 0 to the password_lenth.This is the ASCII range of all the values for letters, numbers, and symbols.

The password_char then stores the values of all the randomly generated strings. The random. Choice (All) returns a randomly selected element from the sequence All. After which, the chosen random element stored in password_char is added to the variable password, and finally, the generated password is displayed to the user. 


#Procedure to Execute
git clone https://github.com/aiprobably/Mini_Projects/Random-Password-Generator.git
cd Random-Password-Generator/
python3 random_password_generator.py
