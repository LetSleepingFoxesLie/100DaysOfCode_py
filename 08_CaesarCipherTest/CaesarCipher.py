# Generating both lowercase and UPPERCASE alphabets
alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = alphabet_lower.upper()

# We gotta fetch the word we wanna cipher somehow. This is how
def get_word():
    word = input("What is the word you want to encrypt? ")
    return word

# And then we gotta do the same for the offset
def get_shift():
    shift = input("What's the offset? ")
    return shift

# For our Caesae cipher to work, we need to find the index at which a specific letter is.
# Since both alphabets are the same other than one having lowercase and the other uppercase,
# we can skip a conditional check by converting everything to lowercase.
def get_letter_index(letter):
    index = 0
    for character in alphabet_lower:
        if letter.lower() == character:
            return index
        else:
            index += 1

# Our Caesar cipher itself
def caesar_cipher(word, offset):
    shifted = ""
    
    # Iterating through each letter in our word
    for letter in word:
        
        # Skipping some specific characters that don't need to be shifted
        if letter not in alphabet_lower:
            shifted += letter
        elif letter in alphabet_lower:
            shifted += alphabet_lower[(get_letter_index(letter) + int(offset)) % len(alphabet_lower)]
        else:
            shifted += alphabet_upper[(get_letter_index(letter) + int(offset)) % len(alphabet_upper)]
            
    return shifted

def main():
    shifted = caesar_cipher(
        get_word(),
        get_shift()
    )
    print(shifted)

main()