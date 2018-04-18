import logging
import logging.config
import logging.handlers
import json
# from config.config import LOGGING as logging_config_dict

from .check_iptv import Snmp
from .DateTime import DateTime
from .rabbitmq_queue import RabbitMQQueue

with open("setting/logging_configuration.json", 'r') as configuration_file:
    config_dict = json.load(configuration_file)
logging.config.dictConfig(config_dict)
# Create the Logger
logger = logging.getLogger(__name__)
