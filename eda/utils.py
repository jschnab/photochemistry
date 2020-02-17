import functools
import logging
import os
import sys
import traceback

from pathlib import Path

HOME = str(Path.home())

logging.basicConfig(
    filename=f"{HOME}/eda_errors.log",
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.DEBUG,
)


def log_errors(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            exc_type, exc_value, _ = sys.exc_info()
            traceback_msg = traceback.format_exc()
            print(f"Error: {exc_type.__name__} {exc_value}")
            logging.error(f"{exc_type.__name__} {exc_value} {traceback_msg}")
            sys.exit(1)
    return wrapper


@log_errors
def linuxize_newlines(input_name, output_name):
    """
    Makes a copy of a file and ensure Unix newline characters.

    :param str input_name: name of the file to process
    :param str output_name: name of the file copy with Unix newlines
    """
    with open(input_name, "rb") as infile:
        lines = infile.readlines()
        with open(output_name, "wb") as outfile:
            for line in lines:
                line = line[:-3] + os.linesep.encode()
                outfile.write(line)


@log_errors
def get_number_lines(path):
    """
    Get the number of lines in a file.

    :param str path: path to the file to process
    :return int: number of line in the file
    """
    n = 0
    with open(path) as f:
        for line in f:
            n += 1
    return n


@log_errors
def get_end_of_data(path):
    """
    Get the index of the line where data ends in a CSV file.
    The end of data is defined as the first blank line.

    :param str path: path to the file to process
    :return int: index of the line where data ends
    """
    end_of_data = 0
    with open(path) as f:
        for line in f:
            end_of_data += 1
            if line.strip() == "":
                break
    return end_of_data