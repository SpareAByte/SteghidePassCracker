"""Steghide pass cracker"""
import subprocess

#wordlist
list_path = '{wordlist}'  

with open(list_path, 'r', encoding='utf=8') as file:
    for line in file:
        
        passphrase = line.strip()
        
        steg_cmd = subprocess.run(['steghide', 'info', '</your/path/to/img.jpeg>', '-p', passphrase], capture_output=True, text=True)
        
        if 'steghide: could not open the file "4.jpg".' in steg_cmd.stderr:
            print(f'Passphrase: {passphrase} incorrect')
            continue
        else:
            print(f'Passphrase found: {passphrase}')
            break
