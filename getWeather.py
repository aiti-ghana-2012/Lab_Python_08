import urllib
import re

# Get a file-like object for the Python Web site's home page.
f = urllib.urlopen("http://www.wunderground.com/global/stations/65432.html")
# Read from the object, storing the page's contents in 's'.
s = f.read()
f.close()