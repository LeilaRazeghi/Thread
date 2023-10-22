from time import time
from moviepy import editor

def convert(video_name, audio_name):
    video = editor.VideoFileClip(video_name)
    video.audio.write_audiofile(audio_name)

videos=[["OfficeWorkout1.mp4", "OfficeWorkout1.mp3"],
        ["OfficeWorkout2.mp4", "OfficeWorkout2.mp3"],
        ["OfficeWorkout3.mp4", "OfficeWorkout3.mp3"],
        ["OfficeWorkout4.mp4", "OfficeWorkout4.mp3"],
        ["OfficeWorkout5.mp4", "OfficeWorkout5.mp3"]
]

start_time=time()

for video, audio in videos:
    convert(video, audio)


end_time=time()

print(end_time-start_time)

#result=32.44288229942322