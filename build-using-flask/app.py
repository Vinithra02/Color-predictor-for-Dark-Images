from flask import Flask, render_template, request, send_file
import json
#import jsonify
import requests
import pickle
import numpy as np
from PIL import Image
import io
import cv2

app = Flask(__name__)
try:
    with open('color.pkl', 'rb') as file:
        model = pickle.load(file)
except EOFError as e:
    print("Error loading pickled file:", e)

# Function to convert OpenCV image to bytes
def cv2_to_bytes(image):
    _, buffer = cv2.imencode('.jpg', image)
    bytes_image = io.BytesIO(buffer)
    bytes_image.seek(0)
    return bytes_image

# Function to get color name
def get_color_name(R, G, B):
    # Your implementation here based on the provided CSV data
    pass

# Function to handle image enhancement and color detection
def enhance(image):
    # Converting image to LAB color space
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Splitting LAB image into L, A, and B channels
    l, a, b = cv2.split(lab)

    # Applying CLAHE to the L channel
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)

    # Merging color channels
    final = cv2.merge((cl,a,b))

    # Converting image from LAB color space to RGB color space
    enhanced_image = cv2.cvtColor(final, cv2.COLOR_LAB2BGR)
    
    return enhanced_image

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/enhance', methods=['POST'])
def enhance_route():
    if request.method == 'POST':
        # Read the uploaded image
        uploaded_image = request.files['image']
        # Convert the image to OpenCV format
        image_cv2 = cv2.imdecode(np.frombuffer(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)
        # Enhance the image
        enhanced_image = enhance(image_cv2)
        # Define the desired width and height
        desired_width = 500
        desired_height = 650

        # Resize the image to the desired resolution
        enhanced_image = cv2.resize(enhanced_image, (desired_width, desired_height))
        # Convert the enhanced image to bytes
        enhanced_image_bytes = cv2_to_bytes(enhanced_image)
        # Return the enhanced image
        return send_file(enhanced_image_bytes, mimetype='image/jpeg')


@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        message = {'answer':'Your answer is showed here'}
        return message
    if request.method == 'POST':
        data=str(request.data)
        predictionData = data[3:-2].split(',')
        r=int(predictionData[0])
        g=int(predictionData[1])
        b=int(predictionData[2])
        answer=model.predict([[r,g,b]])
        print(answer)
        message = {'answer':answer[0]}
        return message

if __name__=="__main__":
    app.run(debug=True)
