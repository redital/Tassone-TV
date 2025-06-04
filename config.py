import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "mysecretkey")

MEDIA_DIR_NAME = os.environ.get("MEDIA_DIR_NAME","placeholder")
STATE_FILE_NAME = os.environ.get("STATE_FILE_NAME","placeholder")
CHANNELS_FILE_NAME = os.environ.get("CHANNELS_FILE_NAME","placeholder")

MEDIA_ROOT = os.path.join(os.getcwd(), MEDIA_DIR_NAME)
STATE_PATH = os.path.join(os.getcwd(), STATE_FILE_NAME)
CHANNELS_PATH = os.path.join(os.getcwd(), CHANNELS_FILE_NAME)

DASHBOARD_HOSTNAME = os.environ.get("DASHBOARD_HOSTNAME","placeholder")



flask_app_config = {
    "debug": os.environ.get("FLASK_DEBUG_OPTION", True),
    "use_reloader": os.environ.get("FLASK_RELOADER_OPTION", False),
    "host": os.environ.get("FLASK_HOST", "0.0.0.0"),
    "port": os.environ.get("FLASK_PORT", 5000),
}
flask_app_init = {
    "static_url_path":  '/{}'.format(MEDIA_DIR_NAME),
    "static_folder":  MEDIA_DIR_NAME,
}