import cv2
import sys
from yolo import YOLO
from video_capture import VideoCapture

def main(video_source="C:/Users/mateo/OneDrive/Escritorio/Projects/DeteccionDeObjetos/objectdetection/data/raw/trafico.mp4"):
    weights = "C:/Users/mateo/OneDrive/Escritorio/Projects/DeteccionDeObjetos/objectdetection/models/yolov4-tiny.weights"
    config = "C:/Users/mateo/OneDrive/Escritorio/Projects/DeteccionDeObjetos/objectdetection/models/yolov4-tiny.cfg"
    coco = "C:/Users/mateo/OneDrive/Escritorio/Projects/DeteccionDeObjetos/objectdetection/models/coco.names"

    # Inicializar YOLO y la captura de video
    yolo = YOLO(weights, config, coco)
    video_capture = VideoCapture(video_source)

    # Definir la posición de la línea de conteo
    line_position = 300  # Ajusta esta posición según la ubicación en tu video

    while True:
        # Leer el fotograma de la cámara o video
        frame = video_capture.read_frame()
        if frame is None:
            break

        # Detectar objetos en el fotograma
        boxes, confidences, class_ids, indexes = yolo.detect_objects(frame)

        # Dibujar las etiquetas en el fotograma y mostrar la cantidad total de autos
        detected_frame = yolo.draw_labels(frame, boxes, confidences, class_ids, indexes)

        # Mostrar el fotograma con objetos detectados
        cv2.imshow('Object Detection', detected_frame)

        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar la captura de video y cerrar las ventanas
    video_capture.release()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])  # Pasar el archivo de video si se proporciona
    else:
        main()  # Usar la cámara web por defecto