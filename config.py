import os
import json

try:
    import yaml
    hasYaml = True
except ImportError:
    hasYaml = False

def readConfig(configFiles):
    for fileName in configFiles:
        (_, ext) = os.path.splitext(fileName)
        try:
            with open(fileName) as configData:
                if ext == "yaml":
                    if hasYaml:
                        return yaml.load(configData)
                    else:
                        raise ConfigWarning(
                                "file %s found, but pyyaml was not installed" % fileName)
                elif ext == "json":
                    return json.load(configData)
        except IOError:
            pass
    return None

class ConfigError(Exception):
    pass

class ConfigWarning(Warning):
    pass

if __name__ == "__main__":
    pass

