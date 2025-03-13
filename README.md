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

# Features
Block Cipher: Works with 16-bit data blocks.

Multiple S-Boxes: 10 unique 16-element substitution boxes for added security.

Permutation-Based Security: A carefully designed bit permutation pattern enhances the algorithm's strength.

Subkey Rotation: Key rotation for each encryption round to prevent attacks.

Encryption and Decryption Functions: Both encryption and decryption are supported with inverse transformations.

Python Code: Fully functional Python implementation of the ADCRYPHAD algorithm.

Manual Tracing: Step-by-step demonstration of encryption and decryption using sample data.

Flexibility: Can be easily adapted for different block sizes and key lengths.
