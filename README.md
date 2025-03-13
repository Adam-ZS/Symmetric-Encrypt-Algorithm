# A New Symmetric Algorithm
Encryption algorithm designed for secure data transmission. It operates on 16-bit blocks of plaintext and uses a set of 10 unique S-Boxes and permutation patterns for encryption and decryption.

# Brief
ADCRYPHAD is a new symmetric encryption algorithm designed for secure data transmission. It operates on 16-bit blocks of plaintext and uses a set of 10 unique S-Boxes and permutation patterns for encryption and decryption. The algorithm incorporates multiple rounds of encryption (4 rounds) with key rotation and substitution operations, making it robust and efficient for real-time cryptographic applications.
# Main Factors
Key Generation: Master keys are rotated to generate 4 subkeys for encryption.

Block Substitution: Each 16-bit block is substituted using predefined S-Boxes.

Permutation: A specific permutation pattern is applied to each block during encryption.

Encryption/Decryption: Both encryption and decryption processes are handled using the subkeys and the inverse of the permutation and S-box.

Manual Tracing: Includes step-by-step tracing with an example plaintext and key to demonstrate the encryption and decryption process.

Code Implementation: Python code to perform encryption and decryption, and test the algorithm with real data.
# Flowchart for the Algorithm
![image](https://github.com/user-attachments/assets/e7602a1b-a15c-4e2b-92e5-d38f523b7534)

# Features
Block Cipher: Works with 16-bit data blocks.

Multiple S-Boxes: 10 unique 16-element substitution boxes for added security.

Permutation-Based Security: A carefully designed bit permutation pattern enhances the algorithm's strength.

Subkey Rotation: Key rotation for each encryption round to prevent attacks.

Encryption and Decryption Functions: Both encryption and decryption are supported with inverse transformations.

Python Code: Fully functional Python implementation of the ADCRYPHAD algorithm.

Manual Tracing: Step-by-step demonstration of encryption and decryption using sample data.

Flexibility: Can be easily adapted for different block sizes and key lengths.

# Manual Tracing with 16-bit Plaintext and Key
    Assume  
    
        Plaintext: 0x1234 
    
        Key: 0xABCD 
    
    1) Convert plaintext string to hexadecimal block 
    
        Plaintext = 0x1234 
    
        This is already in hexadecimal, so we have 
    
        Block 1 = 0x1234 (Hexadecimal format) 
    
    2) Generate subkeys 
    
        We generate subkeys by rotating the key. The key is 0xABCD, which is 1010 1011 1100 1101 in binary. 
    
     
    
        Subkey 1 (Initial key): 0xABCD 
    
        Binary: 1010 1011 1100 1101 
    
        Subkey 2: Rotate the key left by 1 bit: 
    
        Key: 0x579B 
    
        Binary: 0101 0111 1001 1011 
    
        Subkey 3: Rotate the key left by 2 bits: 
    
        Key: 0xAF36 
    
        Binary: 1010 1111 0011 0110 
    
        Subkey 4: Rotate the key left by 3 bits: 
    
        Key: 0x5E6A 
    
        Binary: 0101 1110 0110 1010 
    
      
    
     
    
    3) Encryption (for Block 1 - 0x1234) 
    
        Block 1 = 0x1234 
    
        Sybkey =0xABCD 
    
        Sbox index 0xABCD %10 = [1] 
    
        Binary: 0001 0010 0011 0100 
    
    Now, perform the encryption operations on Block 1. The encryption process involves multiple steps: 
    
        ![image](https://github.com/user-attachments/assets/9e5253c6-873d-4919-94c0-dd36a5af8a0f)
        a.0001 → S-Box lookup → 0x5 

        b. 0010 → S-Box lookup → 0xE 
        
        c. 0011 → S-Box lookup → 0x6 
        
        d. 0100 → S-Box lookup → 0xB 
        
        0x5E6B (0101 1110 0110 1011 in binary.)  
            Permutation: Apply the PERMUTATION pattern. 

    The permutation pattern is  
    [8, 4, 2, 6, 1, 3, 5, 7, 16, 12, 10, 14, 9, 15, 11, 13].  
    This specifies how the bits are rearranged. 
    
    After applying the permutation to 0x5E6B 
    
    (0x5E6B in hex) -> Binary representation: # 0101 1110 0110 1011 
    
    8th bit of input (0) -> 1th bit of output 
    
    4th bit of input (1) -> 2th bit of output 
    
    2th bit of input (1) -> 3th bit of output 
    
    6th bit of input (1) -> 4th bit of output 
    
    1th bit of input (1) -> 5th bit of output 
    
    3th bit of input (0) -> 6th bit of output 
    
    5th bit of input (0) -> 7th bit of output 
    
    7th bit of input (1) -> 8th bit of output 
    
    16th bit of input (0) -> 9th bit of output 
    
    12th bit of input (1) -> 10th bit of output 
    
    10th bit of input (1) -> 11th bit of output 
    
      
    
     
    
    14th bit of input (0) -> 12th bit of output 
    
    9th bit of input (0) -> 13th bit of output 
    
    15th bit of input (1) -> 14th bit of output 
    
    11th bit of input (1) -> 15th bit of output 
    
    13th bit of input (1) -> 16th bit of output 
    
      
    
    Resulting permuted output block (Binary): 0111100101100111 
    
    Resulting permuted output block (Hex): 0x7967  
    
        Permuted Block: 0x7967 
    
        XOR with Subkey: 
    
        Subkey 1 = 0xABCD 
    
        XOR 0x7967 with 0xABCD: 
    
    0x7967 XOR 0xABCD = Result (Hex): 0xD2AA, Binary: 1101001010101010 
    
    So, after the first encryption round, the result is 0xD2AA. 
    
    4) Further Encryption Rounds (for Block 1) 
    
    Repeat steps 1–3 for subsequent encryption rounds (using Subkey 2, Subkey 3, Subkey 4) on the modified blocks. 
    
      
    
     
    
    5) Decryption 
    
    To decrypt, we reverse the process: 
    
        XOR with Subkey: 
    
        XOR the ciphertext with the subkey used during the corresponding encryption round. 
    
        Inverse Permutation: 
    
        Apply the inverse of the permutation used during encryption. 
    
        Inverse Substitution: 
    
        Use the inverse S-box to reverse the substitution. 
    
     6) Final Result 
    
    The final decrypted blocks will match the original plaintext, and the result of this decryption process will be the same as the initial input plaintext 
        
# Installation

Clone the repository

    git clone https://github.com/Adam-ZS/Symmetric-Encrypt-Algorithm.git

Navigate into the project folder

    cd Symmetric-Encrypt-Algorithm
Install Enviroment (if not working)

    python -m venv env
    source env/bin/activate


Run the Encrypt.py script to check the encryption and decryption functionality

    python Encrypt.py

![image](https://github.com/user-attachments/assets/2a6d83be-e126-4208-8e2f-5c837de876eb)

To Decrypt
Run

    python Decryption.py
 ![image](https://github.com/user-attachments/assets/bb69a58b-7d24-435e-9fe1-6a9cfcab3b5e)

 

