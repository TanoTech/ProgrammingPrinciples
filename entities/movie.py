from dataclasses import dataclass
from typing import List

@dataclass
class Movie:
    title: str
    director: str
    year: int
    genres: List[str]

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "director": self.director,
            "year": self.year,
            "genres": self.genres
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Movie':
        return cls(
            title=data["title"],
            director=data["director"],
            year=data["year"],
            genres=data["genres"]
        )