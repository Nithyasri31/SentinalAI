from utils.speech_utils import speech_to_text

audio_path = "uploads/audio/test.mp4"   # Change the name if your file is different

text = speech_to_text(audio_path)

print("Transcript:")
print(text)