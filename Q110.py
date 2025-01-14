import logging

# Configure logging
logging.basicConfig(filename="app.log", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning.")
logging.error("This is an error.")
logging.critical("This is a critical message.")

print("Log messages have been written to app.log.")
