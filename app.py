import streamlit as st
from pytube import Playlist

def get_playlist_links(playlist_url):
    playlist = Playlist(playlist_url)
    return [video.watch_url for video in playlist.videos]

st.title("YouTube Music Playlist Link Extractor")

playlist_url = st.text_input("Enter YouTube Music Playlist URL:")

if playlist_url:
    try:
        links = get_playlist_links(playlist_url)
        st.write("### Playlist Links:")
        for link in links:
            st.write(f"- [{link}]({link})")
    except Exception as e:
        st.error(f"An error occurred: {e}")

