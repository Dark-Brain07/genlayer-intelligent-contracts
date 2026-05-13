# GenLayer Intelligent Contracts — Submission

## Project: Real-World Data Oracles & AI Verification Suite

A collection of 6 production-ready intelligent contracts demonstrating GenLayer's core strengths: fetching live web data, parsing it deterministically, and making AI-powered judgments on-chain.

---

## Intelligent Contracts

#### 1. Football Score Oracle

**Title:** Live Football Match Score Oracle

**Description:**

An intelligent contract that fetches live football match scores from public sports APIs using `gl.nondet.web.get()`. The JSON response is parsed and canonicalized into a pipe-delimited format (`home_team|home_score|away_team|away_score|status`) so all validators reach consensus via `gl.eq_principle.strict_eq` even if the API includes varying metadata. Useful for sports betting dApps, fantasy leagues, or parametric insurance products.

- **Contract Address:** `<fill in after deployment>`

- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/<fill in after deployment>)

- **Source Code:** [football_score_oracle.py](https://github.com/Dark-Brain07/genlayer-intelligent-contracts/blob/main/contracts/football_score_oracle.py)

---

#### 2. Cricket Score Oracle

**Title:** Cricket Match State Tracker with AI Winner Determination

**Description:**

A cricket-specific oracle that tracks innings, overs, and wickets from live match APIs. Goes beyond raw data fetching by combining `gl.nondet.web.get()` with `gl.nondet.exec_prompt()` to reason about match state and determine the winner — a subjective judgment that requires understanding cricket rules (follow-on, duckworth-lewis, etc.). Demonstrates GenLayer's unique ability to bridge structured data and AI reasoning.

- **Contract Address:** `<fill in after deployment>`

- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/<fill in after deployment>)

- **Source Code:** [cricket_score_oracle.py](https://github.com/Dark-Brain07/genlayer-intelligent-contracts/blob/main/contracts/cricket_score_oracle.py)

---

#### 3. GitHub Verifier

**Title:** Developer Identity Verification via GitHub API

**Description:**

Verifies a user's GitHub identity by fetching their profile from the public GitHub API and binding it to a wallet address on-chain. Stores canonical profile data (username, repos, followers, creation date) that validators agree on via the equivalence principle. Perfect for developer bounty platforms, on-chain reputation systems, or gated DAO access based on GitHub credentials.

- **Contract Address:** `<fill in after deployment>`

- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/<fill in after deployment>)

- **Source Code:** [github_verifier.py](https://github.com/Dark-Brain07/genlayer-intelligent-contracts/blob/main/contracts/github_verifier.py)

---

#### 4. Weather Oracle

**Title:** Real-Time Weather Data with AI Threshold Detection

**Description:**

Fetches live weather data for any city from weather APIs (Open-Meteo, OpenWeatherMap) and canonicalizes temperature, conditions, and humidity for on-chain consensus. Includes an AI-powered threshold check that uses `gl.nondet.exec_prompt()` to evaluate subjective conditions like "heavy rain" or "heat wave" — enabling parametric insurance contracts, agricultural derivatives, or weather-based event postponement.

- **Contract Address:** `<fill in after deployment>`

- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/<fill in after deployment>)

- **Source Code:** [weather_oracle.py](https://github.com/Dark-Brain07/genlayer-intelligent-contracts/blob/main/contracts/weather_oracle.py)

---

#### 5. Crypto Price Oracle

**Title:** CoinGecko Price Feed with On-Chain Alerts

**Description:**

Fetches cryptocurrency prices from CoinGecko's public API and stores them on-chain with USD cents precision for deterministic consensus. Includes a `check_price_alert` function that evaluates whether a coin has crossed a threshold in either direction, usable for triggering DeFi liquidations, limit orders, or push notifications. The basis-point storage of 24h change enables sophisticated alert logic without floating-point consensus issues.

- **Contract Address:** `<fill in after deployment>`

- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/<fill in after deployment>)

- **Source Code:** [crypto_price_oracle.py](https://github.com/Dark-Brain07/genlayer-intelligent-contracts/blob/main/contracts/crypto_price_oracle.py)

---

#### 6. News Fact Checker

**Title:** AI-Powered On-Chain Fact Verification

**Description:**

The flagship contract for GenLayer's AI consensus. Fetches article content from a URL, truncates to a manageable snippet, and asks the AI to evaluate a factual claim against the source — returning a structured JSON verdict (`true`/`false`/`partial`/`insufficient_evidence`) with a confidence score. Validators reach consensus on subjective fact-checking judgments that are fundamentally impossible on traditional blockchains. Use cases: prediction markets, misinformation detection, on-chain journalism.

- **Contract Address:** `<fill in after deployment>`

- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/<fill in after deployment>)

- **Source Code:** [news_fact_checker.py](https://github.com/Dark-Brain07/genlayer-intelligent-contracts/blob/main/contracts/news_fact_checker.py)

---

## Technical Patterns Demonstrated

| Pattern | Contracts | Purpose |
|---------|-----------|---------|
| `gl.nondet.web.get(url)` | All 6 | Fetch data from public APIs |
| `gl.nondet.exec_prompt(prompt)` | Cricket, Weather, News | AI-powered reasoning and judgment |
| `gl.eq_principle.strict_eq(fn)` | All 6 | Deterministic validator consensus |
| Pipe-delimited canonical format | All oracles | Consensus on variable API responses |
| `TreeMap[str, str]` with JSON | All 6 | Flexible on-chain storage |
| `u32` counters | News Fact Checker | Deterministic ID generation |

## Full Repository

- **GitHub:** [github.com/Dark-Brain07/genlayer-intelligent-contracts](https://github.com/Dark-Brain07/genlayer-intelligent-contracts)
- **Network:** GenLayer Studionet
- **RPC:** https://studio.genlayer.com/api
- **Explorer:** https://explorer-studio.genlayer.com
