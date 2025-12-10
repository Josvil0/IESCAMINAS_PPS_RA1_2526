# tests/test_extractor_metadatos.py
# Pruebas unitarias para el extractor de metadatos
# Uso: python test/test_extractor_metadatos.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from extractor_metadatos import extraer_metadatos  # Importamos la función principal a probar

# Carpeta temporal donde se crearán los archivos de prueba.
RUTA_TEST = "tests/archivos_prueba"

class TestExtractorMetadatos(unittest.TestCase):
    """
    Clase de pruebas unitarias para verificar la función principal extraer_metadatos.
    Utiliza el método setUp para crear archivos dummy y garantizar un entorno de prueba controlado.
    """

    def setUp(self):
        """
        Se ejecuta ANTES de cada prueba.
        Crea los archivos mínimos necesarios para que las pruebas funcionen sin depender
        de archivos preexistentes.
        """
        # Crear carpeta temporal si no existe
        os.makedirs(RUTA_TEST, exist_ok=True)

        # 1. Crear archivo TXT (archivo no soportado, sirve para probar la nota)
        with open(os.path.join(RUTA_TEST, "archivo.txt"), "w") as f:
            f.write("Hola mundo")

        # 2. Crear PDF mínimo usando PyPDF2
        from PyPDF2 import PdfWriter
        pdf_path = os.path.join(RUTA_TEST, "documento.pdf")
        writer = PdfWriter()
        writer.add_blank_page(width=72, height=72)  # PDF válido con 1 página en blanco
        with open(pdf_path, "wb") as f:
            writer.write(f)

        # 3. Crear DOCX mínimo usando python-docx
        from docx import Document
        doc = Document()
        doc.add_paragraph("Hola")  # Contenido mínimo
        doc.save(os.path.join(RUTA_TEST, "documento.docx"))

        # 4. Crear imagen mínima usando PIL
        from PIL import Image
        img = Image.new('RGB', (10, 10), color='red')
        img.save(os.path.join(RUTA_TEST, "imagen.jpg"))

    # --- Nota: No eliminamos archivos, se dejan en la carpeta Tests ---

    def test_pdf_metadatos(self):
        """Prueba que extraer metadatos de PDF funciona y contiene info del sistema"""
        ruta = os.path.join(RUTA_TEST, "documento.pdf")
        resultado = extraer_metadatos(ruta)
        self.assertIn("pdf", resultado)
        self.assertIn("sistema_archivos", resultado)

    def test_docx_metadatos(self):
        """Prueba que extraer metadatos de DOCX funciona y contiene info del sistema"""
        ruta = os.path.join(RUTA_TEST, "documento.docx")
        resultado = extraer_metadatos(ruta)
        self.assertIn("docx", resultado)
        self.assertIn("sistema_archivos", resultado)

    def test_imagen_metadatos(self):
        """Prueba que extraer metadatos de imagen funciona y contiene info del sistema"""
        ruta = os.path.join(RUTA_TEST, "imagen.jpg")
        resultado = extraer_metadatos(ruta)
        self.assertIn("imagen", resultado)
        self.assertIn("sistema_archivos", resultado)

    def test_archivo_sin_extractor(self):
        """Prueba que un archivo no soportado devuelve la clave 'nota' y info del sistema"""
        ruta = os.path.join(RUTA_TEST, "archivo.txt")
        resultado = extraer_metadatos(ruta)
        self.assertIn("nota", resultado)
        self.assertIn("sistema_archivos", resultado)

if __name__ == "__main__":
    # Ejecuta todas las pruebas unitarias
    unittest.main()
