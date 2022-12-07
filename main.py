# Description: Scraping off metadata and encrypting PDF files from a source directory
# Author: Predrag Petrovic <me@predrag.dev>

from PyPDF2 import PdfReader, PdfWriter
import os, getpass, sys, hashlib
from colorama import Fore, Back, Style

scraped = {"/Author": "PDF Scraper", 
    "/Title": "PDF Scraper",
    "/Subject": "PDF Scraper",
    "/Creator": "PDF Scraper",
    "/Producer": "PDF Scraper"}

def encryptPdf(src_dir, pwd, dst_dir):
    for filename in os.listdir(src_dir):
        if filename.endswith('.pdf'):
            try:
                reader = PdfReader(src_dir + '/' + filename)
                print(Fore.RED + Back.BLACK + Style.BRIGHT + 'Encrypting: ' + src_dir + '/' + filename)
                writer = PdfWriter(dst_dir + '/' + filename)
                for page in reader.pages:
                    writer.add_page(page)
                writer.encrypt(pwd)
                with open(dst_dir + '/' + filename, 'wb') as f:
                    writer.write(f)
                    print(Fore.GREEN + Back.BLACK + Style.BRIGHT + 'Encrypted: ' + dst_dir + '/' + filename)
            except Exception as e:
                print(Fore.RED + Back.BLACK + Style.BRIGHT + 'Error: ' + str(e))

def getFileHash(filename):
    # create sha256 hash of the file
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def scrapeMetadata(src_dir):
    # remove all metadata from PDF files
    for filename in os.listdir(src_dir):
        if filename.endswith('.pdf'):
            try:
                reader = PdfReader(src_dir + '/' + filename)
                print(Fore.RED + Back.BLACK + Style.BRIGHT + 'Scraping metadata: ' + src_dir + '/' + filename)
                writer = PdfWriter()
                writer.appendPagesFromReader(reader)
                writer.add_metadata(scraped)
                with open(src_dir + '/' + filename, "wb") as f:
                    writer.write(f)
                    newfile = getFileHash(src_dir + '/' + filename)
                    # rename a file
                    os.rename(src_dir + '/' + filename, src_dir + '/' + newfile + '.pdf')
                    print(Fore.GREEN + Back.BLACK + Style.BRIGHT + 'Scraped metadata from previous file and renaming: ' + src_dir + '/' + newfile + '.pdf')
            except Exception as e:
                print(Fore.RED + Back.BLACK + Style.BRIGHT + 'Error: ' + str(e))

def main():
    
    src_dir = input('Enter source directory: ')

    # check if directory exists
    if not os.path.exists(src_dir):
        print(Fore.RED + Back.BLACK + Style.BRIGHT + 'Directory does not exist: ' + src_dir)
        sys.exit(1)
    
    dst_dir = input('Enter destination directory: ')
    # check if directory exists
    if not os.path.exists(dst_dir):
        # create the directory
        print(Fore.RED + Back.BLACK + Style.BRIGHT + 'Destination directory does not exist: ' + dst_dir)
        try:
            os.makedirs(dst_dir)
            print(Fore.GREEN + Back.BLACK + Style.BRIGHT + 'Created destination directory: ' + dst_dir)
        except Exception as e:
            print(Fore.RED + Back.BLACK + Style.BRIGHT + 'Error: ' + str(e))
            sys.exit(1)

    pwd = getpass.getpass('Enter password: ')
    scrapeMetadata(src_dir)
    encryptPdf(src_dir, pwd, dst_dir)

if __name__ == "__main__":
    main()