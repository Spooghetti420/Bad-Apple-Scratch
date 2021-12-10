# Bad Apple frame extractor
This is a frame extractor and encoder for my Scratch project: (https://scratch.mit.edu/projects/614473645/editor).
It uses (simple) run-length encoding to compress the image data for Bad Apple into a Scratch-sized file which is able to fit within the 5MB project JSON limit.
Since the individual frames consist largely of black and white only, I quantize the pixels to one of either (255, 255, 255) or (0, 0, 0) depending on its brightness.
Then, it is run-length encoded to convert frames into sequences of like pixels; for instance, the first frame is "10800B". The corresponding data can be recovered from within the Scratch project.

## Running
In order to get the video, run the command (provided you have Python and pip installed, or youtube-dl) in `get_video.sh`; subsequently, extracting the frames is as simple as running `extract_frames.sh`. The frames are then extracted into the frames directory, from where you can run the Python file:
`python to_string.py`.
