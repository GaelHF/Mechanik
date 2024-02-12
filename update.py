import requests
import json

current_version = "v1.5.0"
current_version = current_version.replace("v", "")
current_version = current_version.replace(".", "")

request = requests.get("https://api.github.com/repos/gaelhf/mechanik/releases/latest")
data = request.content
data = json.loads(data)

version = data["tag_name"]
version = version.replace("v", "")
version = version.replace(".", "")

def is_update_available():
    if int(version) > int(current_version):
        return True
    else:
        return False

def get_new_version():
    return int(version)