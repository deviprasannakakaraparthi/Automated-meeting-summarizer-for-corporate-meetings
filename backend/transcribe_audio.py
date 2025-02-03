import speech_recognition as sr
from moviepy.editor import VideoFileClip

def transcribe_audio(file_path):
    # If it's a video, extract the audio
    if file_path.endswith('.mp4') or file_path.endswith('.avi'):
        video = VideoFileClip(file_path)
        audio_path = "temp_audio.wav"
        video.audio.write_audiofile(audio_path)
        file_path = audio_path

    # Initialize recognizer class (for recognizing speech)
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)

    # Use Google Speech Recognition to transcribe audio
    try:
        transcript = recognizer.recognize_google(audio)
        return transcript
    except sr.UnknownValueError:
        return "Could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

