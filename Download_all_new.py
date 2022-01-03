import pytube
yt = pytube.YouTube('https://www.youtube.com/watch?v=Cz-grBsGGkQ')
videos = yt.get_videos()
for v in videos:
    print(v)


