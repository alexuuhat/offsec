import base64

def convert_to_base64(input_string):
    # Remove whitespace and carriage returns
    cleaned_string = input_string.replace(" ", "").replace("\r", "").replace("\n", "")

    # Encode cleaned string to base64
    base64_encoded = base64.b64encode(cleaned_string.encode()).decode()
    
    return base64_encoded

# Example usage:
if __name__ == "__main__":
    input_lines = []
    
    print("Enter the string to convert to base64:")
    
    # Read input until an empty line is encountered
    while True:
        line = input().strip()
        if line:
            input_lines.append(line)
        else:
            break
    
    input_string = "\n".join(input_lines)
    
    # Convert to base64
    encoded_string = convert_to_base64(input_string)
    
    # Print the encoded string
    print("\nBase64 Encoded:\n" + encoded_string + "\n")
