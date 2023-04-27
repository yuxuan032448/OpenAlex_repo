"""Python file for command line utility."""

from s23openalex import Works


def main(oaid, entry):
    """Take oaid and type to output RIS or Bibtex entry."""
    work = Works(oaid)
    if entry == "ris":
        print(work.ris)
    elif entry == "bibtex":
        print(work.bibtex)


# main("https://doi.org/10.1021/acscatal.5b00538","bibtex")
# main("https://doi.org/10.1021/acscatal.5b00538","ris")
