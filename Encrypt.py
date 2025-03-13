def generate_inverse_sboxes(sboxes): 

    inverse_sboxes = [] 

    for sbox in sboxes: 

        inverse_sbox = [0] * 16 

        for i in range(16): 

            inverse_sbox[sbox[i]] = i 

        inverse_sboxes.append(inverse_sbox) 

    return inverse_sboxes 

# Define new 16-element S-boxes for substitution 

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

# Permutation patterns 

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

def encrypt(plaintext, key): 

    subkeys = generate_subkeys(key) 

    block = plaintext 

    for i in range(4): 

        block = substitute_block(block, S_BOXES[i % len(S_BOXES)]) 

        block = permute_block(block, PERMUTATION) 

        block ^= subkeys[i] 

    return block 

  

 

def decrypt(ciphertext, key): 

    subkeys = generate_subkeys(key) 

    block = ciphertext 

    for i in range(3, -1, -1): 

        block ^= subkeys[i] 

        block = permute_block(block, INVERSE_PERMUTATION) 

        block = substitute_block(block, INVERSE_S_BOXES[i % len(INVERSE_S_BOXES)]) 

    return block 

def string_to_hex_blocks(plaintext): 

    hex_blocks = [] 

    hex_string = "".join(f"{ord(c):02X}" for c in plaintext) 

    if len(hex_string) % 4 != 0: 

        hex_string += "0" * (4 - len(hex_string) % 4) 

    for i in range(0, len(hex_string), 4): 

        hex_blocks.append(int(hex_string[i:i+4], 16)) 

    return hex_blocks 

def main(): 

    plaintext = input("Enter plaintext string: ") 

    key = int(input("Enter a 16-bit key", 16) 

    plaintext_blocks = string_to_hex_blocks(plaintext) 

    ciphertext_blocks = [encrypt(block, key) for block in plaintext_blocks] 

    decrypted_blocks = [decrypt(block, key) for block in ciphertext_blocks] 

    print("Results:") 

    print("  Plaintext Blocks (Hex):", " ".join(f"{block:04X}" for block in plaintext_blocks)) 

    print("  Ciphertext Blocks:      ", " ".join(f"{block:04X}" for block in ciphertext_blocks)) 

    print("  Decrypted Blocks:       ", " ".join(f"{block:04X}" for block in decrypted_blocks)) 

    print("  Match:", "Success" if plaintext_blocks == decrypted_blocks else "Failure") 

if __name__ == "__main__": 

    main() 
 
