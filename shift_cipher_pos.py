#code for a shift cipher based on the position of char in text file
input_filename = "input.txt"
try:
    with open(input_filename, "r") as input_file:
        text = input_file.read()

except FileNotFoundError:
    print("File not found.")

if text:
    shifted_text = ""
    for i in range(len(text)):
        shifted_char_value = (ord(text[i]) + i)
        while shifted_char_value > 255:
            shifted_char_value -= 255
        shifted_char = chr(shifted_char_value)  # Use chr() to convert ASCII value to character
        shifted_text += shifted_char
  print(shifted_text)
