# Here we are importing necessary modules
from pathlib import Path
from zipfile import ZipFile
from tqdm import tqdm

# Entering the path of word list and file to decrypt
word_list = Path(str(input('[0] Word List Path: ')))
zip_file_path = Path(str(input('[1] Zip File Path: ')))


def crack_password():
    
    zip_file = ZipFile(zip_file_path)

   
    n_words = len(list(open(word_list, 'rb')))

    
    print('[2] Total passwords that we are testing:', f'{n_words:,}')

    with open(word_list, 'rb') as wordlist:
        for word in tqdm(wordlist, total=n_words, unit='word'):
            try:
                zip_file.extractall(pwd=word.strip())

            except:
                continue

            else:
                print('\n[+] Password found:', word.decode().strip())
                exit(0)

    print("\n[!] Password not found, try other wordlist.")


if word_list.exists() and zip_file_path.exists():
    crack_password()

else:
    print('[x] An incorrect or non-existent path was entered')
    exit(1)
