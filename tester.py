import logging

# https://stackoverflow.com/questions/15474095/writing-a-log-file-from-python-program

LOG = "/tmp/ccd.log"
logging.basicConfig(filename="log_output", filemode="w", level=logging.DEBUG)

# console handler
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
logging.getLogger("").addHandler(console)

logging.debug("This is from logging  output")
logging.warning("This is from Warning")