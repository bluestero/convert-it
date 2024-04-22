from moviepy.editor import VideoFileClip, AudioFileClip

audio = VideoFileClip("Test.mp4").audio
print(audio.reader.read_chunk(10))