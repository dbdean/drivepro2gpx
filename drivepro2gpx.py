#!/usr/bin/env python3

import base64
import exiftool

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(
        description="Extracts gpx traces from Transcend DrivePro 220 videos")

    parser.add_argument('video', help="Video file to extract GPS traces from")

    args = parser.parse_args()

    with exiftool.ExifTool() as et:
        gps = et.get_tag('Unknown_gps', args.video)

    assert gps.startswith('base64:')

    gps = base64.b64decode(gps[len('base64:'):])

    # it looks like we get about 8 bytes for every minute of the
    # video, but it's not clear what those bytes correspond to
    # yet
    for i in range(0, len(gps), 8):
        print(gps[i:i+8].hex())
