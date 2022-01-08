import os

folder = 'Youtube_videos'
file_list = os.listdir(folder)
id_list = []
for filename in file_list:
    filename_list = filename.split(' - ')
    video_id = filename_list[0]
    id_list.append(video_id)

print(id_list)

