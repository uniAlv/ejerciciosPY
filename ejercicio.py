#imports
import os
import cv2
import shutil
import numpy as np 
from zipfile import ZipFile
from urllib.request import urlretrieve

print("Terminal Ejercicio")
#ejercicios
def ejercicio1():
    origen_path = input("Ingrese la ruta de la imagen de origen: ")
    destino_path = input("Ingrese la ruta de destino para la imagen: ")

    if not os.path.exists(origen_path):
        raise FileNotFoundError(f"Source file not found: {origen_path}")

    destination_dir = os.path.dirname(destino_path)
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    filename, extension = os.path.splitext(os.path.basename(origen_path))

    new_filename = filename
    counter = 1
    while os.path.exists(os.path.join(destination_dir, new_filename + extension)):
        new_filename = f"{filename}_{counter}"
        counter += 1

    destination_file = os.path.join(destination_dir, new_filename + extension)
    with open(origen_path, 'rb') as source_file:
        with open(destination_file, 'wb') as destination_file:
            shutil.copyfileobj(source_file, destination_file)

    return print(f"Imagen copiado: {origen_path} -> {destination_file}")

def ejercicio2():
    image_path = input("ruta de la imagen: ")
    image = cv2.imread(image_path)

    # Verifica si la imagen se cargó correctamente
    if image is None:
        print("Error: No se pudo cargar la imagen. Verifica la ruta.")
    else:
        # Obtén el tamaño de la imagen
        height, width, channels = image.shape  # Desempaqueta altura, ancho y canales

    datos = print("Altura:", height, " ", "Ancho:", width, " ", "Cantidad de canales:", channels)
    return datos

def ejercicio3():
    image_path = input("ruta de la imagen: ")
    opcion = input ("desea seleccionar manualmente las coredenadas y or n: ")
  
    if opcion == "y":
        x1 = int(input("cordenada x1: "))
        y1 = int(input("cordenada y1: "))
        x2 = int(input("cordenada x2: "))
        y2 = int(input("cordenada y2: "))
    else:

        x1, y1 = 50, 50  # Coordenadas del primer punto
        x2, y2 = 200, 200  # Coordenadas del segundo punto

    image = cv2.imread(image_path)
    if image is None:
        print("Error: No se pudo cargar la imagen. Verifica la ruta.")
        return
    # Dibujar un rectángulo negro en las coordenadas indicadas
    color_negro = (0, 0, 0)  # Color negro (en formato BGR)
    grosor = -1  # -1 para rellenar el rectángulo
    cv2.rectangle(image, (x1, y1), (x2, y2), color_negro, grosor)

    # Mostrar la imagen completa en una ventana de OpenCV
    cv2.imshow("Imagen con mancha negra", image)  # Nombre de la ventana y la imagen
    cv2.waitKey(0)  # Esperar a que se presione una tecla para cerrar la ventana
    cv2.destroyAllWindows()  # Cerrar la ventana después de cerrar con una tecla

def ejercicio4():
    image_path = input("ruta de la imagen: ")
    
    image = cv2.imread(image_path)
     # Verificar si la imagen se cargó correctamente
    if image is None:
        print("Error: No se pudo cargar la imagen. Verifica la ruta.")
        return
    
    # Invertir la imagen horizontalmente
    imagen_invertida_horizontal = cv2.flip(image, 1)  # 1 para invertir horizontalmente

    # Invertir la imagen verticalmente
    imagen_invertida_vertical = cv2.flip(image, 0)  # 0 para invertir verticalmente

    # Combinar ambas inversiones para obtener el resultado final
    imagen_invertida_total = cv2.flip(imagen_invertida_horizontal, 0)

    # Mostrar la imagen invertida en una ventana de OpenCV
    cv2.imshow("Imagen invertida", imagen_invertida_total)  # Nombre de la ventana
    cv2.waitKey(0)  # Esperar a que se presione una tecla para cerrar la ventana
    cv2.destroyAllWindows()  # Cerrar la ventana después de esperar una tecla

