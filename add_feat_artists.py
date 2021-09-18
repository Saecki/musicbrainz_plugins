PLUGIN_NAME = "#add feat. artists"
PLUGIN_AUTHOR = "Lukas Lalinsky, Michael Wiencek, Bryan Toth, JeromyNix (NobahdiAtoll)"
PLUGIN_DESCRIPTION = "Add 'feat.' or 'ft.' from artist names or album and track titles as artists. Match is case insensitive."
PLUGIN_VERSION = "0.1.0"
PLUGIN_API_VERSIONS = ["2.0", "2.1", "2.2", "2.3"]

from picard.metadata import register_album_metadata_processor, register_track_metadata_processor
import re

_feat_re = [
    re.compile(r"(.+?)\s*feat\.\s*(.+)", re.IGNORECASE),
    re.compile(r"(.+?)\s*ft\.\s*(.+)", re.IGNORECASE)
]


def split_artists(string):
    artists = string.split("&")
    return [a.strip() for a in artists]


def _add_feat_artists(metadata, artist_key, other_keys):
    artists = metadata.getall(artist_key)

    for r in _feat_re:
        for i,v in enumerate(artists):
            match = r.match(v)
            if match:
                artists[i] = match.group(1)
                new = split_artists(match.group(2))
                artists.extend(new)

        for k in other_keys:
            match = r.match(metadata[k])
            if match:
                metadata[k] = match.group(1)
                new = split_artists(match.group(2))
                artists.extend(new)

    metadata.set(artist_key, artists)


def add_album_feat_artists(tagger, metadata, release):
    _add_feat_artists(metadata, "albumartist", ["album"])


def add_track_feat_artists(tagger, metadata, track, release):
    _add_feat_artists(metadata, "artist", ["title"])


register_album_metadata_processor(add_album_feat_artists)
register_track_metadata_processor(add_track_feat_artists)

