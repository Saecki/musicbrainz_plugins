#!/bin/sh

TARGET_DIR="${HOME}/.config/MusicBrainz/Picard/plugins/"
mkdir -p "$TARGET_DIR"
cp ./*.py "$TARGET_DIR"
