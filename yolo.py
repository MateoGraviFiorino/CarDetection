import cv2
import numpy as np

class YOLO:
    def __init__(self, weights, config, classes_file):
        self.net = cv2.dnn.readNet(weights, config)
        self.classes = []
        with open(classes_file, "r") as f:
            self.classes = [line.strip() for line in f.readlines()]
        layer_names = self.net.getLayerNames()
        self.output_layers = [layer_names[i - 1] for i in self.net.getUnconnectedOutLayers()]
        self.classes_to_detect = ["bicycle", "car", "motorbike", "bus", "train", "traffic light", "stop sign"]
        self.colors = self._generate_colors()
        self.detections_log = []

    def _generate_colors(self):
        np.random.seed(42)  # Semilla para colores consistentes
        colors = np.random.uniform(0, 255, size=(len(self.classes_to_detect), 3))
        return {cls: colors[i] for i, cls in enumerate(self.classes_to_detect)}

    def detect_objects(self, img):
        height, width, channels = img.shape

        # Preprocesamiento de la imagen
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.output_layers)

        # Información de detección
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.25 and self.classes[class_id] in self.classes_to_detect:
                    # Objeto detectado
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    # Coordenadas de la caja
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Supresión no máxima para eliminar cajas superpuestas
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.4)

        # Actualizar el registro de detecciones
        self.update_log(class_ids, indexes)

        return boxes, confidences, class_ids, indexes


    def draw_labels(self, img, boxes, confidences, class_ids, indexes):
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(self.classes[class_ids[i]])
                color = self.colors[label]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y + 30), font, 2, color, 2)
        return img


