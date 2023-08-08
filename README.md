## This project will automatically download video from Bilibili by the url of the video.

## Instructions

There is only main.py but it requires some packages: requests, lxml, tqdm. You can download them using:

`pip install -r requirements.txt`

FFmpeg is a powerful and versatile open-source multimedia framework that provides a collection of tools and libraries for processing and manipulating audio and video files. Since video and audio are seperatedly downloaded from Bilibili, we need it to merge them. If you don't have FFmpeg please download it here:

<https://ffmpeg.org/>

The project needs your cookies from Bilibili to download. Please add your cookies to the code here:

`"Cookie": "Your cookies"`

Cookies sometimes need to be updated. If you find the code unable to download some videos, please update coookies.

The code can be run only in terminal by using

`python main.py -u/--url "The url of the video"`

For example:

`python main.py -u "https://www.bilibili.com/bangumi/play/ep291708?theme=movie&spm_id_from=333.337.0.0"`

`python main.py -u "https://www.bilibili.com/video/BV1GJ411x7h7/?spm_id_from=333.337.search-card.all.click"`

During the downloading, video.mp4 and audio.mp3 will appear. Please leave them alone and they will be deleted automatically after the final video is done. The final video is named as "{the title of the video}.mp4" and saved at the same path as main.py. 

Code is only used for learning and communication instead of commercial purposes. If you've found any problems please feel free to contact me.