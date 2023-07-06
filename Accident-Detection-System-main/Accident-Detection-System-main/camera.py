import cv2
import numpy as np
import os
from tensorflow.keras.models import model_from_json

# Load the model architecture from the model.json file
mod = r"C:\Users\Acer pc\Downloads\Accident-Detection-System-main\Accident-Detection-System-main\model.json"
with open(mod, "r") as json_file:
    model_json = json_file.read()

model = model_from_json(model_json)

font = cv2.FONT_HERSHEY_SIMPLEX

def start_application():
    video = cv2.VideoCapture('C:/Users/Acer pc/Downloads/Accident-Detection-System-main/Accident-Detection-System-main/Demo.gif')  # Specify the path to the GIF file here
    frame_count = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        roi = cv2.resize(gray_frame, (250, 250))

        pred = model.predict(roi[np.newaxis, :, :])
        predicted_class = np.argmax(pred, axis=1)[0]
        prob = pred[0][predicted_class]
        if predicted_class == 1:
            prob_percentage = round(prob * 100, 2)
            prob_formatted = "{:.2f}%".format(prob_percentage)

            # To beep when alert:
            # if prob > 90:
            #     os.system("say beep")

            cv2.rectangle(frame, (0, 0), (280, 40), (0, 0, 0), -1)
        

        cv2.imshow('Video', frame)
        if cv2.waitKey(33) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    start_application()
