
from flask import Flask, request, make_response
import addMask
import numpy as np
import base64
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def home():
    return "<html><body>95Defender API is running</body></html>"


@app.route('/mask_image', methods = ['GET'])
def mask_image():
    imgArr = request.form['image_buffer']
    decoded_data = base64.b64decode(imgArr)
    np_data = np.fromstring(decoded_data, np.uint8)
    maskedImgArr = base64.b64encode(addMask.mask(np_data))
    return make_response(maskedImgArr)

# debugger can be auto reload feature 
if __name__ == '__main__':
    app.run(debug=True)