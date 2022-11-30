"""
This file analyzes and visualizes the iTunes data written in 01 - dataProcessing.py.
"""

########
# Prep #
########

# Load packages
import pandas as pd
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.express as px
from seaborn import palplot
import pyplot_themes as themes

# Load raw iTunes data
iTunesInfo = pd.read_csv(
    "/Users/kevinroche22/PythonData/iTunesWrapped/data/iTunesInfo2022.csv"
)

#################
# Data Cleaning #
#################

# Change date to date format and remove hms
iTunesInfo["dateAdded"] = pd.to_datetime(iTunesInfo.dateAdded).dt.date

# Add "daysSinceDownload" variable by subtracting the date a song was added to itunes from todays date
iTunesInfo["daysSinceDownload"] = date.today() - iTunesInfo["dateAdded"]
iTunesInfo["daysSinceDownload"] = (
    iTunesInfo.daysSinceDownload.astype(str).str.extract("(\d+)").astype(int)
)

# Add "playFrequency" variable by dividing the play count by the number of days since download
iTunesInfo["playFrequency"] = (
    iTunesInfo["playCount"] / iTunesInfo["daysSinceDownload"]
)

# Add "totalSeconds" variable by multiplying plays by duration
iTunesInfo["totalSeconds"] = iTunesInfo["playCount"] * iTunesInfo["duration"]

# Add "songNameAndArtist" variable
iTunesInfo["songNameAndArtist"] = (
    iTunesInfo["song"] + ", " + iTunesInfo["albumArtist"]
)

# Add "albumNameAndArtist" variable
iTunesInfo["albumNameAndArtist"] = (
    iTunesInfo["album"] + ", " + iTunesInfo["albumArtist"]
)

# Fill missing genre information with 0's
iTunesInfo["genre"] = iTunesInfo["genre"].fillna("0")

# Define conditions to simplify genres
conditions = [
    iTunesInfo["genre"].str.contains("((?i)R\&B|soul)"),
    iTunesInfo["genre"].str.contains("((?i)rap|hip.{0,1}hop)"),
    iTunesInfo["genre"].str.contains("^0$"),
    iTunesInfo["genre"].str.contains("((?i)R\&B|soul|rap|hip.{0,1}hop)")
    == False,
]

# Define genre bins
values = ["R&B", "Hip-Hop", "Missing", "Other"]

# Simplify genres
iTunesInfo["genre"] = np.select(conditions, values, default="task")

# Filter on music added in 2022
iTunesInfo = iTunesInfo[
    (iTunesInfo["dateAdded"] >= pd.to_datetime("2021-12-01"))
    & (iTunesInfo["dateAdded"] <= pd.to_datetime("2022-12-01"))
]

# Define table styles
thProps = [
    ("font-size", "14px"),
    ("text-align", "center"),
    ("font-weight", "bold"),
]

style = [dict(selector="th", props=thProps)]

##################
# Data Summaries #
##################

# Determine 10 most listened songs that came out in 2021
mostListenedSongs = iTunesInfo.sort_values(
    by="playCount", kind="mergesort", ascending=False
).head(10)

# Determine most listened songs per day (somewhat addresses bias of having more time to listen to songs released earlier in the year)
listensPerDay = (
    iTunesInfo[(iTunesInfo["daysSinceDownload"] > 30)]
    .sort_values(by="playFrequency", kind="mergesort", ascending=False)
    .head(10)
)

