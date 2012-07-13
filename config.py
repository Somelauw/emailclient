import os
import json

try:
    import yaml
    hasYaml = True
except ImportError:
    hasYaml = False

class Config(object):
    def __init__(self, config):
        # Try each config file until it exists
        for config_dir in config_dirs():
            for ext in ["json", "yaml"]:
                filepath = "%s/cursemail/%s.%s" % (config_dir, config, ext)
                print filepath
                try:
                    self.load_config("%s/%s" % (config_dir, filepath))
                    print filepath
                    return
                except IOError:
                    # File doesn't exist. Continue with next one.
                    pass
        else:
            raise ConfigError("No config file found")

    def create_config(self, filename):
        #os.touch(next(config_dirs()) + "/cursemail/config.json")
        pass # TODO

    def load_config(self, filename):
            (_, ext) = os.path.splitext(filename)
            with open(filename) as configdata:
                self.config_filename = filename
                if ext == ".yaml":
                    if hasYaml:
                        self.config = yaml.load(configdata)
                    else:
                        raise ConfigWarning(
                                "file %s found, but pyyaml was not installed" % filename)
                elif ext == ".json":
                    self.config = json.load(configdata)
                else:
                    raise ConfigError("Unknown file format %s" % filename)

def config_dirs():
    # Use xdg standards to find a place to put the config file
    yield os.environ.get("XDG_CONFIG_HOME", os.environ["HOME"] + "/.config")

    for config in os.environ.get("XDG_CONFIG_DIRS", "/etc/xdg").split(":"):
        yield config

    yield "."

class ConfigError(Exception):
    pass

class ConfigWarning(Warning):
    pass

if __name__ == "__main__":
    #print "config", getConfig("email")
    pass

