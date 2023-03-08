from docx import Document
import os

def generateDOCX(name):
    # задаем имя файла
    filename = f"{name}.docx"

    # задаем путь к директории для сохранения файла
    directory = "Documents/"

    # создаем пустой документ
    document = Document()

    # сохраняем документ в заданной директории
    filepath = os.path.join(directory, filename)
    document.save(filepath)


generateDOCX("HelloWorld")
