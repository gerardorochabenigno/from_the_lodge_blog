import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://fromthelodge.netlify.app"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True