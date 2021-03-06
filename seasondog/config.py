import os

DB_PATH = os.path.join(os.path.expanduser("~"), ".seasondog", "database")
PLAYER = "mplayer -lavdopts threads=4 -fs {player_args} \"{videofile}\""
SUB_EXTENSIONS = ["srt", "ass", "aqt", "gsub", "sub", "ttxt", "pjs", "psb", "rt", "stl", "ssa", "usf", "idx", ]
MOVIE_EXTENSIONS = ["mov", "mpg", "mpeg", "m2v", "mkv", "webm", "ogm", "mp4", "m4v", "mp4v", "vob", "qt", "nuv", "wmv", "asf", "rm", "rmvb", "flc", "avi", "fli", "flv", "gl", "dl", "xcf", "xwd", "yuv", "cgm", "emf", ]
PREFIXES = ["episode", "ep", "e", "x"]
SURROUNDINGS = [" ", "", "_"]

COLORS = {
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "grey": "\033[90m",
    "red": "\033[91m",

    "bold": "\033[1m",

    "endc": "\033[0m",
}

COLORS.update({
    "c_title": COLORS["grey"],
    "c_ep_number": COLORS["blue"] + COLORS["bold"],
    "c_path": COLORS["blue"],
    "c_args": COLORS["blue"],
    "c_control": COLORS["grey"],
    "c_success": COLORS["green"],
    "c_error": COLORS["red"],
})

USE_COLORS = True

MATCHER_DEBUG = False

try:
    exec(open(os.path.join(os.path.expanduser("~"), ".sdogrc")).read())
except FileNotFoundError:
    pass

if not USE_COLORS:
    c = {}
    for k, v in COLORS.items():
        c[k] = ""

    COLORS = c
