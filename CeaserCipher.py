alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def func():
    def ceaser(x, y):
        ciphered_text = ""
        for char in x:
            if char in alphabet:
                position = alphabet.index(char)
                if direction == 'encode':
                    new_pos = position + y
                elif direction == 'decode':
                    new_pos = position - y
                else:
                    print("The direction was invalid.")
                    exit()
                new_letter = alphabet[new_pos]
                ciphered_text += new_letter
            else:
                ciphered_text += char
        print(f"The text is {ciphered_text}")

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = str(input("Type your message:\n")).lower()
    shifted = int(input("Type the shift number:\n"))
    shift = shifted % 26
    ceaser(text, shift)

func()

replay = input('Use again?(Y/N): ')

while replay == 'Y':
    func()
    