def ejercicio5():
    image_path = input("ruta de la imagen: ")
    factor_escala = float(input("Introduce el factor de ampliación (por ejemplo, 0.5, 2, 3): "))

    image = cv2.imread(image_path)

    # Verificar si la imagen se cargó correctamente
    if image is None or image.size == 0:
        print("Error: No se pudo cargar la imagen. Verifica la ruta o el archivo.")
        return  # No continuar si la imagen no es válida

    # Obtener las dimensiones originales de la imagen
    height, width = image.shape[:2]  # Solo necesitamos el alto y el ancho

    # Calcular las nuevas dimensiones en función del factor de escalado
    new_width = int(width * factor_escala)
    new_height = int(height * factor_escala)

    # Redimensionar la imagen
    image_escalada = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    # Mostrar la imagen redimensionada
    cv2.imshow("Imagen escalada", image_escalada)  # Nombre de la ventana
    cv2.waitKey(0)  # Esperar a que se presione una tecla para cerrar la ventana
    cv2.destroyAllWindows()  # Cerrar la ventana después de presionar una tecla

def ejercicio6():
    image_path = input("ruta de la imagen: ")
    opcion = input ("desea seleccionar manualmente las coredenadas y or n: ")

    if opcion == "y":
        x1 = int(input("cordenada x1: "))
        y1 = int(input("cordenada y1: "))
        x2 = int(input("cordenada x2: "))
        y2 = int(input("cordenada y2: "))
    else:

        x1, y1 = 100, 250  # Coordenadas del primer punto
        x2, y2 = 500, 500  # Coordenadas del segundo punto

    # Leer la imagen desde la ruta especificada
    image = cv2.imread(image_path)

    # Verificar si la imagen se cargó correctamente
    if image is None or image.size == 0:
        print("Error: No se pudo cargar la imagen. Verifica la ruta o el archivo.")
        return  # No continuar si la imagen no es válida

    # Obtener las dimensiones de la imagen
    height, width = image.shape[:2]  # Alto y ancho de la imagen

    # Mostrar las dimensiones originales en consola
    print(f"Dimensiones originales de la imagen: Alto = {height}, Ancho = {width}")

    # Verificar que las coordenadas de recorte están dentro de los límites de la imagen
    if not (0 <= x1 < width and 0 <= x2 <= width and 0 <= y1 < height and 0 <= y2 <= height):
        print("Error: Las coordenadas de recorte están fuera de los límites de la imagen.")
        return  # No continuar si las coordenadas son inválidas

    # Asegurarse de que x1 < x2 y y1 < y2
    if x1 > x2 or y1 > y2:
        print("Error: Coordenadas de recorte incorrectas. Asegúrate de que x1 < x2 y y1 < y2.")
        return

    # Recortar la imagen usando las coordenadas proporcionadas
    imagen_recortada = image[y1:y2, x1:x2]  # Recorte de la imagen

    # Mostrar la imagen recortada en una ventana de OpenCV
    cv2.imshow("Imagen recortada", imagen_recortada)  # Mostrar en una ventana
    cv2.waitKey(0)  # Esperar a que se presione una tecla para cerrar la ventana
    cv2.destroyAllWindows()  # Cerrar la ventana después de cerrar con una tecla
    return print("holamindo")

def ejercicio7():
    image_path = input("ruta de la imagen: ")
    texto = input("Introduce el texto a escribir en la imagen: ")
    image = cv2.imread(image_path)

    if image is None or image.size == 0:
        print("Error: No se pudo cargar la imagen. Verifica la ruta o el archivo.")
        return  # No continuar si la imagen no es válida
    position = (50, 50)  # Ejemplo: 50 píxeles desde la parte superior izquierda

    font = cv2.FONT_HERSHEY_SIMPLEX  # Tipo de fuente
    font_scale = 1  # Tamaño del texto
    color = (0, 255, 0)  # Color verde en formato BGR
    thickness = 2  # Grosor del texto

    cv2.putText(image, texto, position, font, font_scale, color, thickness, cv2.LINE_AA)

    cv2.imshow("Imagen con texto", image)  # Mostrar la imagen con texto
    cv2.waitKey(0)  # Esperar a que se presione una tecla para cerrar la ventana
    cv2.destroyAllWindows() 

def download_and_unzip(url, save_path):
    print(f"Downloading and extracting assests....", end="")

    # Downloading zip file using urllib package.
    urlretrieve(url, save_path)

    try:
        # Extracting zip file using the zipfile package.q
        with ZipFile(save_path) as z:
            # Extract ZIP file contents in the same directory.
            z.extractall(os.path.split(save_path)[0])

        print("Done")

    except Exception as e:
        print("\nInvalid file.", e)

