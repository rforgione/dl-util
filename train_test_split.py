# A script for moving the cat and dog image files from the Kaggle
# competition dataset into the appropriate data structure for the Vgg class.
# The script should be run from within the directory of image files.

import os
import re

if not os.path.exists("dogs"):
    os.makedirs("dogs")

if not os.path.exists("cats"):
    os.makedirs("cats")

# iterate over files
dog_pattern = re.compile("^dog.+\.jpg$")
cat_pattern = re.compile("^cat.+\.jpg$")

for file in os.listdir("."):
    if bool(dog_pattern.match(file)):
        print file
        print "dogs/" + file
        os.rename(file, "dogs/" + file)
    elif bool(cat_pattern.match(file)):
        os.rename(file, "cats/" + file)


