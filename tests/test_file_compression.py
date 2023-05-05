import os
from conftest import RESOURCES_PATH
from zipfile import ZipFile


def test_pdf_compress():
    pdf_path = os.path.join(RESOURCES_PATH, 'docs-pytest-org-en-latest.pdf')
    zip_path = os.path.join(RESOURCES_PATH, 'test.zip')

    with ZipFile(zip_path, mode='a') as zip_files:
        zip_files.write(pdf_path, os.path.basename(pdf_path))

        assert 'docs-pytest-org-en-latest.pdf' in zip_files.namelist()

def test_xls_compress():
    xls_path = os.path.join(RESOURCES_PATH, 'file_example_XLS_10.xls')
    zip_path = os.path.join(RESOURCES_PATH, 'test.zip')

    with ZipFile(zip_path, mode='a') as zip_files:
        zip_files.write(xls_path, os.path.basename(xls_path))

        assert 'file_example_XLS_10.xls' in zip_files.namelist()

def test_xlsx_compress():
    xlsx_path = os.path.join(RESOURCES_PATH, 'file_example_XLSX_50.xlsx')
    zip_path = os.path.join(RESOURCES_PATH, 'test.zip')

    with ZipFile(zip_path, mode='a') as zip_files:
        zip_files.write(xlsx_path, os.path.basename(xlsx_path))

        assert 'file_example_XLSX_50.xlsx' in zip_files.namelist()