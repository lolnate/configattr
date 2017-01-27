import os
import configparser

from configattr.objects import Dictionary

class Config:
    """Configuration file parser."""

    def __init__(self, config_path=None):
        """
        @param config_path: configuration file path.
        """
        config = configparser.ConfigParser()

        if config_path is not None:
            config.read(config_path)
        else:
            config.read('config.ini')

        self.fullconfig = config._sections

        for section in config.sections():
            setattr(self, section, Dictionary())
            for name, raw_value in config.items(section):
                try:
                    # Ugly fix to avoid '0' and '1' to be parsed as a
                    # boolean value.
                    # We raise an exception to goto fail^w parse it
                    # as integer.
                    if config.get(section, name) in ["0", "1"]:
                        raise ValueError

                    value = config.getboolean(section, name)
                except ValueError:
                    try:
                        value = config.getint(section, name)
                    except ValueError:
                        value = config.get(section, name)

                setattr(getattr(self, section), name, value)


    def get(self, section):
        """Get option.
        @param section: section to fetch.
        @return: option value.
        """
        return getattr(self, section)

    def get_config(self):
        return self.fullconfig
