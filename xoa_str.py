#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe

def cipher(s):
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
    print ("BIN_LIST:    ", bin_list)
    print ("BIN_STRINGS: ", bin_strings)
    print ("ORDER:       ", order)
    print ("VALUES:      ", values)
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
    print ("".join([chr(i) for i in end_values])
           )
    print ("MIXED_BIN:   ", mixed_bin)
    print ("END_VALUES:  ", end_values)
    










if __name__ == "__main__":
    string = input("Give string: \n")
    cipher(string)
