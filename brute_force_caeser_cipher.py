#code for brute forcing a caeser cipher and print any time a word appears
input_filename = "input.txt"
word = "hello"
try:
    with open(input_filename, "r") as input_file:
        text = input_file.read()

except FileNotFoundError:
    print("File not found.")
    
if text:
  for i in range(256):
    shifted_text = ""
    for char in text:
        shifted_char_value = (ord(char) + i)
        if shifted_char_value > 255:
            shifted_char_value -= 255
        shifted_char = chr(shifted_char_value)  # Use chr() to convert ASCII value to character
        shifted_text += shifted_char
    if word in shifted_text:
      print(i, shifted_text)
