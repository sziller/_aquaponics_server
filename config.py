"""=== Public config file ==========================================================
Including settings for the Project, to be changed on or after install.
Not including sensitive data
================================================================== by Sziller ==="""
# Development settings:
isLIVE: bool                = True

# Language settings:
LANGUAGE_CODE = "EN"  # ["HU", "DE"]

# Path settings:
PATH_ROOT: str                  = "."
PATH_ERROR_MSG: str             = "{}/xdata/error.yaml"
PATH_APP_INFO: str              = "{}/xdata/aqua.yaml"

NECESSARY_DIRECTORIES: list     = ["./images", "./documentation", "./documents", "./log"]

# Log settings:
LOG_FORMAT: str                 = "%(asctime)s [%(levelname)8s]: %(message)s"
LOG_LEVEL: str                  = "DEBUG"  # NOTSET=0, DEBUG=10, INFO=20, WARNING=30, ERROR=40, CRITICAL=50
LOG_FILENAME: str               = "{}/log/srvr-aqua{}.log"  # location of logfile. 1st {} = ROOT_PATH, 2nd {} timestamp
LOG_TIMED: bool                 = False  # True: new log file created - stamp in name, False: no stamp, file overwritten
LOG_TIMEFORMAT: str             = "%y%m%d %H:%M:%S"

'''
Routers receive the following parameters passed on startup:
{
    <name>:                               # name of the router - key
        {   "use": bool,                       # if current router instance is used
            "prefix": str,                     # path prefix for current router
            "ip": str[xx.xx.xx.xx],            # ip address
            "zmq_port": int,                   # if socket comm. allowed to engine, use this port
            "arguments": {},                   # dict of {param: arg} pairs for current router instance
            "module": str ["xxx.xxx"],         # module out of which "router" obj is instantiated
            "description": "Information regarding router",
                "externalDocs": {
                    "description": "find additional info under: sziller.eu",
                    "url": "http://sziller.eu"
            },
    <name-02>:
        {},
    ...     }
'''

# App settings:
APP_ID: str                     = "aqua"
APP_IS_PROCESS_RUNNING: bool    = True

# list necessary router data here:
APP_ROUTER_INFO = {
    "aquaponics": {
        "use": True,
        "prefix": "/aqua",
        "zmq_port": 52008,
        "args": {"ip": 'localhost',
                 "port": 8042},
        "module": "shmc_routers.AquaRouter_class",
        "description": "Information regarding SmartHome setup's Aquaponic system",
        "externalDocs": {
            "description": "find additional info under: sziller.eu",
            "url": "http://sziller.eu"}}
    }

DEFAULT_USER_LIST       = [
    # 32char (128bit) hex-string representation of the UUID: double sha256 of the first email-address-string
    {   "uuid": "aa",  # uuid - self generated
        "usr_ln": 'Doe',
        "usr_fn": 'John',
        "pubkey": None,
        "email_list": 'JD@gmail.com',  # last email is the actual one [-1]
        "timestamp": 0.0,  # is added when user hits DB
        "authorization": 15},  # binary sum - 11111111 - fully authorized - TBD
    ]
