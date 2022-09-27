import random
import string
import sys


def collector():
	included = ''
	dict = {'uppercase alphabets': string.ascii_uppercase, 'lowercase alphabets': string.ascii_lowercase, 'decimal digits': string.digits, 'special characters': string.punctuation, 'whitespace': ' '}

	for keys in dict:
		reply = input(f"Want to include {keys} alphabets: ").lower()
		if reply == 'y':
			included += dict[keys]
			print("Included")
		elif reply == 'n':
			print("Left")
		else:
			print("Invlaid input, left by default")

	return included


def generator(sample_space, length):
	return ''.join(random.choices(sample_space, k = length))


def interface():
	sample_space = collector()
	length = int(input("What length of password is desired? "))

	pswd = generator(sample_space, length)

	print(f"Password Generated: {pswd}")

	return pswd


if __name__ == '__main__':
	if len(sys.argv) == 1:
		interface()
	elif len(sys.argv) == 3:
		print(f'Generated Password: {generator(sys.argv[1], int(sys.argv[2]))}')
	else:
		print('ERROR:INVALID NUMBER OF ARGUMENTS')
