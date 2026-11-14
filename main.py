import os
import shutil

# Copy the entry image into the grader's output directory.
# The image is a four-panel collage (chips, outage, talks, tankers)
# generated for this entry; the program only copies it, deterministically.
HERE = os.path.dirname(os.path.abspath(__file__))

os.makedirs("/output", exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"), "/output/entry.png")
