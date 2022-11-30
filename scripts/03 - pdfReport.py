"""
This file generates a report from the plots and tables built in 02 - dataAnalysis.py
"""

########
# Prep #
########

# Python libraries
from fpdf import FPDF
from datetime import datetime, timedelta
import os

# Set working directory
os.chdir("/Users/kevinroche22/PythonData/iTunesWrapped")

# Set dimensions
width = 210
height = 297

# Date report was written
date = "November 30th, 2022"

# Write body script
script = (
    "We're back. I spent 37,511 minutes listening to music in 2022, which is like 26 days, and a little more than last year. "
    " This pales in comparison to Alex's ~100k minutes, which means the guy spent like 4.5 hours "
    "a day listening to music, almost all of which was certainly Bad Bunny.\n\n"
    "In other Spotify Wrapped news, Jonah found himself in the top 0.05% of Curtis Harding listeners this year, "
    "firmly placing him in the company of hipsters and tech-loving grandparents.\n\n"
    "I don't have much else to say, so I instead present to you, my loyal viewers, that same Alex acting like his Spotify got left on repeat "
    "because he's embarassed his top song was none other than Jack Harlow's Dua Lipa.\n\n\n\n\n\n\n\n\n\n"
)

#################
# Create report #
#################

# Define function to create report
def createReport(filename="iTunesWrapped2022.pdf"):

    ## Define pdf
    pdf = FPDF()

    """ Title Page """

    # Add title page
    pdf.add_page()

    # Add letterhead
    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/kevsLetterhead.png",
        0,
        0,
        width,
    )

    # Add logo
    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/logo2022.png",
        20.5,
        95,
        width / 2 + 60,
    )

    # Add intro text
    pdf.set_font("Helvetica", "I", 12)
    pdf.ln(height - 40)
    pdf.write(
        5,
        f"     Created {date}, and on my lunchbreak instead of during the workday this time.",
    )

    """ Introduction """

    # Add Intro page
    pdf.add_page()

    # Add letterhead
    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/kevsLetterhead.png",
        0,
        0,
        width,
    )

    # Add Intro Title
    pdf.set_font("Helvetica", "B", 24)
    pdf.ln(62)
    pdf.write(5, f"A Quick Introduction")

    # Add body text
    pdf.set_font("Helvetica", "", 12)
    pdf.ln(20)
    pdf.write(8, script)

    # Add doom image
    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/alexRoast2022.png",
        width / 2 - 24,
        height - 126,
        50,
    )

    # Add logo again
    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/logo2022.png",
        34.5,
        height - 55,
        width - 80,
    )

    """ Page Three """

    # Add page
    pdf.add_page()

    # Add letterhead
    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/kevsLetterhead.png",
        0,
        0,
        width,
    )

    # Add Title
    pdf.ln(62)
    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/statsOne.png",
        85,
        42,
        70,
    )

    # Add plot
    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/plots/mostListenedArtists.png",
        15,
        80,
        width - 35,
    )

    # Add Genre
    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/plots/genreBreakdown.png",
        width - 110,
        210,
        112,
    )

    # Add Jonah Roast
    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/jonahRoast2022.png",
        width - 90,
        135,
        60,
    )

    # Add Stats
    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/timeStats2022.png",
        15,
        215,
        100,
    )

    """ Page Four """

    # Add page
    pdf.add_page()

    # Add letterhead
    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/kevsLetterhead.png",
        0,
        0,
        width,
    )

    # Add Title
    pdf.ln(62)
    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/statsTwo.png",
        86,
        42,
        70,
    )

    # Add plots
    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/plots/mostListenedSongs.png",
        8,
        90,
        width - 22,
    )

    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/plots/mostListenedAlbums.png",
        12,
        190,
        width - 24,
    )

    # Output pdf
    pdf.output(filename)


# Create report
if __name__ == "__main__":
    createReport()
