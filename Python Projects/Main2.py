import numpy as np
from tkinter import Tk, Label, Button, filedialog, StringVar
from PIL import Image, ImageTk
from sklearn.externals import joblib  # For loading pre-trained models
from sklearn.preprocessing import StandardScaler
from skimage import feature

# Load the pre-trained scikit-learn model (assumed to be an SVM or another ML model)
loaded_model = joblib.load("model.pkl")  # Replace with your own model path

class ImageClassifierGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cat and Dog Image Classifier")
        self.root.geometry("400x400")

        self.upload_button = Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.predict_button = Button(root, text="Predict", command=self.predict_image)
        self.predict_button.pack()

        self.image_label = Label(root)
        self.image_label.pack()

        # Create a StringVar to hold the text of the prediction label
        self.prediction_text = StringVar()
        self.prediction_label = Label(root, textvariable=self.prediction_text, font=("Helvetica", 12))
        self.prediction_label.pack()

    def extract_features(self, image):
        """
        Extracts features from the image. Here we use HOG (Histogram of Oriented Gradients).
        """
        image = np.array(image.convert('L'))  # Convert to grayscale
        fd, hog_image = feature.hog(image, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True)
        return fd  # Return the feature descriptor

    def predict_image(self):
        if hasattr(self, "image_array"):
            # Extract features from the image
            features = self.extract_features(self.image_array)

            # Standardize features (if needed)
            features = StandardScaler().fit_transform(features.reshape(1, -1))

            # Make a prediction using the loaded model
            prediction = loaded_model.predict(features)

            # Display the prediction result
            predicted_class = "dog" if prediction == 1 else "cat"
            self.prediction_text.set(f"Prediction: It is a {predicted_class}")

    def upload_image(self):
        # Clear the previous prediction
        self.prediction_text.set("")

        file_path = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if file_path:
            # Load the image and store it
            image = Image.open(file_path)
            self.image_array = image

            # Display the image
            img_tk = ImageTk.PhotoImage(image)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk

if __name__ == "__main__":
    root = Tk()
    app = ImageClassifierGUI(root)
    root.mainloop()
