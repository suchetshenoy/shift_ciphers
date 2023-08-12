#Vigenère cipher encrypter
plain_text = "hello"
key = "hello"#key must be as long as text at least
plain_text = plain_text.lower()
key = key.upper()
encrypted_text = ""
for i in range(len(plain_text)):
  if plain_text[i] in "abcdefghijklmnopqrstuvwxyz":
    encrypted_text += chr(((ord(plain_text[i])-ord("a")+ord(key[i])-ord("A"))%26)+ord("a"))
  else:
    encrypted_word+=plain_text[i]

print(encrypted_text)
