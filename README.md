# GenLayer Intelligent Contracts Collection

A collection of real-world intelligent contracts demonstrating GenLayer's unique capability: **combining live web data with AI consensus on-chain**. Each contract uses `gl.nondet.web.get()` to fetch data from public APIs and `gl.eq_principle.strict_eq` to reach deterministic consensus across validators.

## Contracts

| Contract | Use Case | Key Features |
|----------|----------|--------------|
| [football_score_oracle.py](contracts/football_score_oracle.py) | Live football match scores | Web fetch + canonical score format |
| [cricket_score_oracle.py](contracts/cricket_score_oracle.py) | Cricket scores with winner AI reasoning | Web fetch + AI judgment |
| [github_verifier.py](contracts/github_verifier.py) | Developer identity verification | GitHub API + wallet binding |
| [weather_oracle.py](contracts/weather_oracle.py) | Real-time weather data | Weather API + AI threshold checks |
| [crypto_price_oracle.py](contracts/crypto_price_oracle.py) | Crypto price feeds | CoinGecko API + price alerts |
| [news_fact_checker.py](contracts/news_fact_checker.py) | AI-powered fact checking | Web content + AI reasoning |

## Why GenLayer?

Traditional smart contracts can't:
- Fetch live data from public APIs (no web access)
- Make subjective judgments (no AI reasoning)
- Handle non-deterministic inputs (validators would disagree)

GenLayer solves this with **Optimistic Democracy** — validators connected to diverse LLMs reach consensus on subjective outcomes via the equivalence principle.

## Pattern: Web Fetch + AI Consensus

Every contract follows this pattern:

```python
def fetch_and_parse() -> str:
    raw = gl.nondet.web.get(api_url)
    # Parse and canonicalize for deterministic consensus
    data = json.loads(raw)
    return f"{field1}|{field2}|{field3}"  # pipe-delimited

result = gl.eq_principle.strict_eq(fetch_and_parse)
self.storage[key] = result
```

The canonical pipe-delimited format ensures all validators agree even if the API returns fields in different orders or includes extra metadata.

## Deployment

All contracts deploy to GenLayer Studionet at [studio.genlayer.com](https://studio.genlayer.com). Each contract has no constructor dependencies, so they can be deployed independently.

```bash
# Via GenLayer CLI
genlayer deploy contracts/football_score_oracle.py
```

Or paste the contract source into GenLayer Studio's web UI.

## Network

- **RPC:** https://studio.genlayer.com/api
- **Chain ID:** 61999
- **Explorer:** https://explorer-studio.genlayer.com
