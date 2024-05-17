# YOLOv4-Tiny Object Detection

Este proyecto utiliza YOLOv4-Tiny para la detección en tiempo real de varios objetos, específicamente vehículos y señales de tráfico en video en tiempo real o en archivos de video pregrabados.

## Requisitos

1. Python 3.x
2. OpenCV 4.x
3. Numpy

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/yolov4-tiny-detection.git
   cd yolov4-tiny-detection

2. Instala las dependencias:
  ```bash
   pip install -r requirements.txt

3. Descarga los archivos de configuración y pesos de YOLOv4-Tiny:
  ```bash
  wget https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg
  wget https://pjreddie.com/media/files/yolov4-tiny.weights
  wget https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names

4. Coloca los archivos descargados (yolov4-tiny.cfg, yolov4-tiny.weights, coco.names) en la carpeta objectdetection/models/ del proyecto.

## Uso
Detección en tiempo real con videos de transito, camara web, etc-
Para ejecutar la detección de objetos en tiempo real usando el video predeterminado, simplemente ejecuta:

  ```bash
  python yolov4_tiny_detection/main.py
  
## Descripción de los archivos
objectdetection/yolo.py
Este archivo contiene la clase YOLO que se encarga de cargar el modelo, procesar las imágenes y detectar los objetos. La clase también mantiene un registro de todos los objetos detectados.

objectdetection/video_capture.py
Este archivo contiene la clase VideoCapture que abstrae la captura de video desde una cámara web o un archivo de video. Proporciona métodos para leer los fotogramas y liberar los recursos.

yolov4_tiny_detection/main.py
Este es el archivo principal que orquesta la captura de video y la detección de objetos. Lee los fotogramas del video, utiliza el modelo YOLO para detectar objetos y muestra los resultados en tiempo real.

Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún problema o tienes una mejora, por favor abre un issue o un pull request.

Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

¡Gracias por usar este proyecto de detección de objetos con YOLOv4-Tiny!
