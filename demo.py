

from mlops.logger import logging
from mlops.exception import MLOpsInsuranceException
import sys

#logging.info("This is an info message.")

try:
    a = 1 / 0
except Exception as e:
    raise MLOpsInsuranceException(e, sys) from e