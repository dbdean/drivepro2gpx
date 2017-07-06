#!/usr/bin/env python3

import base64
import exiftool
import numpy as np


def get_gps_data(videofile, sample_length=8, dtype=np.uint8):
    '''
    Returns the GPS data contained within the videofile.
    '''

    # make sure dtype is numpy dtype object
    dtype = np.dtype(dtype)

    # use exiftool to load the gps tag
    with exiftool.ExifTool() as et:
        data = et.get_tag('Unknown_gps', args.video)

    # decode the base64 data to a byte-string
    assert data.startswith('base64:')
    data = base64.b64decode(data[len('base64:'):])

    # convert the byte string to a numpy array
    data = np.frombuffer(data, dtype=dtype)

    # and reshape according to sample_length (in bytes)
    return data.reshape((-1, sample_length//dtype.itemsize))


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(
        description="Extracts gpx traces from Transcend DrivePro 220 videos")

    parser.add_argument('video', help="Video file to extract GPS traces from")

    args = parser.parse_args()

    # it looks like we get about 8 bytes for every minute of the
    # video, but it's not clear what those bytes correspond to
    # yet
    data = get_gps_data(args.video)

    for row in data:
        print(row)
