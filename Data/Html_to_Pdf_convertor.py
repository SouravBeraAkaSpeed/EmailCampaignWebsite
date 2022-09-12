import pdfkit


def Convert(filename, Output_pdf_name):
    try:
        path_wkhtmltopdf = r'..\..\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        pdfkit.from_file(filename, Output_pdf_name, configuration=config)
    except Exception as e:
        pass
