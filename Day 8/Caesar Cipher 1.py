alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Tipo 'encode' para cifrar, tipo 'decode' para descifrar:\n").lower()
text = input("Escribe tu mensaje:\n").lower()
shift = int(input("Ingresa el número de desplazamiento:\n"))

# if direction == "encode":
#     def encrypt(original_text, shift_amount):
#         cipher_text = ""
#         for letter in original_text:
#             shifted_position = alfabeto.index(letter) + shift_amount # 7 -> 9
#             shifted_position %= len(alfabeto) # 0-25
#             cipher_text += alfabeto[shifted_position]
#         print(f"The encoded text is {cipher_text}")

#     encrypt(text, shift)
# else:
#     def decrypt(cipher_text, shift_amount):
#         output_text = ""
#         for letter in cipher_text:
#             shifted_position = alfabeto.index(letter) - shift_amount
#             output_text += alfabeto[shifted_position]
#         print(f"The decoded text is {output_text}")

#     decrypt(text, shift)


def caesar(text, shift, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
                shift *= -1
    for letter in text:
        if letter not in alfabeto:
            output_text += letter
        else: 
            
            shift_position = alfabeto.index(letter) + shift
            shift_position %= len(alfabeto)
            output_text += alfabeto[shift_position]
    print(f"The {encode_or_decode}d text is {output_text}")
    
caesar(text, shift, direction)

should_continue = True

while should_continue:
    direction = input("Tipo 'encode' para cifrar, tipo 'decode' para descifrar:\n").lower()
    text = input("Escribe tu mensaje:\n").lower()
    shift = int(input("Ingresa el número de desplazamiento:\n"))

    caesar(text, shift, direction)
    result = input("Deseas continuar? 'yes' or 'no'\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye!")
    else:
        should_continue = True
        
