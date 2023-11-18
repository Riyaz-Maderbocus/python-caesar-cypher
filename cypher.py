import art


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def code(message, shift):
    shift = shift % 26
    new_message = ""
    for char in message:
        if char not in alphabet:
            new_message += char
        else:
            old_index = alphabet.index(char)
            new_index = old_index + shift
            if new_index > 25:
                new_index -= 26
            new_message += alphabet[new_index]
    return new_message


print(art.logo)
is_on = True

while is_on:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "decode":
        shift *= -1

        print(f"Your decoded message is :\n{code(text, shift)}")

    elif direction == "encode":

        print(f"Your encoded message is :\n{code(text, shift)}")

    user_choice = input("Do you want to go again? y/n")

    if user_choice == "n":
        is_on = False

print("finished")


# encode("hello", 1)
# encode(text, shift)
