from enigma import Enigma


if __name__ == "__main__":

	message = input("Enter your message: ")
	message = Enigma(message)

	print(message)