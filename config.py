import os
import json

try:
    import yaml
    hasYaml = True
except ImportError:
    hasYaml = False

class Config(object):
    def __init__(self, config):
        configfiles = config_locations(config)

        # Now try each config file until it exists
        for filename in configfiles:
            try:
                self.load_config(filename)
                break
            except IOError:
                # File doesn't exist. Continue with next one.
                pass
        else:
            raise ConfigError("No config file found")

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

def config_locations(configname):
    exts = [".yaml", ".json"]

    # Find the local config
    localconfig = os.environ.get("XDG_CONFIG_HOME", 
            os.environ["HOME"] + "/.config") + "/cursemail/"
    otherconfigs = [config + "/cursemail/" 
            for config in os.environ.get("XDG_CONFIG_DIRS", "/etc/xdg/").split(":")]
    configdirs = [localconfig] + otherconfigs + ["./"]

    # Also try some other config locations
    configfiles = [configdir + configname + ext 
            for configdir in configdirs
            for ext in exts]

    return configfiles

class ConfigError(Exception):
    pass

class ConfigWarning(Warning):
    pass

if __name__ == "__main__":
    #print "config", getConfig("email")
    pass

