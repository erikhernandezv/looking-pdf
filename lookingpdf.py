import pdfplumber

with pdfplumber.open("JHDSS_CourseDependencies.pdf") as pdf:
    first_page = pdf.pages[0]
    print(first_page.chars[0])
    print("\n")
    print(first_page.extract_texts())
