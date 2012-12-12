	   __                             __ ______     __ 
	  / /_____  _____________  ____  / //_  __/  __/ /_
	 / __/ __ \/ ___/ ___/ _ \/ __ \/ __// / | |/_/ __/
	/ /_/ /_/ / /  / /  /  __/ / / / /_ / / _>  </ /_  
	\__/\____/_/  /_/   \___/_/ /_/\__//_/ /_/|_|\__/  
	                                                   
Author: Leland Batey

Description
===========
torrentTxt monitors a directory and whenever a file is added, you will receive a txt message (via Twilio) with the name of the file added. This makes a great addition to a seedbox that automatically adds torrents from an RSS feed, so you know exactly when you've got new downloads!

Notes:
------
torrentTxt is meant to be installed as a cronJob that runs every few minutes.

Requirements:
-------------
1. Python 2.7
2. Twilio tools installed (`pip install Twilio`)
3. A Twilio account

Instructions:
-------------
1. Edit the torrentTxt.py file so that it has the correct settings for your needs. This means setting the appropriate directory to watch, your Twilio account SID and Auth Key, as well as the correct send and receive phone numbers.
2. Set up a cron job to run the torrentTxt.py at a suitable interval. An example that runs every 5 minutes:
		
	`*/5 * * * * /path/to/python /path/to/torrentTxt.py`
	- Note that if you are using a virtualenvironment (something I highly recommend) then "/path/to/python" will be "/path/to/virtualenv/**bin/python**"
3. ???
4. Profit!
