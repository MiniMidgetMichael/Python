#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe

def cipher(s):
    length = len(s)
    bin_list = []
    bin_strings = []
    order = {}
    values = {}
    for index, i in enumerate(s):
        order[index] = i
        values[i] = ord(i)
        i = ord(i)
        x = bin(i)
        bin_strings += [x[2:].zfill(8)]
        bin_list += [x]
    mixed_bin = []
    for i in bin_list:
        i = int(i, base=2)
        i = i ^ len(s)
        x = bin(i)
        x = x[2:].zfill(8)
        mixed_bin += [x]
    end_values = []
    for i in mixed_bin:
        i = int(i, base=2)
        end_values.append(i)
    ciphered = "".join([chr(i) for i in end_values])
    if __name__ == "__main__":
        print ("LENGTH:      ", length)
        print ("BIN_LIST:    ", bin_list)
        print ("BIN_STRINGS: ", bin_strings)
        print ("ORDER:       ", order)
        print ("VALUES:      ", values)
        print ("MIXED_BIN:   ", mixed_bin)
        print ("END_VALUES:  ", end_values)
        print ("CIPHERED TEXT:", ciphered)
    return ciphered
    

def decipher(s):
    bin_list = []
    for i in s:
        i = ord(i)
        x = bin(i)
        bin_list += [x]
    end_bin = []
    for i in bin_list:
        i = int(i, base=2)
        i = i ^ len(s)
        x = bin(i)
        x = x[2:].zfill(8)
        end_bin += [x]
    end_values = []
    for i in end_bin:
        i = int(i, base=2)
        end_values.append(i)
    deciphered = "".join([chr(i) for i in end_values])
    if __name__ == "__main__":
        print ("DECIPHERED:  ", deciphered)
    return deciphered





<<<<<<< HEAD
        ***IF CONTENTS ARE SAME, END VALUE IS SAME***
            EX.: 'mike' == 'emki'
    """
    string = 
    print ("## XOR ##\n" + xor_bin(string))
    x_string = xor_bin(string)
    print ("## OR ##\n" + or_bin(string))
    o_string = or_bin(string)
    print ("## AND ##\n" + and_bin(string))
    a_string = and_bin(string)
=======
>>>>>>> refs/remotes/origin/string_bin_ops



if __name__ == "__main__":
    string = input("Give string: \n")
    string = cipher(string)
    decipher(string)
