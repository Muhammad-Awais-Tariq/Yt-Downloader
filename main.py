import yt_dlp

def get_info(url):
    with yt_dlp.YoutubeDL({"quiet": True,"no_warnings": True,}) as ydl:
        info = ydl.extract_info(url, download=False)

    return info

def download(url , destination , quality):
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        'format': f'bestvideo[height={quality}]+bestaudio/best',
        'outtmpl': f'{destination}/%(title)s.%(ext)s',
        'ffmpeg_location': './ffmpeg/bin/ffmpeg.exe'
    }   
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
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

def main():
    url = input("Enter the url: ")
    destination = input("Enter the destination path : ")
    info = get_info(url)
    avaliable_quality = get_quality(info)
    while True:
        quality = int(input(f"Following video qualities are avaliable for the video {avaliable_quality} \n Select one : "))
        if quality in avaliable_quality:
            break
    title = info.get("title")
    print(f"Downloading : {title}")
    download(url , destination , quality)

if __name__ == "__main__":
    main()

#add the option to select between playlist and video
#download all the videos in the playlist
#using streamlit make an interactive gui