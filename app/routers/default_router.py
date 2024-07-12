import logging

import json
from pathlib import Path
from fastapi import APIRouter, Response

logger = logging.getLogger(__name__)
router = APIRouter()

# https://www.patorjk.com/software/taag/#p=display&f=Doom&t=qualification%20%20register%20%20api
LOGO = r"""
                   _ _  __ _           _   _                               _     _                           _ 
                  | (_)/ _(_)         | | (_)                             (_)   | |                         (_)
  __ _ _   _  __ _| |_| |_ _  ___ __ _| |_ _  ___  _ __     _ __ ___  __ _ _ ___| |_ ___ _ __     __ _ _ __  _ 
 / _` | | | |/ _` | | |  _| |/ __/ _` | __| |/ _ \| '_ \   | '__/ _ \/ _` | / __| __/ _ \ '__|   / _` | '_ \| |
| (_| | |_| | (_| | | | | | | (_| (_| | |_| | (_) | | | |  | | |  __/ (_| | \__ \ ||  __/ |     | (_| | |_) | |
 \__, |\__,_|\__,_|_|_|_| |_|\___\__,_|\__|_|\___/|_| |_|  |_|  \___|\__, |_|___/\__\___|_|      \__,_| .__/|_|
    | |                                                               __/ |                           | |      
    |_|                                                              |___/                            |_|      
"""


@router.get("/", include_in_schema=False)
def index() -> Response:
    content = LOGO

    try:
        with open(Path(__file__).parent.parent.parent / "version.json", "r") as file:
            data = json.load(file)
            content += "\nVersion: %s\nCommit: %s" % (data["version"], data["git_ref"])
    except BaseException as e:
        content += "\nNo version information found"
        logger.info("Version info could not be loaded: %s" % e)

    return Response(content)
