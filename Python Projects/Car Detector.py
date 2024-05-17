import cv2
import numpy as np
import random

def detect_objects(image):
    # Load the pre-trained model (for demonstration purposes, you can replace this with a more accurate model)
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # Convert image to blob format
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    # Forward pass through the network
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Process the outputs
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * image.shape[1])
                center_y = int(detection[1] * image.shape[0])
                w = int(detection[2] * image.shape[1])
                h = int(detection[3] * image.shape[0])

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    return boxes, confidences, class_ids

def draw_labels(boxes, confidences, class_ids, classes, colors, image):
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            cv2.putText(image, label, (x, y + 30), font, 2, color, 2)
    return image

def detect_objects_in_car():
    # Replace "car_image.jpg" with a random file path
    image_path = random.choice(["Car1.jpg", "Car2.jpg", "Car3.jpg"])
    image = cv2.imread("F:\My projects\Python Projects\Car1.jpg")
    image = cv2.resize(image, None, fx=0.4, fy=0.4)
    height, width, _ = image.shape

    boxes, confidences, class_ids = detect_objects(image)

    classes = ["gun", "drug"]  # Customize as needed
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    image_with_boxes = draw_labels(boxes, confidences, class_ids, classes, colors, image)

    if len(boxes) > 0:
        print("The car has been flagged for security check!")
        cv2.imshow("Security Check", image_with_boxes)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("The car is clear.")

# Call the function
detect_objects_in_car()
