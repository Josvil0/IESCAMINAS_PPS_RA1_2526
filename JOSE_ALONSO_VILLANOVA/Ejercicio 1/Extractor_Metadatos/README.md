# 📁 Extractor de Metadatos Forenses

## 1. 📝 Descripción del Proyecto

Este proyecto implementa una herramienta en Python (`extractor_metadatos.py`) diseñada para el **análisis de metadatos** en archivos comunes. Su objetivo es extraer la información oculta (metadatos) tanto a nivel de sistema operativo como las propiedades internas de documentos e imágenes, devolviendo el resultado de forma estructurada en formato **JSON** para su fácil procesamiento.

La aplicación soporta la extracción detallada para los siguientes formatos:

* **Imágenes:** `.jpg`, `.jpeg`, `.png` (Extracción de propiedades de la imagen y metadatos EXIF).
* **Documentos:** `.pdf` (Extracción de campos `/Info` como Autor, Creador y Fechas).
* **Documentos Office:** `.docx` (Extracción de propiedades del núcleo como autor, título y fechas de modificación).

***

## 2. ⚙️ Requisitos y Configuración del Entorno

Para ejecutar la aplicación y las pruebas, se requiere **Python 3.x**. Se recomienda encarecidamente el uso de un **entorno virtual (`venv`)** para gestionar las dependencias de forma aislada.

### A. Dependencias del Proyecto

Las librerías necesarias son: `Pillow`, `PyPDF2`, y `python-docx`.

### B. Instalación (Linux/macOS)

1.  **Crear y Activar el Entorno Virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
2.  **Instalar Librerías:**
    ```bash
    pip install Pillow PyPDF2 python-docx
    ```

### C. Instalación (Windows - CMD/PowerShell)

1.  **Crear el Entorno Virtual:**
    ```powershell
    python -m venv venv
    ```
2.  **Activar el Entorno:**
    ```powershell
    # Usando PowerShell
    .\venv\Scripts\Activate.ps1
    
    # Usando Command Prompt (CMD)
    venv\Scripts\activate.bat
    ```
3.  **Instalar Librerías:**
    ```powershell
    pip install Pillow PyPDF2 python-docx
    ```

***

## 3. ▶️ Modo de Uso (Ejecución de la Aplicación)

Una vez activado el entorno virtual, el *script* se ejecuta pasando la **ruta del archivo** a analizar como único argumento.

### Uso General

```bash
(venv) $ python extractor_metadatos.py [RUTA_AL_ARCHIVO]

## 4. 🧪 Pruebas Unitarias

El archivo **`test_extractor_metadatos.py`** contiene un *suite* de pruebas para garantizar que el extractor maneja correctamente los diferentes tipos de archivo y que la lógica es consistente.

### A. Metodología de Pruebas

Las pruebas utilizan el método `setUp` para **generar dinámicamente archivos temporales** (*dummy* files) antes de cada test. Esto asegura que:

1.  Las pruebas son **independientes** de archivos externos.
2.  Se verifica el manejo de **todos los tipos de archivo** soportados, incluso si son mínimos o están vacíos.
3.  Se verifica el manejo de archivos **no soportados** (`.txt`).

### B. Ejecución de las Pruebas

Para ejecutar el *suite* de pruebas, asegúrese de estar en el directorio del proyecto con el entorno virtual activado:

```bash
(venv) $ python test_extractor_metadatos.py
