import setuptools
import yaml

PIP_CONFIG_FILE = "pip_config.yml"
KEY_NAME = "name"
KEY_VERSION = "version"
KEY_AUTHOR = "author"
KEY_AUTHOR_EMAIL = "author_email"
KEY_DESCRIPTION = "description"
KEY_LONG_DESCRIPTION_PATH = "long_description_path"
KEY_LONG_DESCRIPTION_CONTENT_TYPE = "long_description_content_type"
KEY_URL = "url"
KEY_CLASSIFIERS = "classifiers"
KEY_INSTALL_REQUIRES = "install_requires"

config = yaml.safe_load(open(PIP_CONFIG_FILE, "r"))

with open(config[KEY_LONG_DESCRIPTION_PATH], "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=config[KEY_NAME],
    version=config[KEY_VERSION],
    author=config[KEY_AUTHOR],
    author_email=config[KEY_AUTHOR_EMAIL],
    description=config[KEY_DESCRIPTION],
    long_description=long_description,
    long_description_content_type=config[KEY_LONG_DESCRIPTION_CONTENT_TYPE],
    url=config[KEY_URL],
    classifiers=config[KEY_CLASSIFIERS],
    install_requires=config[KEY_INSTALL_REQUIRES],
    packages=setuptools.find_packages()
)
