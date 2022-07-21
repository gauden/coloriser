"""
Coloring black and white jpeg images using the DeepAI API.

    API_KEY: Your DeepAI API key as env variable `DEEPAI_API_KEY`
    SRC: The directory containing the jpegs to be colored, with suffix .jpg
    DEST: The directory to save the colored jpegs

"""

import os
from pathlib import Path
from time import sleep
import requests

# read the DeepAI API key from environment variable
API_KEY = os.environ["DEEPAI_API_KEY"]

SRC = Path(__file__).parent / "src"
DEST = Path(__file__).parent / "dest"


def collect_src_jpegs():
    """
    Collect all jpegs in the src directory
    """
    jpegs = []
    for file in SRC.iterdir():
        if file.suffix == ".jpg":
            jpegs.append(file)
    return jpegs


def main():
    jpegs = collect_src_jpegs()
    for jpeg in jpegs:
        target_file = DEST / jpeg.name
        r = requests.post(
            "https://api.deepai.org/api/colorizer",
            files={
                "image": open(jpeg, "rb"),
            },
            headers={"api-key": API_KEY},
        )
        output_url = r.json()["output_url"]
        sleep(1)
        r = requests.get(output_url)
        with open(target_file, "wb") as f:
            f.write(r.content)


if __name__ == "__main__":
    main()
