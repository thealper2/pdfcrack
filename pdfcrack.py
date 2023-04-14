import pikepdf
import sys
import colorama
import argparse
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def crack_pdf(pdf, wordlist):
	try:
		with open(wordlists) as file:
			content = file.read()
			passwords = content.splitlines()

		for password in passwords:
			try:
				with pikepdf.open(pdf_file, password=password) as pdf:
					print(f"{Fore.GREEN}[+] Password Found: {Fore.RESET}", password)
					exit()

			except pikepdf._qpdf.PasswordError:
					continue

			print(f"{Fore.RED}[-] Password not found. {Fore.RESET}")

	except Exception as e:
		print(f"{Fore.RED}[!] Error: {Fore.RESET}", e)

argument_parser = argparse.ArgumentParser(description='pdf cracker')
argument_parser.add_argument("-f", required=True, type=str, help='PDF File')
argument_parser.add_argument("-w", required=True, type=str, help='Wordlist File')
args = argument_parser.parse_args()

crack_pdf(args.f, args.w)
