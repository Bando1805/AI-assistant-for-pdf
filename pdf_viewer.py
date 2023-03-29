import PyPDF2
import os

class pdfViewer():
    
    def __init__(self,dictionary) -> None:
        self.dictionary = dictionary
        self.file_paths = [self.dictionary[f'chunk_{i}']['source'] for i in range(len(self.dictionary))]
        self.pages = [int(self.dictionary[f'chunk_{i}']['page']) for i in range(len(self.dictionary))]
        self.visualize_pages()

    def visualize_pages(self):
        file_path = self.file_paths[0]
            # open the PDF file in read binary mode
        with open(file_path, 'rb') as pdf_file:
            # create a PdfFileReader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # create a PdfFileWriter object
            pdf_writer = PyPDF2.PdfWriter()

            for page_num in self.pages:

                # get the page at the specified page number
                pdf_page = pdf_reader.pages[page_num -1]
                # add the page to the writer
                pdf_writer.add_page(pdf_page)

            pdf_name = file_path.split("/")[-1]
        
            # write the writer's content to a new PDF file
            with open(pdf_name, 'wb') as output_file:
                pdf_writer.write(output_file)

            # open the new file in your default PDF viewer
            os.startfile(pdf_name)
    

