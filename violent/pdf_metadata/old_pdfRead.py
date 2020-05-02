"""Script to extract metadata from PDF files."""

import pyPdf
import optparse
from pyPdf import PdfFileReader


def printMeta(fileName):
    """Print Metadata about PDF file."""
    pdfFile = PdfFileReader(file(fileName, 'rb'))
    docInfo = pdfFile.getDocumentInfo()
    print("[*] PDF MetaData For:" + str(fileName))
    for metaItem in docInfo:
        print('[+] ' + metaItem + ':' + docInfo[metaItem])


def main():
    parser = optparse.OptionParser('usage %prog"+\
        " -F <PDF file name>')
    parser.add_option("-F", dest='FileName', type='string',
                      help='specify PDF file name')
    (options, args) = parser.parse_args()
    fileName = options.fileName
    if fileName == None:
        print.parser.usage
        exit(0)
    else:
        printMeta(fileName)


if __name__ == '__main__':
    main()
