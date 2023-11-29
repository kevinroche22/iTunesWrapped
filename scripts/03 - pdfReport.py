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
date = "November 29th, 2023"

# Write body script
script = (
    "T and I went to a play (social outing for assholes) a while back back and they made a joke about how people who send out Christmas newsletters are assholes."
    " 'So true', I whispered to T, only a few weeks before building my annual Christmas newsletter for music like an asshole.\n\n"
    "This year\'s findings were so embarassing that I had to add a brand new page measuring listens by hour instead of play count. "
    "It helps the story a little bit, but at the end of the day all of my top 10 songs were either by Drake or White Drake. I might never reputationally recover from this.\n\n"
    "The story here is that I'm slowly morphing into Gerard. 10K less hours of music listened to this year than last year, and a rock (ish?) album made it into the top 10. "
    "I spend every summer day fighting the urge to ask my neighoburs kids to get off the lawn (this is not a joke), and I'm probably no less than two years away from taking an interest in the Kitchener Jazz Festival.\n\n"
    "Cheers from your Kevin, the one you've known since you were seven.\n\n\n\n\n\n\n\n\n\n"
)

#################
# Create report #
#################

# Define function to create report
def createReport(filename="iTunesWrapped2023.pdf"):

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
        "/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/logo2023.png",
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

    # Add logo again
    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/logo2023.png",
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

    # Add Stats
    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/timeStats2023.png",
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
    
    """ Page Five """

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
        "/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/statsThree.png",
        86,
        42,
        70,
    )

    # Add plots
    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/plots/mostListenedSongsHours.png",
        8,
        90,
        width - 22,
    )

    pdf.image(
        "/Users/kevinroche22/PythonData/iTunesWrapped/plots/mostListenedAlbumsHours.png",
        12,
        190,
        width - 24,
    )
    
    # Output pdf
    pdf.output(filename)


# Create report
if __name__ == "__main__":
    createReport()
