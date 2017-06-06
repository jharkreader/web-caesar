import string

def alphabet_position(letter):
    """Takes a letter and returns its index, 0 - 25 """
    letter = letter.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for index in range(len(alphabet)):
        if letter == alphabet[index]:
            return index

def rotate_char(char, rot):
    """Takes a character char and rotates it by a factor of rot"""
    rot = int(rot)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rot_char = ""
    pos = alphabet_position(char)
    new_pos = (pos + rot) % 26
    rot_char = alphabet[new_pos]
    
    if char in string.ascii_uppercase:
        return rot_char.upper()

    return rot_char