# Determine 10 most listened artists that released in 2021
mostListenedArtists = pd.DataFrame(
    iTunesInfo.groupby(["albumArtist"])["playCount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Determine 10 most listened albums released in 2021
mostListenedAlbums = pd.DataFrame(
    iTunesInfo.groupby(["albumNameAndArtist"])["playCount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Determine 10 most skipped songs released in 2021
mostSkips = iTunesInfo.sort_values(
    by="skips", kind="mergesort", ascending=False
).head(10)

# Determine how many hours I spent listening to my top 10 songs
hoursPerSong = pd.DataFrame(
    iTunesInfo.groupby(["song", "albumArtist"])["totalSeconds"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
hoursPerSong["totalSeconds"] = hoursPerSong["totalSeconds"].div(3600)
hoursPerSong = hoursPerSong.rename(
    {"totalSeconds": "totalHours"}, axis="columns"
)
hoursPerSong.style.set_table_styles(style)

# Determine how many hours I spent listening to my top 10 artists
hoursPerArtist = pd.DataFrame(
    iTunesInfo.groupby(["albumArtist"])["totalSeconds"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
hoursPerArtist["totalSeconds"] = hoursPerArtist["totalSeconds"].div(3600)
hoursPerArtist = hoursPerArtist.rename(
    {"totalSeconds": "totalHours"}, axis="columns"
)
hoursPerArtist.style.set_table_styles(style)

# Determine how many hours I spent listening to my top 10 albums
hoursPerAlbum = pd.DataFrame(
    iTunesInfo.groupby(["album", "albumArtist"])["totalSeconds"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
hoursPerAlbum["totalSeconds"] = hoursPerAlbum["totalSeconds"].div(3600)
hoursPerAlbum = hoursPerAlbum.rename(
    {"totalSeconds": "totalHours"}, axis="columns"
)
hoursPerAlbum.style.set_table_styles(style)

# Determine time spent listening across genres
hoursPerGenre = pd.DataFrame(
    iTunesInfo.groupby(["genre"])["totalSeconds"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)
hoursPerGenre["totalSeconds"] = hoursPerGenre["totalSeconds"].div(3600)
hoursPerGenre = hoursPerGenre.rename(
    {"genre": "genre", "totalSeconds": "totalHours"}, axis="columns"
)

# Total minutes&hours listened
totalSecondsListened = pd.DataFrame(iTunesInfo["totalSeconds"]).sum()
totalMinutesListened = totalSecondsListened.div(60).round(0)
totalHoursListened = totalSecondsListened.div(3600).round(0)

############
# Data Viz #
############

# Define hoursPerGenre parameters
genreLabels = ["R&B", "Hip-Hop", "Other"]

# Plot hours per genre
plt.pie(
    hoursPerGenre["totalHours"],
    labels=genreLabels,
    autopct="%1.1f%%",
    shadow=True,
    colors=["tomato", "lightsalmon", "peachpuff"],
    textprops={"weight": "bold", "fontsize": "13"},
)
plt.title("Genre Breakdown", weight="bold", fontsize=16)
plt.tight_layout()
plt.savefig(
    "/Users/kevinroche22/PythonData/iTunesWrapped/plots/genreBreakdown.png"
)
plt.show()

# Plot most listened songs
mostListenedSongs = mostListenedSongs.sort_values("playCount")
plt.barh(
    mostListenedSongs["songNameAndArtist"],
    mostListenedSongs["playCount"],
    color="tomato",
)
plt.title("Most Listened Songs of 2021")
plt.xlabel("Play Count")
plt.box(False)
plt.savefig(
    "/Users/kevinroche22/PythonData/iTunesWrapped/plots/mostListenedSongs.png",
    bbox_inches="tight",
)
plt.show()

# Plot most listened artists
mostListenedArtists = mostListenedArtists.sort_values("playCount")
plt.barh(
    mostListenedArtists.index, mostListenedArtists["playCount"], color="tomato"
)
plt.title("Most Listened Artists Of 2021")
plt.xlabel("Combined Play Count (Songs)")
plt.box(False)
plt.savefig(
    "/Users/kevinroche22/PythonData/iTunesWrapped/plots/mostListenedArtists.png",
    bbox_inches="tight",
)
plt.show()

# Plot most listened albums
mostListenedAlbums = mostListenedAlbums.sort_values("playCount")
plt.barh(
    mostListenedAlbums.index, mostListenedAlbums["playCount"], color="tomato"
)
plt.title("Most Listened Albums of 2021")
plt.xlabel("Combined Play Count (Songs)")
plt.box(False)
plt.savefig(
    "/Users/kevinroche22/PythonData/iTunesWrapped/plots/mostListenedAlbums.png",
    bbox_inches="tight",
)
plt.show()