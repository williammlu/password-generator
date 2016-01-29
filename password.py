import hashlib
import pdb


def swapLetters(s, swap_index):
    """
    In ever pair of values in swap_index, letters in s are swapped

    Parameters:
        s: list of characters to be mutated
        swap_index: list of indices to swap

    Returns:
        Mutated s where appropriate letters are swapped
    """

    for v in range(0, len(swap_index)//2):
        a = swap_index[v*2]
        b = swap_index[v*2 + 1]
        s[a], s[b] = s[b], s[a]
    return s



def baseChange(base, val):
    """
    Converts absolute value of an integer into a different base

    Parameters:
        base: new base to use
        val: original integer that will be converted

    Returns:
        A list of integers representing the digits of the number in new base
    """

    val = abs(val)
    output = []
    if(val == 0):
        return [0]

    while(val != 0):
        output.append(val%base)
        val = int(val//base)
    
    output.reverse()
    return output



possible_letters = list('abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ')
pl_length = len(possible_letters)
print('Enter in a number that creates')
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
strs = [str1, str2]

hash1 = int(hashlib.sha512(bytes(str1,  encoding="UTF-8")).hexdigest(), 16)
hash2 = int(hashlib.sha1(bytes(str2,  encoding="UTF-8")).hexdigest(), 16)
#must use determinstic hash function so that each run with the same inputs will be 

swap_indices = baseChange(pl_length, hash1)
swapLetters(possible_letters, swap_indices) # rearranges values in possible_letters
letter_index = baseChange(pl_length, abs(hash2))
letters = [possible_letters[v] for v in letter_index] # selects random characters based on hash of second string

password = "".join(letters)

print(password)

