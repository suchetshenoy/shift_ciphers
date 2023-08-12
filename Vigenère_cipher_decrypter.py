#Vigenère cipher decrypter
encrypted_text = "hello"
key = "hello"#key must be as long as text at least
plain_text = plain_text.lower()
key = key.upper()
decrypted_text = ""
for i in range(len(encrypted_text)):
  if plain_text[i] in "abcdefghijklmnopqrstuvwxyz":
    decrypted_text += chr(((ord(encrypted_text[i])-ord("a")+ord(key[i])-ord("A"))%26)+ord("a"))
  else:
    decrypted_word+=plain_text[i]

print(decrypted_text)
