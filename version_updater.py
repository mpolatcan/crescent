from sys import argv
import yaml

VERSION_TYPE_PATCH = "patch"
VERSION_TYPE_MINOR = "minor"
VERSION_TYPE_MAJOR = "major"
KEY_VERSION = "version"
PIP_CONFIG_FILE = "pip_config.yml"

if __name__ == "__main__":
    version_type = argv[1]
    config = yaml.safe_load(open(PIP_CONFIG_FILE, "r"))

    version_numbers = [int(version_number) for version_number in config[KEY_VERSION].split(".")]

    if version_type == VERSION_TYPE_PATCH:
        version_numbers[2] += 1
    elif version_type == VERSION_TYPE_MINOR:
        version_numbers[1] += 1
    elif version_type == VERSION_TYPE_MAJOR:
        version_numbers[0] += 1
    else:
        raise Exception("Invalid version type: {}".format(version_type))

    version_numbers = [str(version_number) for version_number in version_numbers]

    config[KEY_VERSION] = ".".join(version_numbers)

    yaml.dump(config, open(PIP_CONFIG_FILE, "w"))
