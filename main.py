from kavy.core.kavy import Kavy
api_key = ""

if __name__ == "__main__":
    kavy_instance = Kavy(api_key)

    print("Arigato!")

    # Use a URL as an example
    url = "https://www.tanjiro.tech/"
    kavy_instance.train_on_url(url)

    response_url = kavy_instance.generate_response("What is on the website?")
    print("Response from URL:", response_url)

    # Use a PDF file path as an example
    # pdf_file_path = "path/to/your/pdf/file.pdf"
    # kavy_instance.train_on_pdf(pdf_file_path)

    # response_pdf = kavy_instance.generate_response("What is the main idea in the PDF?")
    # print("Response from PDF:", response_pdf)

    # # Use a Word file path as an example
    # word_file_path = "path/to/your/word/file.docx"
    # kavy_instance.train_on_word(word_file_path)

    # response_word = kavy_instance.generate_response("What is the main idea in the Word document?")
    # print("Response from Word:", response_word)

    # # Use a TXT file path as an example
    # txt_file_path = "data/txt_data/input.txt"
    # kavy_instance.train_on_txt(txt_file_path)

    # response_txt = kavy_instance.generate_response("What is in the text document?")
    # print("Response from TXT:", response_txt)
