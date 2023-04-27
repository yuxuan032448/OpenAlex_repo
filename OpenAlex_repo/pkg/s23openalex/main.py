"""Python file for command line utility."""

import sys
sys.path.append('.')
from works import Works


def main(oaid, entry):
    """Take oaid and type to output RIS or Bibtex entry."""
    work = Works(oaid)
    if entry == "ris":
        print(work.ris)
    elif entry == "bibtex":
        print(work.bibtex)


# main("https://doi.org/10.1021/acscatal.5b00538","bibtex")
# main("https://doi.org/10.1021/acscatal.5b00538","ris")
