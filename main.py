#! python

from textwrap import wrap
def to_ascii(char):
    return chr(int(char, 2))

def translate(txt):
    result = ""
    #print(len(txt))
    letters =  [txt[i:i+8] for i in range(0,len(txt), 8)]
    for letter in letters:
        result += to_ascii(letter)
    return result

def main(file="maerchen.txt"):
    msgbits = b""
    with open(file, "r") as f:
        for line in f.readlines():
            
            for word in line.lower().split(" "):

                if "cyber-" in word.lower():
                    print(f"{word.strip()}:\t1")
                    msgbits += b"1"
                elif "cyber" in word.lower():
                    print(f"{word.strip()}:\t0")
                    msgbits += b"0"
                else:
                    pass
    #print(msgbits)
    print(translate(msgbits))

if __name__ == "__main__":
    main(file="maerchen.txt")