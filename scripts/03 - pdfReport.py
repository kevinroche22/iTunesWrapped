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
date = "December 2nd, 2021"

# Write body script
script = 'December 1st, 2021: I woke up slowly and looked outside. It was snowing lightly, causing a smile to creep across my face. '\
    'Christmas season was upon us! "Nothing can ruin my mood today," I thought to myself as I sat down at my desk and prepared for another workday.\n\n'\
    'And then I opened Instagram.\n\nIt was everywhere. Every single story on my feed. Spotify Wrapped had taken over. Hell, a guy from '\
    'my highschool even posted that he was in the top 0.1% of Logic listeners. In 2021. Weird flex.\n\nAnyway, the reason it upset me so much '\
    'was simple: I don\'t have Spotify. Or Apple Music. Or anything else. I\'m still out here torre- uhm, buying and downloading all of my music. '\
    'It\'s the only way to live, and I\'ll die on that hill - but I digress. The only feature that streaming services offer that I feel like I\'m '\
    'missing out on year after year (and it may shock you that a data analyst feels this way) is what Spotify Wrapped offers: those sweet, sweet summary stats.\n\n'\
    'So, I got to researching, and here I am two days later - a little better at Python, a lot better at seeing others post their Spotify Wrapped without entering an uncontrollable rage, '\
    'and very confused about how I\'m going to explain to my friends that I listened to MF DOOM almost 400 times this year.'

#################
# Create report #
#################

# Define function to create report
def createReport(filename = 'iTunesWrapped2021.pdf'):

    ## Define pdf
    pdf = FPDF()

    ''' Title Page '''

    # Add title page
    pdf.add_page()

    # Add letterhead
    pdf.image("/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/kevsLetterhead.png", 0, 0, width)

    # Add logo
    pdf.image("/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/logo.png", 20.5, 95, width/2+60)

    # Add intro text
    pdf.set_font('Helvetica', 'I', 12)
    pdf.ln(height-40)
    pdf.write(5, f'     Created {date}, just a day after Spotify Wrapped came out and ruined my life.')

    ''' Introduction '''

    # Add Intro page
    pdf.add_page()

    # Add letterhead
    pdf.image("/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/kevsLetterhead.png", 0, 0, width)

    # Add Intro Title
    pdf.set_font('Helvetica', 'B', 24)
    pdf.ln(62)
    pdf.write(5, f'A Quick Introduction')

    # Add body text
    pdf.set_font('Helvetica', '', 12)
    pdf.ln(20)
    pdf.write(8, script)

    # Add doom image
    pdf.image("/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/doom.png", width-21, height-67, 8)

    # Add logo again
    pdf.image("/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/logo.png", 34.5, height-55, width-80)

    ''' Page Three '''

    # Add page
    pdf.add_page()

    # Add letterhead
    pdf.image("/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/kevsLetterhead.png", 0, 0, width)

    # Add Title
    pdf.ln(62)
    pdf.image("/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/statsOne.png", 85, 42, 70)

    # Add plot
    pdf.image("/Users/kevinroche22/PythonData/iTunesWrapped/plots/mostListenedArtists.png", 15, 80, width - 35)

    # Add Genre
    pdf.image("/Users/kevinroche22/PythonData/iTunesWrapped/plots/genreBreakdown.png", width-110, 202, 112)

    # Add Stats
    pdf.image("/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/timeStats.png", 15, 202, 100)

    ''' Page Four '''

    # Add page
    pdf.add_page()
    
    # Add letterhead
    pdf.image("/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/kevsLetterhead.png", 0, 0, width)

    # Add Title
    pdf.ln(62)
    pdf.image("/Users/kevinroche22/PythonData/iTunesWrapped/letterhead/statsTwo.png", 86, 42, 70)

    # Add plots
    pdf.image("/Users/kevinroche22/PythonData/iTunesWrapped/plots/mostListenedSongs.png", 18, 90, width-15)
    pdf.image("/Users/kevinroche22/PythonData/iTunesWrapped/plots/mostListenedAlbums.png", 3, 195, width-8, height-205)

    # Output pdf
    pdf.output(filename)

# Create report
if __name__ == '__main__':
    createReport()
