import cv2

class VideoCapture:
    def __init__(self, src=0, width=640, height=480):
        """
        Inicializa la captura de video.

        Parámetros:
        src (int o str): Índice de la cámara o ruta del archivo de video.
        width (int): Ancho del video.
        height (int): Alto del video.
        """
        self.cap = cv2.VideoCapture(src)
        if isinstance(src, int):  # Solo ajustar el tamaño si es una cámara
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def read_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
