import streamlit as st
from main import get_info, get_quality, download_video, download_playlist

st.set_page_config(page_title="YouTube Downloader", layout="centered")

st.title("YouTube Downloader")


url = st.text_input("Enter YouTube URL")

if url:

    info = get_info(url)
    title = info.get("title", "Unknown Title")

    st.subheader(f"{title}")

    is_playlist = "list=" in url

    if is_playlist:
        destination = st.text_input("Download folder path", "downloads")
        folder_name = st.text_input("Playlist folder name", "my_playlist")

        if st.button("⬇ Download Playlist"):
            with st.spinner("Downloading playlist..."):
                download_playlist(url, destination, folder_name)
            st.success("Playlist downloaded successfully!")

    else:
        qualities = get_quality(info)

        if not qualities:
            st.warning("No quality info found")
        else:
            quality = st.selectbox("Select video quality", qualities)

            destination = st.text_input("Download folder path", "downloads")

            if st.button("Download Video"):
                with st.spinner("Downloading video..."):
                    download_video(url, destination, quality)
                st.success("Video downloaded successfully!")

st.divider()
link = "https://www.linkedin.com/in/muhammadawaistariq/"
st.markdown("Made by: [Muhammad Awais tariq](%s)" %link)