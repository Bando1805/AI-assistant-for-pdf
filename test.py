import PyPDF2
import tabula

def extract_tables_from_pdf(pdf_file_path):
    # Open the PDF file in read binary mode
    with open(pdf_file_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty list to store the extracted tables
        tables = []

        # Loop through each page in the PDF
        for page_num in range(len(pdf_reader.pages)):
            # Extract the page as a DataFrame using tabula-py
            page_df = tabula.read_pdf(pdf_file_path, pages=page_num+1, pandas_options={'header': None})
            # Check if the page contains any tables
            if len(page_df) > 0:
                # Append the tables to the list
                tables.extend(page_df)

        # Return the list of tables
        return tables


tables = extract_tables_from_pdf('files\REPORT CASE-Academy for Business and Technology (1).pdf')
