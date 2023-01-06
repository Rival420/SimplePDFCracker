import sys
import itertools
import PyPDF2
import argparse

parser = argparse.ArgumentParser(description='Try different combinations of characters as passwords for a PDF file')

# Add the list of characters and password length as arguments
parser.add_argument('characters', help='A string containing the list of characters to use')
parser.add_argument('password_length', type=int, help='The length of the password')
parser.add_argument('pdf_filename', help='The name of the PDF file')

# Parse the command line arguments
args = parser.parse_args()

# Open the PDF file in read-binary mode
with open(args.pdf_filename, 'rb') as file:
  # Create a PDF object
  pdf = PyPDF2.PdfFileReader(file)
  
  # Get all possible combinations of the characters
  combinations = itertools.product(args.characters, repeat=args.password_length)

  # Try each combination as a password for the PDF
  for combination in combinations:
    password = ''.join(map(str, combination))
    if pdf.decrypt(password) == 1:
      # The password was correct and the PDF has been decrypted
      # You can now read the contents of the PDF
      print("[+] Password found: " + password + "\n")
      print("content of pdf: \n")
      print(pdf.getPage(0).extractText())
      break
  else:
    # All of the combinations were incorrect
    print("None of the provided passwords were correct.")
