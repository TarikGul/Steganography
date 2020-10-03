# Welcome to this steganography repository.

In this repository we are going to embed a message inside a picture and then allow you to decode the message as well

## Getting Started

Lets get things running for you. 

First lets setup your virtual enviornment

In the root directory of this repository

```python3 -m venv env```

```source env/bin/activate```

Now that we have you in a virtual env, lets install necessary dependencies. 

```pip install pillow```

Now that we have it all installed. Lets embed an image with som text.
I have put a mock png in here so that you can work with that. The command to run it is simple.

There are two flags you can use. ```-e``` for encode, and ```-d``` for decode.

``` python hide.py -e video.png```

Then you will be prompted to write the message you want to embed it with.

Then in order to decode that message 

``` python hide.py -d video.png```

# TODOS

Add the encryption to the message then embed the message. I wrote a one time pad to use. 
The next and more adventurous goal should be to embed files into an image. 
