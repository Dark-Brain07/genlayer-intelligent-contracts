# { "Depends": "py-genlayer:test" }
from genlayer import *
import json

class CocktailOracle(gl.Contract):
    """
    GenLayer Cocktail Oracle
    Fetches cocktail recipes for in-game item crafting.
    """
    last_drink: str

    def __init__(self):
        self.last_drink = ""

    @gl.public.write
    def fetch_cocktail(self, name: str) -> str:
        if name == "": name = "Margarita"
        url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + name

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.body.decode("utf-8"))
            
            # Check if any drinks were found
            if data.get("drinks") is not None:
                drink = data["drinks"][0]["strDrink"]
                instructions = data["drinks"][0]["strInstructions"]
                return drink + "|" + instructions
            else:
                return "Potion Failure|The requested elixir was not found in the ancient archives."

        result = gl.eq_principle.strict_eq(_fetch)
        parts = result.split("|")
        self.last_city = parts[0]
        return "Alchemy Recipe for " + parts[0] + ": " + parts[1]

    @gl.public.view
    def get_last_drink(self) -> str:
        return self.last_drink
