def caesar_cypher(message, key):

    encrypted_msg = ""

    for i in message:
        i = i.lower()
        if ord(i) == 32:
            encrypted_msg += ' '
        elif ord(i) >96 and ord(i) <173:
            value = ord(i)-97
            new_value = ((value+key)%26)+97
            new_letter = chr(new_value)
            encrypted_msg+= (new_letter)

        else:
            encrypted_msg += i

    return(encrypted_msg)






message = input('Enter a message: ')

key = input('Enter a message to encrypt: ')

try:

    key = int(key)

exce

encrypted_msg = caesar_cypher(message, key)

print(encrypted_msg)