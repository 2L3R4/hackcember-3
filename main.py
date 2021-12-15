
#import bitstring
from textwrap import wrap
def to_ascii(char):
    return chr(int(char, 2))

def translate(txt):
    result = ""
    print(len(txt))
    letters =  [txt[i:i+8] for i in range(0,len(txt), 8)]
    for letter in letters:
        result += to_ascii(letter)
    return result

def main(file="maerchen.txt"):
    msgbits = b""
    with open(file, "r") as f:
        for line in f.readlines():
            
            for word in line.lower().split(" "):
                if word.startswith('"'):
                    # remove " infront of word because there are some words that have it infront of 'cyber' 
                    word = word[1:]
                if word.startswith("cyber-"):
                    print(f"{word.strip()}:\t1")
                    msgbits += b"1"
                elif word.startswith("cyber"):
                    print(f"{word.strip()}:\t0")
                    msgbits += b"0"
                else:
                    pass
    print(msgbits)
    print(translate(msgbits))
    #value = int(msgbits,2)
    #print(len(msgbits)//8)
    #value_bytes = (value.bit_length() + 7) // 8
    #bin_array = value.to_bytes(value_bytes, "big")
    #value = bitstring.BitArray(bin(int(msgbits)))
    #print(value)
    #out = ""
    #print(bin_array)
    #print (bin_array.decode())

if __name__ == "__main__":
    main(file="maerchen.txt")