# Image Watermarking Desktop App
The project uses the Python Pillow library to put a watermark on one of the given images. The Graphical User Interface is created with the use of Tkinter.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
* [License](#license)


## General Information
The project allows the user to put a watermark on a given picture. After running the code, the iterface appears showing an option to choose one of pictures. The chosen picture receives a watermark that is put on it.


## Technologies Used
- Pillow 9.4.0


## Setup
The project's requirements are listed in a "requirements.txt" file.

Download the code from this GitHub repository, two example images ("sunset", "test_sink") and activate the virtual environment. Make sure that you have Python 3.6 or newer installed. The next step is to install the Pillow using pip within a virtual environment:

    PS> python -m venv venv

    PS> .\venv\Scripts\activate

    (venv) PS> python -m pip install Pillow

Next, you are ready to run the code. When running the code, you get the following error:

    FileNotFoundError: [Errno 2] No such file or directory: 'logo.png'

you should use an absolute path instead of a relative one, in the lines:

    watermark = "logo.png"

    sunset = "sunset.png"

    sink = "test_sink.png"

## Usage
After fulfilling the instructions described in "Setup" you are ready to use the code.


## Project Status
The project's status is _complete_.


## Room for Improvement
As for future development it would be worth to offer the users a possibility to put their own watermarks on their own images.


## Acknowledgements
This project was based on "Image Processing With the Python Pillow Library" (https://realpython.com/image-processing-with-the-python-pillow-library/).


## Contact
Created by Adam Hoppe (adhoppe@poczta.fm) - feel free to contact me!


## License
This project is open source and available under the MIT License.
