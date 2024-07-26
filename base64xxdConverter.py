import base64
import binascii
import argparse

def decode_hex_to_bytes(hex_string):
    """
    Decode a hexadecimal string to bytes.
    :param hex_string: The hexadecimal string.
    :return: The decoded bytes.
    """
    # Remove any whitespace characters
    hex_string = ''.join(hex_string.split())
    
    # Ensure the hex string has an even length
    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string
    
    try:
        return binascii.unhexlify(hex_string)
    except binascii.Error as e:
        print(f"Error decoding hex string: {e}")
        exit(1)

def remove_carriage_returns_and_newlines(input_bytes):
    """
    Remove carriage returns and newlines from the input bytes.
    :param input_bytes: The input bytes.
    :return: The bytes without carriage returns and newlines.
    """
    return input_bytes.replace(b'\r', b'').replace(b'\n', b'')

def decode_base64(encoded_bytes):
    """
    Decode Base64 encoded bytes.
    :param encoded_bytes: The Base64 encoded bytes.
    :return: The decoded bytes.
    """
    try:
        return base64.b64decode(encoded_bytes)
    except (TypeError, binascii.Error) as e:
        print(f"Error decoding Base64: {e}")
        exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process and decode a Base64 encoded file.")
    parser.add_argument('input_filename', help="The input filename containing the Base64 encoded data.")
    parser.add_argument('-o', '--output_filename', default='decoded_output', help="The output filename for the decoded data (default: 'decoded_output').")
    
    args = parser.parse_args()
    
    input_filename = args.input_filename
    output_filename = args.output_filename
    
    try:
        with open(input_filename, "r") as f:
            hex_string = f.read()
    except Exception as e:
        print(f"Error reading file {input_filename}: {e}")
        exit(1)
    
    # Decode the hexadecimal string to bytes
    decoded_bytes = decode_hex_to_bytes(hex_string)
    
    # Remove carriage returns and newlines
    clean_bytes = remove_carriage_returns_and_newlines(decoded_bytes)
    
    # Decode the Base64 string to bytes
    decoded_data = decode_base64(clean_bytes)
    
    # Print the decoded data to the terminal
    print("\nDecoded data:\n")
    print(decoded_data.decode('utf-8', errors='ignore'))
    
    # Write the decoded data to a file
    try:
        with open(output_filename, "wb") as f:
            f.write(decoded_data)
        print(f"\nDecoded data written to {output_filename}")
    except Exception as e:
        print(f"Error writing to file {output_filename}: {e}")
        exit(1)
