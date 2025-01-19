import base64

def extract_extra_bits(encoded_str):
    # Base64 characters to their 6-bit binary values mapping
    base64_map = {c: bin(i)[2:].zfill(6) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")}
    
    # Decoding the base64 string to binary
    binary_str = ''.join(base64_map[char] for char in encoded_str if char in base64_map)

    # Splitting the binary string into 8-bit chunks
    eight_bit_chunks = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]

    # Calculating the length of the extra bits
    remainder = len(binary_str) % 8

    # Extracting the extra bits
    extra_bits = binary_str[-remainder:] if remainder else '00000000'

    return extra_bits

# Example usage
encoded_str = "SSdtIFBob2VuaXh="
extra_bits = extract_extra_bits(encoded_str)
print(f"Extra bits for '{encoded_str}': {extra_bits}")

