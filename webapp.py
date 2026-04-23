import streamlit as st
from main import get_info, get_quality, download_video, download_playlist
import tempfile ,os
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

        if st.button("Download Playlist"):
            with st.spinner("Downloading playlist..."):
                with tempfile.TemporaryDirectory() as tmpdir:                
                    download_playlist(url, tmpdir, folder_name)
                    playlist_dir = os.path.join(tmpdir, folder_name)
                    for fname in os.listdir(playlist_dir):
                        fpath = os.path.join(playlist_dir, fname)
                        with open(fpath, "rb") as f:
                            st.download_button(
                                label=f"{fname}",
                                data=f,
                                file_name=fname,
                                mime="video/mp4"
                            )                    

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
                    with tempfile.TemporaryDirectory() as tmpdir:
                        download_video(url, tmpdir, quality)
                        fname = os.listdir(tmpdir)[0]
                        fpath = os.path.join(tmpdir, fname)
                        with open(fpath, "rb") as f:
                            st.download_button(
                                label=f"{fname}",
                                data=f,
                                file_name=fname,
                                mime="video/mp4"
                            )

                st.success("Video downloaded successfully!")

st.divider()
link = "https://www.linkedin.com/in/muhammadawaistariq/"
st.markdown("Made by: [Muhammad Awais tariq](%s)" %link)