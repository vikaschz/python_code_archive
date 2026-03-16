"""Create a base class FileReader with read(). Derive TextFileReader and PDFFileReader. Demonstrate polymorphic file reading."""
class FileReader:
    def read(self, path):
        raise NotImplementedError("Subclass must implement read()")

class TextFileReader(FileReader):
    def read(self, path):
        print("Reading text file:", path)
        
        print("Content: Hello from txt")

class PDFFileReader(FileReader):
    def read(self, path):
        print("Reading PDF file:", path)
        # dummy logic
        print("Content: Hello from pdf")

def read_file(reader: FileReader, path: str):
    reader.read(path)

txt_reader = TextFileReader()
pdf_reader = PDFFileReader()

read_file(txt_reader, "notes.txt")
read_file(pdf_reader, "book.pdf")
