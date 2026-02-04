


# string = input('enter a sequence to compress: ')
# string += " "


def string_compressor(string):

    compressed = []

    previous_letter = None

    letter_count = 0


    for i in string:
        current_letter = i

        if current_letter == previous_letter:
            letter_count +=1

        if current_letter != previous_letter and previous_letter != None:
            compressed.append(((letter_count + 1) , previous_letter))
            letter_count = 0

        previous_letter = current_letter

    return compressed 

def compressed_write_file(string):
    file = open('Compresed.txt')
    count = 0
    for i in string:
        

def string_decompressor(string):


file= open('input.txt' , 'r')

string = file.read()

string += ""





output = string_compressor(string)


print(output)
