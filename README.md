# Coloriser Script

Convenience script for colorising text in a terminal, interfacing with the [DeepAi API](https://deepai.org/machine-learning-model/colorizer).

## 1. Initialise these three global variables:

- `API_KEY`: Your DeepAI API key as env variable `DEEPAI_API_KEY`
- `SRC`: The directory containing the jpegs to be colored, with suffix `.jpg`
- `DEST`: The directory to save the colored jpegs

## 2. Prepare the source directory

Prepare a series of jpegs in the `SRC` directory, with the following naming convention:

    `<name>.jpg`

where `<name>` is the name of the image, without the suffix `.jpg`.

## 3. Run the script

And that's it! Beware, the script does not conduct any validity checks or error handling.
