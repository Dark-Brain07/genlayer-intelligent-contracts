# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *
import json


class CryptoPriceOracle(gl.Contract):
    """Fetches cryptocurrency prices from CoinGecko's public API and stores
    them on-chain. Useful for DeFi protocols, lending platforms, and price
    alerts. Validators use the equivalence principle to reach consensus on
    the canonical price even though timestamps may differ slightly."""

    prices: TreeMap[str, str]

    def __init__(self):
        pass

    @gl.public.write
    def fetch_price(self, coin_id: str) -> str:
        """Fetch the latest USD price for a coin from CoinGecko.

        Args:
            coin_id: CoinGecko coin ID (e.g. "bitcoin", "ethereum", "solana")
        """
        api_url = (
            f"https://api.coingecko.com/api/v3/simple/price"
            f"?ids={coin_id}&vs_currencies=usd&include_24hr_change=true"
        )

        def fetch_and_round() -> str:
            raw = gl.nondet.web.get(api_url)
            try:
                data = json.loads(raw)
                if coin_id not in data:
                    return f"{coin_id}|not_found|0"

                coin_data = data[coin_id]
                price = coin_data.get("usd", 0)
                # Round to integer USD cents for deterministic consensus
                price_cents = int(price * 100)
                change_24h = coin_data.get("usd_24h_change", 0)
                change_bps = int(change_24h * 100)  # basis points

                return f"{coin_id}|{price_cents}|{change_bps}"
            except Exception:
                return f"{coin_id}|error|0"

        result = gl.eq_principle.strict_eq(fetch_and_round)
        self.prices[coin_id] = result
        return result

    @gl.public.write
    def check_price_alert(self, coin_id: str, threshold_usd: int, direction: str) -> bool:
        """Check if a coin's price has crossed a threshold.

        Args:
            coin_id: The coin to check (must be previously fetched)
            threshold_usd: Price threshold in USD (whole dollars)
            direction: "above" or "below"
        """
        if coin_id not in self.prices:
            raise Exception("PRICE_NOT_FETCHED: " + coin_id)

        price_data = self.prices[coin_id]
        parts = price_data.split("|")
        if len(parts) < 2 or parts[1] == "error" or parts[1] == "not_found":
            raise Exception("INVALID_PRICE_DATA: " + coin_id)

        price_cents = int(parts[1])
        threshold_cents = threshold_usd * 100

        if direction == "above":
            return price_cents > threshold_cents
        elif direction == "below":
            return price_cents < threshold_cents
        else:
            raise Exception("INVALID_DIRECTION: Must be 'above' or 'below'")

    @gl.public.view
    def get_price(self, coin_id: str) -> str:
        if coin_id not in self.prices:
            raise Exception("COIN_NOT_FETCHED: " + coin_id)
        return self.prices[coin_id]
