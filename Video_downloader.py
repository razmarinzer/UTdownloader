
import pytube
import moviepy.editor as mpe
import os
import ffmpeg

folder = "E:/Python/Projects/Youtube_videos"
# link = 'https://www.youtube.com/watch?v=Cz-grBsGGkQ&t=1s'
link = 'https://www.youtube.com/watch?v=bN1xpI6f3Vo'


you_video = pytube.YouTube(link)

video_streams = you_video.streams.filter(subtype="mp4").order_by('resolution').desc()
audio_streams = you_video.streams.filter(only_audio=True).order_by('abr').desc()

if not video_streams:
    raise IndexError('Video streams is empty')

if not audio_streams:
    raise IndexError('Audio streams is empty')

print(audio_streams)

video_stream = video_streams[0]
audio_stream = audio_streams[0]

filename = you_video.video_id + ' - ' + you_video.title

# video_stream.download(output_path=folder, filename=filename + '.mp4')
# audio_stream.download(output_path=folder, filename=filename + '.webm')
#
# full_filename_video = os.path.join(folder, filename + '.mp4')
# full_filename_audio = os.path.join(folder, filename + '.webm')
#
# my_clip = mpe.VideoFileClip(full_filename_video)
# final_audio = mpe.AudioFileClip(full_filename_audio)
# # final_audio = mpe.CompositeAudioClip([my_clip.audio, audio_background])
# final_clip = my_clip.set_audio(final_audio)
# final_clip.write_videofile(os.path.join(folder, filename + ' + audio.mp4'))

print("Download Successful...")



# print(os.getcwd())
#
# input_video = ffmpeg.input('./1.mp4')
# input_audio = ffmpeg.input('./1.webm')
#
# out = ffmpeg.concat(input_video, input_audio, v=1, a=1).output('./1.mp4')
#
# out.run()

# class Downloader:
#     def download_video_from_ref(self, video_ref):
#         Save_to = "E:/Python/Projects/Youtube_videos"
#         link = 'https://www.youtube.com/watch?v=Cz-grBsGGkQ&t=1s'
#
#         you_video = pytube.YouTube(link)
#         videos = you_video.get_videos()
#         for v in videos:
#             return v


# you_video.streams.filter(file_extension="mp4").first().download(Save_to)
# print("Download Successful...")


# video_link = 'https://www.youtube.com/watch?v=8ZpVwAeLzm4'
# yt = pytube.YouTube(video_link)
# videos = yt.videos
# video = yt.get('mp4', '720p')
# path = "E:/Python/Projects/Youtube_videos"
# video.download(path)


# def _download_file(self, video_id):
#     file_path = self._build_file_path(video_id)
#     if not os.path.isfile(file_path):
#         yt = YouTube()
#         yt.from_url("http://youtube.com/watch?v=" + video_id)
#         yt.filter('mp4')[0].download(file_path)  # downloads the mp4 with lowest quality
#     return file_path