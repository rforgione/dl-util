# A script for moving the cat and dog image files from the Kaggle
# competition dataset into the appropriate data structure for the Vgg class.
# The script should be run from within the directory of image files.

import os
import re
import random

if not os.path.exists("../valid"):
    os.makedirs("../valid")

if not os.path.exists("../valid/dogs"):
    os.makedirs("../valid/dogs")

if not os.path.exists("../valid/cats"):
    os.makedirs("../valid/cats")

if not os.path.exists("dogs"):
    os.makedirs("dogs")

if not os.path.exists("cats"):
    os.makedirs("cats")

# iterate over files
dog_pattern = re.compile("^dog.+\.jpg$")
cat_pattern = re.compile("^cat.+\.jpg$")

for file in os.listdir("."):
    if bool(dog_pattern.match(file)):
        num = random.randint(0,3)
        if num == 0:
            os.rename(file, "../valid/dogs/" + file)
        else:
            os.rename(file, "dogs/" + file)
    elif bool(cat_pattern.match(file)):
        if num == 0:
            os.rename(file, "../valid/cats/" + file)
        else:
            os.rename(file, "cats/" + file)


