#!/usr/bin/env sh

# Setup the style of color
COLOR_RED='\033[0;31m'
COLOR_YELLOW='\033[0;33m'
COLOR_NC='\033[0m'

filename=$1
if [ $# -gt 0 ]; then
    ffmpeg -i "$1" -pix_fmt yuv420p -c:a copy -movflags +faststart "${filename%.*}_windows_compatible.mp4"
else
    echo -e "${COLOR_RED}Usage: source convert_kazam_video [YOUR_VIDEO_FILE]1a${COLOR_NC}"
fi

# how to use it
# source convert_kazam_video.sh videoname.mp4 
