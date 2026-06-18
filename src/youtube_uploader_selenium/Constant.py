import re


class Constant:
    """A class for storing constants for YoutubeUploader class"""

    YOUTUBE_URL = "https://www.youtube.com"
    YOUTUBE_STUDIO_URL = "https://studio.youtube.com"
    YOUTUBE_UPLOAD_URL = "https://www.youtube.com/upload"
    USER_WAITING_TIME = 1

    # Login check: avatar button present on youtube.com when logged in
    USER_AVATAR_XPATH = "//button[@id='avatar-btn']"

    VIDEO_TITLE = "title"
    VIDEO_DESCRIPTION = "description"
    PLAYLIST = "playlist"
    TAGS = "tags"
    NOTIFY_SUBS = "notify_subs"

    # Upload dialog fields — relative XPaths keyed on stable component names
    DESCRIPTION_CONTAINER = "//ytcp-social-suggestions-textbox"
    # "Show more" / "More options" toggle button in the details step
    MORE_OPTIONS_CONTAINER = "//ytcp-button[@id='toggle-button']"

    # Playlist dropdown trigger inside the upload dialog
    PLAYLIST_CONTAINER = "//ytcp-video-metadata-playlists//ytcp-text-dropdown-trigger"

    # Elements inside the playlist management dialog
    PLAYLIST_SEARCH = "//ytcp-playlist-dialog//input"
    PLAYLIST_SEARCH_CLEAR_BUTTON = "//ytcp-playlist-dialog//ytcp-icon-button"
    PLAYLIST_NEW_BUTTON = "//ytcp-playlist-dialog//ytcp-button[1]"
    PLAYLIST_NEW_TITLE = "//ytcp-playlist-dialog//ytcp-form-textarea//textarea"
    PLAYLIST_DONE_BUTTON = "//ytcp-playlist-dialog//ytcp-button[@id='save-button']"
    PLAYLIST_CREATE_BUTTON = "//ytcp-playlist-dialog//ytcp-button[@id='create-playlist-button']"
    PLAYLIST_VISIBILITY_DROPDOWN = "//ytcp-playlist-dialog//ytcp-dropdown"
    PLAYLIST_LABEL = "//label[./span/span[@class='label label-text style-scope ytcp-checkbox-group']]"

    TOOLTIP = "//ytcp-paper-tooltip"

    # Tags chip-bar input
    TAGS_TEXT_INPUT = "//ytcp-free-text-chip-bar//input"

    # Notify subscribers checkbox
    NOTIFY_SUBSCRIBERS_CHECKBOX = "//ytcp-checkbox-lit[@id='notify-subscribers']"

    TEXTBOX = "textbox"
    TEXT_INPUT = "text-input"
    RADIO_LABEL = "radioLabel"

    # Upload progress span inside the upload dialog
    STATUS_CONTAINER = "//ytcp-video-upload-progress/span"

    # "Not made for kids" radio button — identified by its name attribute (stable)
    NOT_MADE_FOR_KIDS = "//tp-yt-paper-radio-button[@name='VIDEO_MADE_FOR_KIDS_NOT_MFK']"

    NEXT_BUTTON = "next-button"
    VIDEO_URL_CONTAINER = "//span[@class='video-url-fadeable style-scope ytcp-video-info']"
    VIDEO_URL_ELEMENT = "//ytcp-uploads-review//ytcp-video-info//a"
    UPLOADED = "Uploading"
    ERROR_CONTAINER = '//*[@id="error-message"]'
    DONE_BUTTON = "done-button"
    INPUT_FILE_VIDEO = "//input[@type='file']"
    USERNAME_ID = "account-name"
    VIDEO_PUBLISHED_DIALOG = '//*[@id="dialog-title"]'

    PROGRESS_REGEX = re.compile(r"Uploading (?P<progress>\d+)%.*")

    MAX_TITLE_LENGTH = 100
    MAX_DESCRIPTION_LENGTH = 5000
    MAX_TAGS_LENGTH = 500

    @staticmethod
    def lookup(s):
        for name, value in vars(Constant).items():
            if s == value:
                return name
        return value
