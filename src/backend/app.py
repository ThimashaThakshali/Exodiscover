import os
from flask import Flask, render_template, request, redirect, url_for, flash
from inference import predict_exoplanet

app = Flask(
    __name__,
    template_folder=os.path.join(os.getcwd(), "../frontend/templates"),
    static_folder=os.path.join(os.getcwd(), "../frontend/static")
)
app.secret_key = "supersecretkey"
UPLOAD_FOLDER = os.path.join(os.getcwd(), "../data")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'file' not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files['file']
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            prediction, confidence = predict_exoplanet(filepath)
            return render_template("result.html", filename=file.filename, prediction=prediction, confidence=confidence)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
