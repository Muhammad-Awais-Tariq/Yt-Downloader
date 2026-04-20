import yt_dlp

url = "https://www.youtube.com/watch?v=GZkbK1NXuas"

def get_info(url):
    with yt_dlp.YoutubeDL({"quiet": True,"no_warnings": True,}) as ydl:
        info = ydl.extract_info(url, download=False)

    return info

def download(url , destination):
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        'outtmpl': f'{destination}/%(title)s.%(ext)s'
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
    print(get_quality(info))
    title = info.get("title")
    print(f"Downloading : {title}")
    download(url , destination)

if __name__ == "__main__":
    main()


#add the task to select the specific quality to download
#add the option to select between playlist and video
#download all the videos in the playlist
#using streamlit make an interactive gui