from flask import Flask, request, jsonify
from summarization import summarize_text
from transcribe_audio import transcribe_audio

app = Flask(__name__)

@app.route('/')
def index():
    return "Automated Meeting Summarizer is running."

@app.route('/summarize', methods=['POST'])
def summarize():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})

    # Save the uploaded file
    file_path = "uploaded_file"  # Save the uploaded file temporarily
    file.save(file_path)

    # Transcribe audio to text
    transcript = transcribe_audio(file_path)
    if not transcript:
        return jsonify({"error": "Error during transcription"})

    # Summarize the transcript
    summary = summarize_text(transcript)

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)

