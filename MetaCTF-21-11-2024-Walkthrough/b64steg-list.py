import base64

def extract_extra_bits(encoded_list):
    # Base64 characters to their 6-bit binary values mapping
    base64_map = {c: bin(i)[2:].zfill(6) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")}
    
    extra_bits = ""
    
    for encoded_str in encoded_list:
        # Decoding the base64 string to binary
        binary_str = ''.join(base64_map[char] for char in encoded_str if char in base64_map)

        # Splitting the binary string into 8-bit chunks
        eight_bit_chunks = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]

        # Calculating the length of the extra bits
        remainder = len(binary_str) % 8

        # Extracting the extra bits and concatenating them
        if remainder:
            extra_bits += binary_str[-remainder:]

    return extra_bits

# Example usage
encoded_list = [
    "VEh=", "QT==", "Tl==", "S5==", "IF==",
    "Wd==", "Tx==", "VY==", "IF==", "SA==",
    "Qd==", "Q1==", "Sx==", "RR==", "Up==",
    "Ie==", "Cs==", "Ct==", "Qh==", "VX==",
    "VN==", "IJ==", "T4==", "Vc==", "Ut==",
    "IN==", "Rt==", "TH==", "Qc==", "R8==",
    "IN==", "Se==", "Ux==", "IN==", "SR==",
    "Ts==", "II==", "Qd==", "Th==", "T3==",
    "VN==", "SI==", "RY==", "Us==", "IF==",
    "Q9==", "QQ==", "U9==", "VF==", "TP==",
    "RU==", "IQ=="
]
extra_bits = extract_extra_bits(encoded_list)
print(f"Concatenated extra bits for the list: {extra_bits}")

