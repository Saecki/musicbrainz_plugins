PLUGIN_NAME = "#remove other tags"
PLUGIN_AUTHOR = "Saecki"
PLUGIN_DESCRIPTION = 'Remove all tags apart from the ones specified.'
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["2.0", "2.1", "2.2", "2.3"]

from picard.metadata import register_track_metadata_processor, register_album_metadata_processor

wanted_tags = (
    "title",
    "artist",
    "albumartist",
    "album",
    "date",
    "genre",
    "encodedby",
    "tracknumber",
    "totaltracks",
    "disknumber",
    "totaldisks",
    "length",
)


def album_remove_unwanted_tags(tagger, metadata, release):
    for m in metadata:
        if m not in wanted_tags:
            metadata.deleted_tags.add(m)


def track_remove_unwanted_tags(tagger, metadata, track, release):
    for m in metadata:
        if m not in wanted_tags:
            metadata.deleted_tags.add(m)


register_album_metadata_processor(album_remove_unwanted_tags)
register_track_metadata_processor(track_remove_unwanted_tags)
