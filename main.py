import os
import requests
import argparse
import json
from lxml import etree
from tqdm import tqdm

parse = argparse.ArgumentParser(
    prog="Download bilibili video.", description="Download bilibili video by url.")
parse.add_argument("--url", "-u", help="The url of the video.", required=True)
args = parse.parse_args()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Cookie": "",
    "Referer": "https://www.bilibili.com/"
}
chunk_size = 4096  # chunk size


def write(url, name, desc):
    response = requests.get(url, headers=headers, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    with open(name, mode="wb") as f:
        with tqdm(total=total_size, unit='B', unit_scale=True, desc=desc) as pbar:
            for chunk in response.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                pbar.update(len(chunk))
    print(f"Download from {url} to ./{name}")


def download(url):
    if url[25:30] == "video":
        response = requests.get(url=url, headers=headers)
        tree = etree.HTML(response.text)
        data = json.loads(tree.xpath("/html/head/script[3]")[0].text[20:])
        title = tree.xpath(
            "/html/head/title")[0].text.replace("_哔哩哔哩_bilibili", "")
        video_url = data["data"]["dash"]["video"][0]["baseUrl"]
        audio_url = data["data"]["dash"]["audio"][0]["baseUrl"]
    elif url[25:32] == "bangumi":
        response = requests.get(url=url, headers=headers)
        tree = etree.HTML(response.text)
        tree.xpath("/html/head/title")
        title = tree.xpath(
            "/html/head/title")[0].text.replace("-电影-高清正版在线观看-bilibili-哔哩哔哩", "")
        id = url[40:46]
        url = f"https://api.bilibili.com//pgc/player/web/v2/playurl?support_multi_audio=true&avid=75449394&cid=129066799&qn=116&fnver=0&fnval=4048&fourk=1&gaia_source=&from_client=BROWSER&ep_id={id}&session=081ae231a816e98efe7a7c22038fcd5e&drm_tech_type=2"
        response = requests.get(url=url, headers=headers)
        video_url = response.json(
        )["result"]["video_info"]["dash"]["video"][0]["baseUrl"]
        audio_url = response.json(
        )["result"]["video_info"]["dash"]["audio"][0]["baseUrl"]
    else:
        return
    write(url=video_url, name="video.mp4", desc="Downloading video.mp4")
    write(url=audio_url, name="audio.mp3", desc="Downloading audio.mp3")
    if not os.path.exists(f"./{title}.mp4"):
        os.system(f"ffmpeg -i video.mp4 -i audio.mp3 -c copy {title}.mp4")
        print(f"Combine video.mp4 and audio.mp3 to {title}.mp4")
    if os.path.exists("video.mp4"):
        os.system("del video.mp4")
    if os.path.exists("audio.mp3"):
        os.system("del audio.mp3")


download(args.url)
