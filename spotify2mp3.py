#!/bin/env python3
# spotify2mp3.py
# Downloads a Spotify playlist into a folder of MP3 tracks
# Github: github.com/not-an-android/Spotify2MP3

import os
from dotenv import load_dotenv, find_dotenv
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import youtube_dl
from youtube_search import YoutubeSearch


def auth():
    """
    Authorizes the client with spotify.
    """
    scope = "playlist-read-private"

    if find_dotenv():
        load_dotenv()
        auth_manager = SpotifyOAuth(scope=scope)
    else:
        client_id = input("Client ID: ")
        client_secret = input("Client Secret: ")
        redirect_uri = (
            f"https://developer.spotify.com/dashboard/applications/{client_id}"
        )
        auth_manager = SpotifyOAuth(client_id, client_secret, redirect_uri, scope)

    return auth_manager


def write_tracks():
    """
    Writes track information (name, artist, URL) to a text file as CSVs.
    """
    written_count = 0

    with open(reference_file, "w") as f:

        for idx, item in enumerate(playlist["tracks"]["items"], start=1):
            name = item["track"]["name"]
            artist = item["track"]["artists"][0]["name"]
            URL = item["track"]["external_urls"]["spotify"]
            csv_line = f"{idx}, {name}, {artist}, {URL}"

            try:
                f.write(f"{csv_line}\n")
                written_count += 1
            except:
                raise

    print(
        f'Successfully written {written_count}/{tracks_total} tracks to "{reference_file_path}".'
    )


def write_playlist():
    """
    Creates playlist directory, moves into it, and calls write_tracks() if it doesn't already exist.
    """
    try:
        if os.path.exists(reference_file_path):
            os.chdir(playlist_name)
        else:
            os.mkdir(playlist_name)
            os.chdir(playlist_name)
            write_tracks()

    except FileExistsError:
        os.chdir(playlist_name)
        write_tracks()
    except:
        raise


def find_and_download_tracks():
    """
    Looks for playlist tracks on YouTube, downloads them, and converts them to MP3 format.
    """
    CONNECTION_ATTEMPTS = 5

    with open(reference_file, "r") as f:

        for line in f:
            csv_list = line.split(",")
            track_name, track_artist = csv_list[1].strip(), csv_list[2].strip()
            search = f"{track_name} by {track_artist}"
            URL = None
            attempts_left = CONNECTION_ATTEMPTS

            while attempts_left > 0:
                try:
                    results = YoutubeSearch(search, max_results=1).to_dict()
                    URL = f"https://www.youtube.com{results[0]['url_suffix']}"
                    break

                except IndexError:
                    attempts_left = 0

                except requests.exceptions.ConnectionError:
                    attempts_left -= 1
                    print(
                        f"\rAn error occured while connecting, retrying... ({attempts_left} attempts left)",
                        end="",
                    )

                except:
                    raise

            if URL is None:
                print(f"\nCould not obtain URL for '{search}', skipping track.")
                continue

            print(f"\nInitiating download for '{search}'.")

            ydl_opts = {
                "format": "bestaudio/best",
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
            }

            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([URL])
            except:
                raise


if __name__ == "__main__":
    auth_manager = auth()
    sp = spotipy.Spotify(auth_manager=auth_manager)
    playlist_id = f"spotify:playlist:{input('Playlist URI: ')}"
    playlist = sp.playlist(playlist_id)
    playlist_name = playlist["name"]
    tracks_total = playlist["tracks"]["total"]
    reference_file = f"{playlist_name}.txt"
    reference_file_path = os.path.join(playlist_name, reference_file)
    write_playlist()
    find_and_download_tracks()
    print("\nDone!")
