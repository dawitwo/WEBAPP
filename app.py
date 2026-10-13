import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("./ufo-model.pkl", "rb"))

# Load the LabelEncoder so we can turn integer predictions back into country names
le = pickle.load(open("./ufo-countries.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Use float, NOT int — lat/lng are decimals
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]

    prediction = model.predict(final_features)[0]

    # Map the integer back to the real country name
    country_name = le.inverse_transform([prediction])[0]

    return render_template(
        "index.html",
        prediction_text="Likely country: {}".format(country_name)
    )


if __name__ == "__main__":
    app.run(debug=True)