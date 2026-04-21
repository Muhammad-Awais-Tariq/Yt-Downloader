import yt_dlp

def get_info(url):
    with yt_dlp.YoutubeDL({"quiet": True,"no_warnings": True,}) as ydl:
        info = ydl.extract_info(url, download=False)

    return info

def download_video(url , destination ,quality):
    video_opts = {
        "quiet": True,
        "no_warnings": True,
        'format': f'bestvideo[height={quality}]+bestaudio/best',
        'outtmpl': f'{destination}/%(title)s.%(ext)s',
        'ffmpeg_location': './ffmpeg/bin/ffmpeg.exe',

    }

    with yt_dlp.YoutubeDL(video_opts) as ydl:
        ydl.download([url])
    


def get_quality(info):
    qualities = set()
    formats = info.get("formats" , [])
    for f in formats:
        if f != None and f.get("ext") == "mp4":
            qualities.add(f.get("height"))

    sorted_list = list(qualities)
    sorted_list.sort()
    return sorted_list

def get_video(url):
    destination = input("Enter the destination path : ")
    info = get_info(url)
    avaliable_quality = get_quality(info)
    while True:
        quality = int(input(f"Following video qualities are avaliable for the video {avaliable_quality} \n Select one : "))
        if quality in avaliable_quality:
            break
    title = info.get("title")
    print(f"Downloading : {title}")
    download_video(url , destination ,quality )

def download_playlist(url , destination , folder_name):
    playlist_opts = {
    "quiet": True,
    "no_warnings": True,
    'format': 'bestvideo+bestaudio/best',
    'ignoreerrors': True,
    'noplaylist': False,
    'outtmpl': f'{destination}/{folder_name}/%(title)s.%(ext)s',
    'merge_output_format': 'mp4',
    'continuedl': True,
    'download_archive': 'downloaded.txt',    
    }

    with yt_dlp.YoutubeDL(playlist_opts) as ydl:
        ydl.download([url])

def get_playlist(url):
    destination = input("Enter the destination path : ")
    folder_name = input("Enter the name of the folder for playlist : ")

    print("Downloading")
    download_playlist(url , destination , folder_name)

def main():
    url = input("Enter the url: ")

    if "list=" in url: 
        get_playlist(url)
    else:
        get_video(url)


if __name__ == "__main__":
    main()

#using streamlit make an interactive gui