import os

from pypdf import PdfReader

from conftest import RESOURCES_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_pdf():
    pdf_path = os.path.join(RESOURCES_PATH, 'docs-pytest-org-en-latest.pdf')
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)

    assert number_of_pages == 412
    assert 'holger krekel, trainer and consultant, https://merlinux.eu/' in text