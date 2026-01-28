from flask import Flask, render_template, request, jsonify
import whisper
import tempfile
import os

app = Flask(__name__)

# Load model once
model = whisper.load_model("base")  # use "small" or "medium" for better quality

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"error": "No audio"}), 400

    audio_file = request.files["audio"]

    # Save temp wav
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as temp:
        audio_file.save(temp.name)
        temp_path = temp.name

    try:
        result = model.transcribe(temp_path)
        text = result["text"]
    finally:
        os.remove(temp_path)

    return jsonify({"text": text})


if __name__ == "__main__":
    app.run(debug=True)
