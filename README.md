# iTunesWrapped

All of my friends are posting their end of year Spotify Wrapped infographics, and I'll be damned if I can't join them. The issue: I still, erm, buy all of my music through iTunes. Yes, you read that right - I'm the last man on Earth that doesn't use a music streaming service. So, I needed a way to query my iTunes library. Enter: `appscript`, which transforms AppleScript (never heard of it? don't worry, neither has anyone else) commands to a python interpretable format and allowed me to pull my iTunes info into a .csv. From there, I used `pandas` and `matplotlib` to manipulate and plot the data, and `fpdf` to build the final report. 

If you're one of my buddies here to check out my iTunes Wrapped, click [here.](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

This project contains the following scripts:
- [01 - dataProcessing.py](https://github.com/kevinroche22/iTunesWrapped/blob/master/scripts/01%20-%20dataProcessing.py).
- [02 - dataAnalysis.py](https://github.com/kevinroche22/iTunesWrapped/blob/master/scripts/02%20-%20dataAnalysis.py).
- [03 - pdfReport.py](https://github.com/kevinroche22/iTunesWrapped/blob/master/scripts/03%20-%20pdfReport.py)

And outputs the following PDF:
- [Kev's iTunes Wrapped 2021'](https://github.com/kevinroche22/iTunesWrapped/blob/master/iTunesWrapped2021.pdf)
