

def encrypt():
	text_to_encypt = input("Enter the text u wanna encrypt : ")
	#The key can any string you like but it should be less that the text_to_encrypt in length
	key = input("Enter the key to ")
	#empty string created to store the encypted characters in the for loop below
	encrypted_text = ""
	#Iterating through the characters and excrypting them
	for i in range(len(text_to_encypt)):
		text = text_to_encypt[i]
		key_to_encrypt = key[i%len(key)]
		#This is where the XOR operation takes place and ^ is the xor operator
		encrypted_text += chr(ord(text) ^ ord(key_to_encrypt))
	#a lot of unncessary print statements in between just to make the terminal look a little better and clean!
	print()
	print(encrypted_text)
	print()
	#The encrypted text is stored in a text file named crypt.txt
	with open('crypt.txt','w') as f:
		f.write(encrypted_text)
	print("Writing to the file complete bro ---- >")
	print()
	#here the encrypted string is converted into a hex value.
	print(f"The hex value of the encrypted text is ---- > {encrypted_text.encode('utf-8').hex()}")




#This decyptor function operates in the same way as the encyptor but in a reverse order
def decryptor():
	#Here you first have to enter the key to decrypt the data
	key = input("Enter the key to decrypt : ")
	#it opens the crypt.txt file and reads its content where the encrypted data was stored
	with open('crypt.txt','r') as f:
		content = f.read()
		#you can remove this print statement if u want to
		print(content)
		#an empty string where the decrypted data will be stored
		decrypted=""
		for i in range(len(content)):
			text_to_decrypt = content[i]
			key_to_decrypt = key[i%len(key)]
			#The xor operation on the encrypted data with same key will give u the actual data,soo no brainer!
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
