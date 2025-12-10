# 💻 Script de Información del Sistema (Bash Multiplataforma)

## 📝 Descripción del Proyecto

Este proyecto consiste en un **script escrito en Bash** (`info_sistema.sh`) cuyo objetivo es mostrar, en **un único mensaje por consola**, información esencial del sistema desde el que se ejecuta.

El script está diseñado para ser multiplataforma y obtiene los siguientes datos:

* ✅ La **dirección MAC** del equipo.
* ✅ El **sistema operativo** concreto (incluyendo la versión de Linux o macOS).
* ✅ El **nombre del equipo (hostname)**.
* ✅ El **usuario** que ha ejecutado el script.
* *Información adicional como valor añadido.*

Toda la información se presenta de forma clara y legible en una sola salida por consola, cumpliendo el requisito del enunciado.

***

## ⚙️ Requisitos y Compatibilidad

El script **requiere el intérprete Bash** para funcionar.

### Sistemas Compatibles

| Sistema | Compatible | Método de Ejecución |
| :--- | :--- | :--- |
| **Linux** | ✅ | Bash nativo. |
| **macOS** | ✅ | Bash nativo. |
| **Windows** | ✅ | Git Bash o WSL (Windows Subsystem for Linux). |
| **Windows (CMD / PowerShell)** | ❌ | No soporta Bash sin herramientas externas. |

> **Nota importante:**
> Windows no incluye Bash de forma nativa. Para ejecutar este script en Windows es necesario usar **Git Bash** o **WSL**, que son los métodos estándar y oficialmente soportados para ejecutar scripts Bash en dicho sistema operativo.

***

## 🚀 Instalación y Uso del Script

### A. Instalación en Windows (Git Bash)

1.  Descargar e instalar **Git para Windows**:
    ```
    [https://git-scm.com/download/win](https://git-scm.com/download/win)
    ```
2.  Durante la instalación, asegurarse de que el componente **Git Bash** esté habilitado.
3.  Abrir **Git Bash** y navegar a la carpeta donde se encuentra el script.

### B. Instalación en Windows (WSL)

1.  Ejecutar en PowerShell como administrador:
    ```powershell
    wsl --install
    ```
2.  Reiniciar el equipo.
3.  Abrir una terminal Linux (Ubuntu u otra) y ejecutar el script desde allí.

### C. Uso General

Para ejecutar el script en cualquier entorno (Linux / macOS / WSL):

1.  **Dar permisos de ejecución:**
    ```bash
    chmod +x info_sistema.sh
    ```
2.  **Ejecutar:**
    ```bash
    ./info_sistema.sh
    ```

En Windows con **Git Bash**, también puede ser necesario ejecutarlo explícitamente:
```bash
bash info_sistema.sh