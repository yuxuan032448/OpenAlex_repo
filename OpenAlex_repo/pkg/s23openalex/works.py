"""Module providing a Works class and bibtex, RIS attributes."""
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser import dumps
import requests


class Works:
    """OpenAlex Works class."""

    def __init__(self, oaid):
        self.oaid = oaid
        self.req = requests.get(f"https://api.openalex.org/works/{oaid}", timeout=10)
        self.data = self.req.json()

    def __str__(self):
        return "str"

    def __repr__(self):
        return "repr"

    @property
    def bibtex(self):
        """Print formatted Bibtex entry."""
        _authors = [au["author"]["display_name"] for au in self.data["authorships"]]
        if len(_authors) == 0:
            authors = "Editorial"
        elif len(_authors) == 1:
            authors = _authors[0]
        else:
            authors = ", ".join(_authors[0:-1]) + " and" + _authors[-1]

        pages = "-".join(
            [
                self.data["biblio"].get("first_page", "") or "",
                self.data["biblio"].get("last_page", "") or "",
            ]
        )

        database = BibDatabase()
        database.entries = [
            {
                "ID": self.data["id"],
                "title": self.data["title"],
                "author": authors,
                "journal": self.data["host_venue"]["display_name"],
                "volume": self.data["biblio"]["volume"],
                "number": self.data["biblio"]["issue"],
                "pages": pages,
                "year": str(self.data["publication_year"]),
                "url": self.data["doi"],
                "ENTRYTYPE": self.data["type"],
            }
        ]
        writer = BibTexWriter()
        bibtex = dumps(database, writer)
        return bibtex

    @property
    def ris(self):
        """Print RIS entry."""
        fields = []
        if self.data["type"] == "journal-article":
            fields += ["TY  - JOUR"]
        else:
            raise ValueError("Unsupported type {self.data['type']}")

        for author in self.data["authorships"]:
            fields += [f'AU  - {author["author"]["display_name"]}']

        fields += [f'PY  - {self.data["publication_year"]}']
        fields += [f'TI  - {self.data["title"]}']
        fields += [f'JO  - {self.data["host_venue"]["display_name"]}']
        fields += [f'VL  - {self.data["biblio"]["volume"]}']

        if self.data["biblio"]["issue"]:
            fields += [f'IS  - {self.data["biblio"]["issue"]}']

        fields += [f'SP  - {self.data["biblio"]["first_page"]}']
        fields += [f'EP  - {self.data["biblio"]["last_page"]}']
        fields += [f'DO  - {self.data["doi"]}']
        fields += ["ER  -"]

        ris = "\n".join(fields)
        return ris
