from ascii import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_direction():

	while True:
		direction = input("Type 'encrypt' or 'decrypt':\n")
		if direction == 'encrypt' or direction == 'decrypt':
			break
		else:
			continue
	
	return direction

def get_message():
	msg = input("Type your message:\n").lower()
	return msg

def get_shift():
	shift = int(input("Type the shift number:\n"))
	shift = shift % 25

	return shift


def encrypt_decrypt(text, shift_num, direction):
	chars = []
	alphabet_dict = {}

	for i in range(0, len(alphabet)):
		# if alphabet[i] not in alphabet_dict:
		if direction == 'decrypt':
			if i - shift_num in range(-len(alphabet), len(alphabet)):
				alphabet_dict[alphabet[i]] = i - shift_num
			else:
				alphabet_dict[alphabet[i]] = (len(alphabet) - i) - shift_num

		else:
			if i + shift_num in range(-len(alphabet), len(alphabet)):
				alphabet_dict[alphabet[i]] = i + shift_num
			else:
				alphabet_dict[alphabet[i]] = 0 + shift_num - (len(alphabet) - i)

	for char in text:
		if char not in alphabet_dict:
			chars.append(char)
		else:
			chars.append(alphabet[alphabet_dict[char]])
	
	return_text = "".join(chars)

	print(f"Message: {return_text}")
	return return_text

def restart():
	again = input("Type 'yes' if you want to go again, otherwise type 'no' ")
	if again == 'yes':
		start_caesars_cipher()
	else:
		print("Goodbye and good luck!")
		return

def start_caesars_cipher():
	direction = get_direction()
	message = get_message() 
	shift = get_shift()

	encrypt_decrypt(message, shift, direction)

	restart()

print(logo)
start_caesars_cipher()
