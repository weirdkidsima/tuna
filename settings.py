
class Settings:
    COMPILED_APP_MODE = False

    """ general settings """
    APP_NAME = "GuitarTuner"
    VERSION = "3.2"
    AUTHOR = "Weirdkidsima"
    YEAR = "2023"


    STATISTICS_AGREEMENT = f"{APP_NAME} tracks how often the app is being opened.\n\n" + \
                           "Do you agree on sending this anonymous data?"

    USER_SETTINGS_PATH = "/assets/user_settings/user_settings.json"

    ABOUT_TEXT = "{} Version {}  © {} {}".format(APP_NAME, VERSION, YEAR, AUTHOR)

    WIDTH = 450
    HEIGHT = 440

    MAX_WIDTH = 600
    MAX_HEIGHT = 500

    FPS = 60
    CANVAS_SIZE = 300

    NEEDLE_BUFFER_LENGTH = 30
    HITS_TILL_NOTE_NUMBER_UPDATE = 15