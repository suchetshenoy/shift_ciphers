#code for a simple caeser cipher shift
input_filename = "input.txt"
output_filename = "output.txt"
shift_amount = 60

try:
    with open(input_filename, "r") as input_file:
        text = input_file.read()

    shifted_text = ""
    for char in text:
        shifted_char_value = (ord(char) + shift_amount)
        while shifted_char_value > 255:
            shifted_char_value -= 255
        while shifted_char_value < 0:
            shifted_char_value += 255
        shifted_char = chr(shifted_char_value)  # Use chr() to convert ASCII value to character
        shifted_text += shifted_char

    with open(output_filename, "w") as output_file:
        output_file.write(shifted_text)
    print("Shifted text saved to", output_filename)

except FileNotFoundError:
    print("File not found.")
