
class ConfigApi:
    def __init__(self):
        with open("config.toml", "r") as f:
            lines = f.readlines()

        for line in lines:
            if line.startswith("app_url"):
                self.app_url = line.split("=")[1]
