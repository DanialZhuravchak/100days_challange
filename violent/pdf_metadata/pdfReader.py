"""Script to extract metadata from PDF files."""

import PyPDF2
from PyPDF2 import PdfFileReader
import optparse


def printMeta(fileName):
    """Print Metadata about PDF file."""
    with open(fileName, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title
    documentInfo = pdf.getDocumentInfo()

    print("Main MetaData from file")
    print("[+] Name of PDF" + str(pdf))
    print("[+] Information:" +
          str(info) + "Pages:" + str(number_of_pages))
    print("[+] Author " + str(author))
    print("[+] Creator " + str(creator))
    print("[+] Producer " + str(producer))
    print("[+] Subject " + str(subject))
    print("[+] Title " + str(title))
    for metaItem in documentInfo:
        print(f'[+] metaItem: {documentInfo[metaItem]}')


def main():
    """Parse console output Function."""
    parser = optparse.OptionParser('usage %prog"+\
        " -F <PDF file name>')
    parser.add_option("-f", dest='fileName', type="string",
                      help='specify PDF file name')
    (options, _) = parser.parse_args()
    fileName = options.fileName
    if fileName:
        printMeta(fileName)

    else:
        print(parser.usage)
        exit(0)


if __name__ == '__main__':
    main()
