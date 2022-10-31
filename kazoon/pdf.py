import os


def pdf_merger(pdf_files_path, output_name):
    """
    Merge pdf files to one pdf file.

    Arguments:
        pdf_files_path: Path where all pdf files are located.
        output_name: Name of output pdf file.

    Return:
        None
    """
    from PyPDF2 import PdfMerger
    merger = PdfMerger()
    pdf_files = os.listdir(pdf_files_path)
    for pdf_file in pdf_files:
        merger.append(pdf_files_path + "/" + pdf_file)

    merger.write(f"{output_name}.pdf")
    merger.close()
