"""Steghide pass cracker"""
import subprocess

# Replace with your wordlist path
list_path = '</your/path/to/wordlist.txt>'  

with open(list_path, 'r', encoding='utf=8') as file:
    for line in file:
        #Cleaning the word for input
        passphrase = line.strip()
        #Calling the steghide command
        steg_cmd = subprocess.run(['steghide', 'info', '</your/path/to/img.jpeg>', '-p', passphrase], capture_output=True, text=True)
        #Output check for the correct passphrase
        if 'steghide: could not open the file "4.jpg".' in steg_cmd.stderr:
            #You could delete this if you don't want you cli to be cluttered
            print(f'Passphrase: {passphrase} incorrect')
            continue
        else:
            print(f'Passphrase found: {passphrase}')
            break