def ejercicio8():

    # URL = r"https://www.dropbox.com/s/efitgt363ada95a/opencv_bootcamp_assets_12.zip?dl=1"

    # asset_zip_path = os.path.join(os.getcwd(), f"opencv_bootcamp_assets_12.zip")

    # #Download if assest ZIP does not exists.
    # if not os.path.exists(asset_zip_path):
    #     download_and_unzip(URL, asset_zip_path)
    # # ====================================================================


    #s = 0
    #if len(sys.argv) > 1:
    #    s = sys.argv[1]

    frame_save_path = "img"
    if not os.path.exists(frame_save_path):
        os.makedirs(frame_save_path)

    source = cv2.VideoCapture(0)

    win_name = "Camera Preview"
    cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

    net = cv2.dnn.readNetFromCaffe("deploy.prototxt", "res10_300x300_ssd_iter_140000_fp16.caffemodel")
    # Model parameters
    in_width = 300
    in_height = 300
    mean = [104, 117, 123]
    conf_threshold = 0.7

    frame_count = 0  # Contador para nombrar los frames
    while cv2.waitKey(1) != 27:
        has_frame, frame = source.read()
        if not has_frame:
            break
        frame = cv2.flip(frame, 1)
        frame[10:220,10:200] = [255,255,255]
        frame_height = frame.shape[0]
        frame_width = frame.shape[1]

        # Create a 4D blob from a frame.
        blob = cv2.dnn.blobFromImage(frame, 1.0, (in_width, in_height), mean, swapRB=False, crop=False)
        # Run a model
        net.setInput(blob)
        detections = net.forward()

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > conf_threshold:
                x_left_bottom = int(detections[0, 0, i, 3] * frame_width)
                y_left_bottom = int(detections[0, 0, i, 4] * frame_height)
                x_right_top = int(detections[0, 0, i, 5] * frame_width)
                y_right_top = int(detections[0, 0, i, 6] * frame_height)

                cv2.rectangle(frame, (x_left_bottom, y_left_bottom), (x_right_top, y_right_top), (0, 255, 0))
                label = "Confidence: %.4f" % confidence
                label_size, base_line = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)

                cv2.rectangle(
                    frame,
                    (x_left_bottom, y_left_bottom - label_size[1]),
                    (x_left_bottom + label_size[0], y_left_bottom + base_line),
                    (255, 255, 255),
                    cv2.FILLED,
                )
                cv2.putText(frame, label, (x_left_bottom, y_left_bottom), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

        t, _ = net.getPerfProfile()
        label = "Inference time: %.2f ms" % (t * 1000.0 / cv2.getTickFrequency())
        cv2.putText(frame, label, (0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
        cv2.imshow(win_name, frame)

    # Guardar el frame en la carpeta especificada
        # frame_filename = f"{frame_save_path}/frame_{frame_count:04d}.jpg"
        # cv2.imwrite(frame_filename, frame)
        frame_count += 1

        cv2.imshow(win_name, frame)

    source.release()
    cv2.destroyWindow(win_name)
    print("Finito")
   

#seleccion
def opciones(valor):
    menu={
        1: ("Has seleccionado la opción 1.",ejercicio1),
        2: ("Has seleccionado la opción 2.",ejercicio2),
        3: ("Has seleccionado la opción 3.",ejercicio3),
        4: ("Has seleccionado la opción 4.",ejercicio4),
        5: ("Has seleccionado la opción 5.",ejercicio5),
        6: ("Has seleccionado la opción 6.",ejercicio6),
        7: ("Has seleccionado la opción 7.",ejercicio7),
        8: ("Has seleccionado la opción 8.",ejercicio8),
    }
    resultado = menu.get(valor, ("valor incorrecto", None))  # Obtén la opción seleccionada
    if resultado[1]:  # Si la función no es None
        return resultado[0], resultado[1]()  # Ejecuta la función y devuelve el resultado
    else:
        return resultado[0]


def main():
    while True:
        print("\nMenú Principal")
        print("1. Copiar una imagen de una ubicación A, a una ubicación B")
        print("2. Mostrar las características de una imagen")
        print("3. Sobrescribir los pixeles de la imagen con color negro")
        print("4. Invertir imagen")
        print("5. Ampliar o reducir una imagen")
        print("6. Recortar una imagen")
        print("7. Escribir texto en la imagen")
        print("8. Reconocimiento facial")
        print("9. Salir")

        opcion = int(input("Digite un numero: "))

        if opcion == 9:
            print("Saliendo del programa...")
            break

        mensaje = opciones(opcion)
        print(mensaje[0], mensaje[1])  


if __name__ == "__main__":
    main()