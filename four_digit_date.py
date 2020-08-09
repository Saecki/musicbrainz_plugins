PLUGIN_NAME = "#4 digit date"
PLUGIN_AUTHOR = "Saecki"
PLUGIN_DESCRIPTION = "Shorten the release date to 4 digits to only display the year."
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["2.0", "2.1", "2.2", "2.3"]

from picard.metadata import register_track_metadata_processor


def track_4_digit_date(tagger, metadata, track, release):
    date = metadata["date"]
    if len(date) > 4:
        metadata["date"] = date[:4]


register_track_metadata_processor(track_4_digit_date)
