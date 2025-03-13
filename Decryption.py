def generate_inverse_sboxes(sboxes): 

    inverse_sboxes = [] 

    for sbox in sboxes: 

        inverse_sbox = [0] * 16 

        for i in range(16): 

            inverse_sbox[sbox[i]] = i 

        inverse_sboxes.append(inverse_sbox) 

    return inverse_sboxes 

  

# Define the same S-boxes used during encryption 

S_BOXES = [ 

    [0xE, 0x4, 0xD, 0x1, 0x2, 0xF, 0xB, 0x8, 0x3, 0xA, 0x6, 0xC, 0x5, 0x9, 0x0, 0x7], 

    [0xA, 0x5, 0xE, 0x6, 0xB, 0xF, 0x0, 0xC, 0x8, 0x1, 0x9, 0x3, 0xD, 0x7, 0x4, 0x2], 

    [0x6, 0xC, 0xA, 0x3, 0x7, 0x0, 0xE, 0x5, 0x8, 0x2, 0xD, 0xF, 0x9, 0x1, 0xB, 0x4], 

    [0x9, 0x2, 0x8, 0xD, 0x0, 0xA, 0x7, 0xE, 0x3, 0xC, 0x1, 0x6, 0xF, 0x5, 0x4, 0xB], 

    [0xF, 0xB, 0x7, 0xE, 0x9, 0x2, 0x4, 0xC, 0x0, 0x3, 0xA, 0x6, 0xD, 0x1, 0x8, 0x5], 

    [0x5, 0x0, 0xC, 0xA, 0xF, 0x6, 0x2, 0x8, 0x7, 0xB, 0x9, 0xE, 0x1, 0xD, 0x4, 0x3], 

    [0x3, 0x9, 0xF, 0x5, 0xE, 0x8, 0x6, 0x1, 0xC, 0xD, 0x0, 0x7, 0xA, 0x4, 0x2, 0xB], 

    [0x7, 0xE, 0x4, 0xA, 0x8, 0x1, 0x9, 0x5, 0xB, 0x3, 0xD, 0x0, 0x6, 0xF, 0xC, 0x2], 

    [0xD, 0x8, 0x9, 0x2, 0x5, 0xC, 0x0, 0x7, 0x6, 0xB, 0xE, 0x3, 0x1, 0xF, 0x4, 0xA], 

    [0xC, 0x7, 0xE, 0x5, 0xA, 0x1, 0xF, 0x8, 0x0, 0x6, 0x9, 0x4, 0xD, 0xB, 0x2, 0x3], 

] 

  

INVERSE_S_BOXES = generate_inverse_sboxes(S_BOXES) 

  

PERMUTATION = [8, 4, 2, 6, 1, 3, 5, 7, 16, 12, 10, 14, 9, 15, 11, 13] 

INVERSE_PERMUTATION = [PERMUTATION.index(i) + 1 for i in range(1, 17)] 

  

def rotate_left(value, bits, size=16): 

    return ((value << bits) | (value >> (size - bits))) & 0xFFFF 

  

def generate_subkeys(key): 

    return [rotate_left(key, i) for i in range(4)] 

 

 

def substitute_block(block, sbox): 

    left = (block >> 12) & 0xF 

    mid_left = (block >> 8) & 0xF 

    mid_right = (block >> 4) & 0xF 

    right = block & 0xF 

  

    left = sbox[left] 

    mid_left = sbox[mid_left] 

    mid_right = sbox[mid_right] 

    right = sbox[right] 

  

    return (left << 12) | (mid_left << 8) | (mid_right << 4) | right 

  

def permute_block(block, pattern): 

    permuted_block = 0 

    for i, p in enumerate(pattern): 

        bit = (block >> (16 - p)) & 1 

        permuted_block |= bit << (15 - i) 

    return permuted_block 

  

def decrypt(ciphertext, key): 

    subkeys = generate_subkeys(key) 

    block = ciphertext 

    for i in range(3, -1, -1): 

        block ^= subkeys[i] 

        block = permute_block(block, INVERSE_PERMUTATION) 

        block = substitute_block(block, INVERSE_S_BOXES[i % len(INVERSE_S_BOXES)]) 

    return block 

  

def hex_blocks_to_string(blocks): 

    hex_string = "".join(f"{block:04X}" for block in blocks) 

    plaintext = "" 

    for i in range(0, len(hex_string), 2): 

        char_code = int(hex_string[i:i+2], 16) 

        plaintext += chr(char_code) 

    return plaintext.rstrip("\x00")  # Remove padding 

  

def main(): 

    ciphertext = input("Enter ciphertext blocks : ") 

    key = int(input("Enter the 16-bit key"), 16) 

  

    ciphertext_blocks = [int(block, 16) for block in ciphertext.split()] 

    decrypted_blocks = [decrypt(block, key) for block in ciphertext_blocks] 

  

    original_message = hex_blocks_to_string(decrypted_blocks) 

  

    print("Decrypted Message:", original_message) 

  

if __name__ == "__main__": 

    main() 
