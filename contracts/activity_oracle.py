# { "Depends": "py-genlayer:test" }
from genlayer import *
import json

class ActivityOracle(gl.Contract):
    """
    GenLayer Character Oracle (Rick & Morty Edition)
    Fetches deterministic character lore from the 
    Rick and Morty API to generate consistent quest NPCs.
    """
    last_character: str

    def __init__(self):
        self.last_character = ""

    @gl.public.write
    def fetch_activity(self, char_id: str) -> str:
        if char_id == "" or char_id == "0": char_id = "1"
        
        # Using Rick and Morty API (Deterministic by ID)
        url = "https://rickandmortyapi.com/api/character/" + char_id

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            try:
                body_str = response.body.decode("utf-8")
                data = json.loads(body_str)
                
                name = data.get("name", "Unknown Traveler")
                species = data.get("species", "Unknown Species")
                status = data.get("status", "Unknown Status")
                return name + "|" + species + "|" + status
            except Exception:
                return "A glitched character from another dimension."

        result = gl.eq_principle.strict_eq(_fetch)
        parts = result.split("|")
        self.last_character = parts[0]
        return "Character Lore: " + parts[0] + " is a " + parts[1] + " (" + parts[2] + ")"

    @gl.public.view
    def get_last_character(self) -> str:
        return self.last_character
