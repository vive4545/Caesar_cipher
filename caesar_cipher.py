print("   ____                                      ____ _ _           \n  / ___|__ _ _ __ ___  _ __   ___ _ __      / ___(_) | ___  ___ \n | |   / _` | '_ ` _ \\| '_ \\ / _ \\ '__|____| |   | | |/ _ \\/ __|\n | |__| (_| | | | | | | |_) |  __/ | |_____| |___| | |  __/\\__ \\\n  \\____\\__,_|_| |_| |_| .__/ \\___|_|        \\____|_|_|\\___||___/\n                      |_|                                       ")

def caesar(original_text,shift_text,encode_or_decode):
    alphabet = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l","m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
    output_text = ""  
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter       
        else:
            if encode_or_decode == "decode":
                shift_text *= -1

            encoded_text = alphabet.index(letter) + shift_text
            encoded_text %= len(alphabet)
            output_text += alphabet[encoded_text]
        print(f"Here is the {encode_or_decode}d text:\n{output_text}")


status = True
while status:
    direction = input("Type 'encode' for encoding and 'decode' for decoding : \n").lower()
    text = input("Type your message :\n").lower()
    shift = int(input("Type the shift number : \n"))
    caesar(original_text=text, shift_text=shift, encode_or_decode=direction)
    
    choice = input("Do you want to continue? (y/n) \n").lower()
    if choice != "y":
        status = False