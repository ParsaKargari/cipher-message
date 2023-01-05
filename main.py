# encryption.py
# Parsa Kargari
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.

def list_to_dictionary_enc(alph_list, ciph, map):
    """
    Function that maps together two lists as key and value pairs. This is for encoding so it takes the alphabet list as keys and cipher as values and 
    maps it together to a new variable "mapping".

    Arguments:
    alphabet_list -- A list containing the 26 letters of the alphabet in lowercase
    cipher -- List of the single element strings inputted by the user, wanting it to be their cipher
    mapping -- Blank dictionary than is turned into a key:value pair by the end of the function, alphabet_list as keys, and cipher as values

    Returns:
    None

    """
    for keys1 in alph_list:
        for value1 in ciph:
            map[keys1] = value1[0]
            ciph.remove(value1[0])
            break


def list_to_dictionary_dec(ciph, alph_list, map):
    """
    Function that maps together two lists as key and value pairs. This is for decoding so it takes the cipher as keys and alphabet list as values and 
    maps it together to a new variable "mapping".

    Arguments:
    cipher -- List of the single element strings inputted by the user, wanting it to be their cipher
    alphabet_list -- A list containing the 26 letters of the alphabet in lowercase
    mapping -- Blank dictionary than is turned into a key:value pair by the end of the function, cipher as keys, and alphabet_list as values

    Returns:
    None

    """
    for keys2 in ciph:
        for value2 in alph_list:
            map[keys2] = value2[0]
            alph_list.remove(value2[0])
            break


def printer(output):
    """
    Function that joins a list of elements together into a single long string. It joins them without any space or anything, it's simply blank and easy to read by the reader

    Arguments:
    output_list -- A list of single elements (strings) that is the program's output but in a form of a list

    Returns:
    str_output -- A single string that is gotten from a list that was joined by the function. This is the programs output.
    """
    str_output = ''.join(output)
    return str_output


def outputer(text, map, output):
    """
    Function that adds the values from the mapping dictionary as appropiate to the output_list list. Checks each letter in the user's text then compares and matches it to the mapping
    dictionary's keys. If match is found, it appends the value of that certain key to the output_list list. This function makes sure to find the right values that want to be outputed by the
    user's unique cipher.
    Also has the printer() function in it and prints the user output at the end of the function. (More details on the printer() function can be found above)

    Arguments:
    text_list -- List of letter of the user's original input that needs to be either encoded or decoded
    mapping -- A dictionary mapping key:value pairs. alphabet_list as either key or value and cipher as either key or value, according and with respect to the user's choice of encoding/decoding.
    output_list -- A list of single elements (strings) that is the program's output but in a form of a list

    Returns:
    None

    """
    for letter in text:
        for letter_dict in map:
            if letter == letter_dict:
                output.append(map[letter_dict])
                break
    print('Your output is: {}\n'.format(printer(output_list)))


def dupe_remover(ciph, arbl):
    """
    As the name says it itself, a function that removes duplicate strings from a given list. Uses a "dummy" list to store in the unique strings. It appends every string to the dummy list that
    is NOT found in the dummy list, with this logic, it will add only unique strings to the list. In this function specifically, duplicates are being removed from the cipher, without changing its order.

    Arguments:
    cipher -- List of the single element strings inputted by the user, wanting it to be their cipher
    arblist -- A blank list at first, but appended with UNIQUE strings at the end of the function to be used by the program

    Returns:
    None

    """
    for n in ciph:
        if n not in arbl:
            arbl.append(n)


def validator(ciph, ciph_input):
    """
    Function that validates the cipher given by the user. Makes sure that the cipher is alphanumeric, has no spaces and it must have a length of 26. If any of those conditions aren't met it returns a False boolean

    Arguments:
    cipher: List of the single element strings inputted by the user, wanting it to be their cipher
    user_cipher_input: The direct cipher that is inputed by the user to the program. A long string. 

    Returns:
    (CONDITIONAL BOOLEAN) False  

    """
    if len(ciph) != 26:
        return False
    elif ciph_input.isalnum() == False:
        return False
    elif ciph_input.isspace() == True:
        return False


###
# List of lower case alphabets defined to a variable
alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
mapping = {}        # Blank dictionary, to map alphabets and cipher
output_list = []    # Blank list, that will contain the user output
choice = 1          # A dummy choice that will be changes by the user
cipher = []         # Blank list, will be turned into a list of the user cipher
arblist = []        # A dummy list will be used by a function to remove duplicates
###

print("ENDG 233 Encryption Program")

while choice == 1 or choice == 2:

    # User is asked to choose from 3 options, if the choice is not recognized by the program, it will ask the user to input it again.
    # Program will move on if choice is recognized. Valid choices: 0, 1, 2
    # User choice is stored
    choice = int(
        input('Select 1 to encode or 2 to decode your message, select 0 to quit: '))
    if choice != 0 and choice != 1 and choice != 2:
        choice = 1
        print('Choice number not recognizd.\n')
        continue
    elif choice == 0:   # Early leave from the user, if choice is 0 then program breaks out of the while loop
        break

    text = str(input('Please enter the text to be processed: ')
               )                # Program asks for the user's text
    # Text is turned to list
    text_list = list(text)
    # Program asks for user's desired cipher
    user_cipher_input = str(input('Please enter the cipher text: ')).lower()
    # Cipher is turned to list
    cipher = list(user_cipher_input)
    # Paremeters are given to the function. removes any dupes within the cipher without changing the order of it
    dupe_remover(cipher, arblist)
    cipher = arblist

    # Program has to encode the user text if choice 1 was selected originally
    if choice == 1:

        # User's cipher must be valid. Parameters are given to the function. Function checks for the validity of the cipher, and returns False IF cipher is NOT valid.
        # If cipher validity returns False, user is directed back at the main menu.
        if validator(cipher, user_cipher_input) == False:
            print(
                'Please enter a valid Cipher! Tip: Use 26 unique elements of a-z or 0-9.\n')
            arblist = []
            continue
        # Cipher is valid once it passes the validity check
        print('Your cipher is valid.')
        # Paramters are sent to the function. Encodes the user's text accordingly, and stores the new output in a new variable as a list
        list_to_dictionary_enc(alphabet_list, cipher, mapping)
        # Parameters are sent to the function. Turns list into a single string and prints it as the out put of the program
        outputer(text_list, mapping, output_list)

        # Resets mapping, output_list, arblist for the next use by the user
        mapping = {}
        output_list = []
        arblist = []

    # If original choice was 2, program has to decode the user's text
    elif choice == 2:

        # User's cipher must be valid. Parameters are given to the function. Function checks for the validity of the cipher, and returns False IF cipher is NOT valid.
        # If cipher validity returns False, user is directed back at the main menu.
        if validator(cipher, user_cipher_input) == False:
            print(
                'Please enter a valid Cipher! Tip: Use 26 unique elements of a-z or 0-9.\n')
            arblist = []
            continue
        # Cipher is valid once it passes the validity check
        print('Your cipher is valid.')
        # Paramters are sent to the function. Decodes the user's text accordingly, and stores the new output in a new variable as a list
        list_to_dictionary_dec(cipher, alphabet_list, mapping)
        # Parameters are sent to the function. Turns list into a single string and prints it as the out put of the program
        outputer(text_list, mapping, output_list)

        # Resets mapping, output_list, arblist, alphabet_list for the next use by the user
        alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
        mapping = {}
        output_list = []
        arblist = []

    # If choice is somehow not recognized by the program as an error in the program
    # This will never occur, and is a default
    else:
        break

# End of program
print('\n\nThank you for using the encryption program. Hope to see you encrypting again!')
