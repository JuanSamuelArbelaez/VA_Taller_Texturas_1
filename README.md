# Actividad: Clasificación de Imágenes Basada en Texturas

## Juan Samuel Arbeláez Rocha

## Descripción
Este proyecto aplica algoritmos de **extracción de características de textura** en imágenes digitales (GLCM, LBP, filtros de Gabor, Wavelet), utilizando **Python** y **MATLAB**, para construir una base de datos de características y compararlas de manera matemática (sin clasificador).

Se incluyen:
- Imágenes utilizadas (9 acercamientos de pan y 3 de esponjas en escala de grises).
- Archivos Python (`.py`) y scripts MATLAB (`.m`).
- Resultados en hojas de cálculo:
  - `src\textures\statistics\taller\resultados_texturas_python.csv`  
  - `src\textures\statistics\taller\resultados_texturas_matlab.csvv`
- Archivo de **conclusiones.txt** con observaciones comparativas.

## Objetivo General
Aplicar algoritmos de extracción de características de textura en imágenes digitales para reconocer patrones y generar una base de datos de análisis.

## Objetivos Específicos
- Comprender la importancia del análisis de texturas en visión artificial.  
- Implementar algoritmos de extracción de características (GLCM, LBP, Gabor, Wavelet).  
- Construir vectores de características a partir de imágenes de texturas.  
- Comparar los resultados obtenidos en **Python** y **MATLAB**.  

## Instrucciones Básicas
1. Convertir imágenes a escala de grises.  
2. Aplicar los algoritmos de análisis de textura.  
3. Extraer los vectores de características en ambos entornos.  
4. Guardar resultados en `.csv`.  
5. Analizar comparativamente los resultados.  

## Requisitos (Python)
Crear entorno virtual, activarlo e instalar dependencias:

```bash
# Crear venv
python -m venv .venv

# Activar venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
