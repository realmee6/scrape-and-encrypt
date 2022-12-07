# Scrape and Encrypt

Note: This script is only tested on Mac OS and Linux.

This is a small script that I use for scraping all metadata from a PDF file before password protecting the PDF file.

Install prerequisites:
`pip3 install pypdf2 colorama`

How to use the script:
- Provide the source directory.
- Provide the destination directory.
- Input the password for protecting the PDFs.

You can define what metadata will be present in the newly created files by modifying the values in the scraped dictionary.

scraped = {"/Author": "PDF Scraper", 
    "/Title": "PDF Scraper",
    "/Subject": "PDF Scraper",
    "/Creator": "PDF Scraper",
    "/Producer": "PDF Scraper"}
    
What the script does:
- Takes all PDF files from a source directory.
- Replaces all metadata in the PDF with the scraped dictionary defintion.
- Creates a new file with the sha256 value of the PDF file.
- Encrypts the PDF with the supplied password.
