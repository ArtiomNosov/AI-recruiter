from pdfminer.high_level import extract_text
from docx import Document
import subprocess

def extract_text_from_file(file_path):
    """Извлекает текст из файлов PDF, DOCX и DOC"""
    try:
        if file_path.lower().endswith('.pdf'):
            return extract_text(file_path)
        elif file_path.lower().endswith('.docx'):
            doc = Document(file_path)
            return "\n".join([para.text for para in doc.paragraphs])
        elif file_path.lower().endswith('.doc'):
            return extract_doc_text(file_path) or "[Не удалось извлечь текст из .doc файла]"
        else:
            return None
    except Exception as e:
        return f"Ошибка при извлечении текста: {str(e)}"

def extract_doc_text(file_path):
    """Извлекает текст из старых .doc файлов с помощью antiword"""
    try:
        result = subprocess.run(['antiword', file_path], 
                              capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else None
    except:
        return None