# import python packages
from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import os
from werkzeug.utils import secure_filename

# constant values and variables
app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'super secret key'
PATHFILE = "model"
FILE = "densenet_.h5"
HEADINGLIST = ["filename", "DR status"]
RETINAClASSES = ['NO', 'Mild', 'Moderate', 'Severe', 'Proliferative']
MODEL = os.path.join(os.getcwd(), os.path.join(PATHFILE, FILE))

# index page
@app.route('/')
def index():
    return render_template('index.html')

# upload images processing and predicts
@app.route("/", methods=["GET","POST"])
def upload_file():
    # post method to upload images
    if request.method == "POST":
        # check if images are uploaded or not
        if "images" not in request.files:
            return render_template('index.html'), 201
        # List of images
        files1 = request.files.getlist("images")
        results = {}
        # load the prediction model
        retinamodel = tf.keras.models.load_model(MODEL)
        # for loop each image or file
        for file in files1:
            # get the file name with removal of special characters
            filename = secure_filename(file.filename)
            # open the file
            image = Image.open(file)
            # array the image
            demo = np.array(image)
            # copy to extract the data
            demo = demo[:, :, ::-1].copy()
            # type conversion
            demo = tf.image.convert_image_dtype(demo, tf.float32)
            # resizing the image
            demo = tf.image.resize(demo, size=[300, 300])
            # dimensions
            demo = np.expand_dims(demo, axis=0)
            # predict the status of the DR using model
            pred = retinamodel.predict(demo)
            # collect the status
            result = np.argmax(pred)
            # dict the values and file name
            results[filename] = RETINAClASSES[result]
            # post the value in the page
        return render_template("results.html", heading=HEADINGLIST, result=results), 201
    return render_template("index.html")


if __name__ == "__main__":
    # run the application
    app.run(debug=False)
