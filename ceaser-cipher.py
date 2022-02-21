
def encode(text,shiftn):
    newmsg =""
    for letter in text:
        position = letters.index(letter)
        new_pos = position + shiftn
        newmsg+=letters[new_pos]

    print(f"the encrypted message is {newmsg}")

def decode(text,shiftn):
    newmsg = ""
    for letter in text:
        position = letters.index(letter)
        new_pos = position - shiftn
        newmsg += letters[new_pos]

    print(f"the decrypted message is {newmsg}")


letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while(1):
 dir = input("enter 'encode' to encode or 'decode' to decode a message in ceaser cipher")
 msg = input("type the message").lower()
 shift = int(input("enter the number of shift"))
 if dir=="encode":
    encode(msg,shift)
 if dir=="decode":
    decode(msg,shift)


