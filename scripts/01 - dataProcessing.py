"""
This script pulls the metadata I need to analyze my iTunes library and writes it to a .csv in the data folder.
"""

## Load packages
from appscript import *
import pandas as pd

## Define iTunes application
itunes = app("iTunes")

## Initialize empty list
iTunesInfo = []

## Pull required data
for track in itunes.file_tracks():
    iTunesInfo.append(
        {
            "song": track.name(),
            "album": track.album(),
            "artist": track.artist(),
            "albumArtist": track.album_artist(),
            "playCount": track.played_count(),
            "dateAdded": track.date_added(),
            "genre": track.genre(),
            "duration": track.duration(),
            "skips": track.skipped_count()
        }
    )

## Convert to pandas dataframe
iTunesInfo = pd.DataFrame(iTunesInfo)

## Write to folder
iTunesInfo.to_csv(
    "/Users/kevinroche22/PythonData/iTunesWrapped/data/iTunesInfo.csv",
    index=False
)
