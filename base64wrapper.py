import textwrap
import base64

def reformat_base64(encoded_string, line_length=76):
    """
    Reformat a Base64 encoded string into lines of specified length.

    :param encoded_string: The original Base64 encoded string.
    :param line_length: The length of each line in the reformatted string.
    :return: The reformatted Base64 string.
    """
    return "\n".join(textwrap.wrap(encoded_string, line_length))

if __name__ == "__main__":
    print("Enter the Base64 encoded string (press Enter twice to finish):")
    base64_input = ""
    while True:
        line = input()
        if line:
            base64_input += line
        else:
            break
    
    # Validate if the input is a valid Base64 string
    try:
        base64.b64decode(base64_input, validate=True)
    except (TypeError, binascii.Error):
        print("Invalid Base64 input. Exiting.")
        exit(1)
    
    # Get the desired line length
    try:
        line_length = int(input("Enter the line length (default is 76): "))
    except ValueError:
        line_length = 76

    # Reformat the Base64 string
    formatted_base64 = reformat_base64(base64_input, line_length)

    # Print the reformatted Base64 string
    print("\nReformatted Base64 string:\n")
    print(formatted_base64)
    
    # Decode the Base64 string and write to a file
    try:
        decoded_data = base64.b64decode(base64_input)
    except Exception as e:
        print(f"Error decoding Base64: {e}")
        exit(1)
    
    output_filename = input("\nEnter the output file name (default is 'decoded_output'): ") or "decoded_output"
    try:
        with open(output_filename, "wb") as f:
            f.write(decoded_data)
        print(f"\nDecoded data written to {output_filename}")
    except Exception as e:
        print(f"Error writing to file {output_filename}: {e}")
        exit(1)
