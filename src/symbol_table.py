#! /usr/bin/env python

## so, let's implement the symbol table.
## Symbol tables are meant to help in storing and retrieving register addresses pretty quickly
## Using dictionaries to keep track of identifier names and locations with the token type suffixed with
## an integer to count the identifier will help in keeping track of the variables
from typing import NoReturn, Union

class SymbolTable:

    def __init__(self) -> None:
        self.table = {}

    def add(self, count: int, id_name: str, loc: Union[int, NoReturn]) -> None:
        """Add an identifier to the symbol table."""
        for k, v in self.table.items():
            if id_name in v:
                return
        self.table['id'+str(count)] = (id_name, loc)

    def get(self, label: str) -> tuple:
        """Get the name and location of an identifier indicated by the input token label from the symbol table."""
        return self.table.get(label, (None, None))