import numpy as np
import cv2
import os
import pandas as pd
from skimage.feature import graycomatrix
from skimage.feature import graycoprops
from skimage import img_as_ubyte

def apply_second_order_ops_to_img(image, filename) -> dict:
    # Convertir la imagen a un tipo adecuado para GLCM
    image = img_as_ubyte(image)

    # Calcular la matriz de co-ocurrencia con un desplazamiento de 1 píxel en dirección horizontal
    glcm = graycomatrix(image, distances=[1], angles=[0], symmetric=True, normed=True)

    # 1. Contraste
    contrast = graycoprops(glcm, prop='contrast').item()

    # 2. Homogeneidad
    homogeneity = graycoprops(glcm, prop='homogeneity').item()

    # 3. Disimilitud
    dissimilarity = graycoprops(glcm, prop='dissimilarity').item()

    # 4. Energía
    energy = graycoprops(glcm, prop='energy').item()

    # 5. Correlación
    correlation = graycoprops(glcm, prop='correlation').item()

    # 6. Media de la GLCM
    mean_glcm = np.mean(glcm)

    # 7. Desviación estándar de la GLCM
    std_dev_glcm = np.std(glcm)

    # 8. Entropía de la GLCM
    # Calcular entropía de la GLCM (una aproximación simple)
    glcm_flat = glcm.flatten()
    glcm_flat = glcm_flat[glcm_flat > 0]  # Eliminar ceros para evitar log(0)
    entropy_glcm = -np.sum(glcm_flat * np.log(glcm_flat))

    # Mostrar resultados
    print(f"Nombre: {filename}")
    print(f"Contraste: {contrast}")
    print(f"Homogeneidad: {homogeneity}")
    print(f"Disimilitud: {dissimilarity}")
    print(f"Energía: {energy}")
    print(f"Correlación: {correlation}")
    print(f"Media de la GLCM: {mean_glcm}")
    print(f"Desviación Estándar de la GLCM: {std_dev_glcm}")
    print(f"Entropía de la GLCM: {entropy_glcm}")

    # Retornar los resultados en un diccionario
    return {
        "Imagen": filename,
        "Contraste": contrast,
        "Homogeneidad": homogeneity,
        "Disimilitud": dissimilarity,
        "Energía": energy,
        "Correlación": correlation,
        "Media de la GLCM": mean_glcm,
        "Desviación Estándar de la GLCM": std_dev_glcm,
        "Entropía de la GLCM": entropy_glcm
    }

def load_images(directorio = "src/img/texturas") -> list:
    # Obtener lista de archivos en el directorio
    archivos = os.listdir(directorio)

    # Filtrar solo imágenes (ej: jpg, png, jpeg)
    extensiones_validas = [".jpg", ".jpeg", ".png"]
    imagenes = [imagen for imagen in archivos if os.path.splitext(imagen)[1].lower() in extensiones_validas]

    # Leer las imágenes con cv2
    imagenes_cargadas = []
    for nombre in imagenes:
        ruta = os.path.join(directorio, nombre)
        img = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
        if img is not None:  # Verificamos que se haya leído correctamente
            imagenes_cargadas.append((nombre, img))
        else:
            print(f"No se pudo leer: {ruta}")

    print(f"Se cargaron {len(imagenes_cargadas)} imágenes.")
    return imagenes_cargadas

def apply_second_order_ops_to_all_imgs_in_dir(directorio = "src/img/texturas") -> list:
    # Cargar imágenes del directorio
    imagenes = load_images(directorio)

    # Aplicar las operaciones a cada imagen
    resultados = []
    for i, (nombre, img) in enumerate(imagenes):
        print(f"\nProcesando imagen {i+1}/{len(imagenes)}: {nombre}")
        resultado = apply_second_order_ops_to_img(img, nombre) # Obtener el diccionario de resultados
        resultados.append(resultado) # Guardar el diccionario en la lista
    
    # Retornar la lista de resultados
    return resultados

def save_dicts_to_csv(dicts: list, filename: str):
    # Convertir la lista de diccionarios a un DataFrame de pandas
    df = pd.DataFrame(dicts)

    # Guardar el DataFrame en un archivo CSV
    df.to_csv(filename, index=False, sep="|")
    print(f"\nResultados guardados en {filename}")

if __name__ == "__main__":
    # Aplicar las operaciones a todas las imágenes en el directorio
    resultados = apply_second_order_ops_to_all_imgs_in_dir("src/img/texturas")

    # Guardar los resultados en un archivo CSV
    save_dicts_to_csv(resultados, "src/textures/statistics/taller/resultados_texturas_python.csv")