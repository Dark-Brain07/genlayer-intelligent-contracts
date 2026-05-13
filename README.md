# GenLayer Intelligent Contracts v2

A collection of 10 advanced GenLayer intelligent contracts utilizing real-world data fetching via `gl.nondet.web.get()`. Each contract is designed for high-reliability consensus and optimized for the GenVM runtime.

## 📦 Included Oracles

1. **News Oracle**: Fetches world news headlines.
2. **Stock Oracle**: Real-time stock price tracking.
3. **SpaceX Oracle**: Latest space launch data.
4. **Air Quality Oracle**: City-based AQI index.
5. **Exchange Rate Oracle**: Live USD/EUR forex rates.
6. **Holiday Oracle**: Public holiday tracking.
7. **Joke Oracle**: Deterministic NPC dialogue jokes.
8. **Advice Oracle**: Deterministic NPC life advice.
9. **Activity Oracle**: Dynamic quest generation ideas.
10. **Cocktail Oracle**: Crafting recipes for in-game items.

## 🛠 Technical Implementation

All contracts utilize the verified GenVM parsing pattern:
```python
data = json.loads(response.body.decode("utf-8"))
```

## 🚀 Deployment Instructions

1. Connect your wallet to **GenLayer Studio**.
2. Select the contract you wish to deploy.
3. Use the source code from the `contracts/` directory.
4. Deploy and interact via the Explorer.

---
**Maintained by:** [Dark-Brain07](https://github.com/Dark-Brain07)
