import passlib
import codecs
import pyperclip



def encrypt():
	text_to_encypt = input("Enter the text u wanna encrypt : ")
	key = input("Enter the key to ")
	encrypted_text = ""
	for i in range(len(text_to_encypt)):
		text = text_to_encypt[i]
		key_to_encrypt = key[i%len(key)]

		encrypted_text += chr(ord(text) ^ ord(key_to_encrypt))
	print()
	print(encrypted_text)
	print()
	with open('crypt.txt','w') as f:
		f.write(encrypted_text)
	print("Writing to the file complete bro ---- >")
	print()
	#pyperclip.copy(encrypted_text)
	print(f"The hex value of the encrypted text is ---- > {encrypted_text.encode('utf-8').hex()}")




def decryptor():
	key = input("Enter the key to decrypt : ")
	with open('crypt.txt','r') as f:
		content = f.read()

		print(content)
		decrypted=""
		for i in range(len(content)):
			text_to_decrypt = content[i]
			key_to_decrypt = key[i%len(key)]
			decrypted += chr(ord(text_to_decrypt)^ord(key_to_decrypt))
		print(decrypted)


def main():
	while True:
		inp = input("Do u wanna encrypt(e) Decrypt(d) Quit(q) : ")
		if inp == 'q':
			break
		elif inp == 'e':
			encrypt()
		elif inp == 'd':
			decryptor()


if __name__ == '__main__':
	main()