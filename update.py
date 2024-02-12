import requests
import json

current_version = "v1.5.0"
current_version_m = current_version.replace("v", "")
current_version_m = current_version_m.replace(".", "")

request = requests.get("https://api.github.com/repos/gaelhf/mechanik/releases/latest")
data = request.content
data = json.loads(data)

version = data["tag_name"]

version_m = version.replace(".", "")
version_m = version_m.replace("v", "")

def is_update_available():
    if int(version_m) > int(current_version_m):
        return True
    else:
        return False

def get_new_version():
    return str(version)