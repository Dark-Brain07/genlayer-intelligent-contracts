# GenLayer Points Portal Submission Template

Use these templates to submit each of the 10 contracts to the **GenLayer Points Portal** under the **Tools & Infrastructure** category.

---

### 1. Activity Oracle
- **Title:** Rick & Morty Character Lore Oracle
- **Description:** An intelligent contract that fetches deterministic character data (Name, Species, Status) from the Rick and Morty API using `gl.nondet.web.get()` to generate consistent quest NPCs.
- **Contract Address:** `0x8cf47A37785B0CC5B471758A8b3b5ba6EB9b55a3`
- **Source:** `contracts/activity_oracle.py`

### 2. Advice Oracle
- **Title:** RPG NPC Advice Oracle
- **Description:** Fetches deterministic life advice from the Advice Slip API for immersive NPC interactions.
- **Contract Address:** `0x7fbce5fe497274Cc2883405d7c7a04F8e6C0964b`
- **Source:** `contracts/advice_oracle.py`

### 3. Air Quality Oracle
- **Title:** Global Air Quality Index Oracle
- **Description:** Fetches real-time AQI data for any city worldwide using the WAQI API.
- **Contract Address:** `0xd10aEFb5121d4A52444A6b28d45C81982d6CFbBE`
- **Source:** `contracts/air_quality_oracle.py`

### 4. Cocktail Oracle
- **Title:** Item Crafting & Recipe Oracle
- **Description:** Fetches real cocktail recipes from TheCocktailDB to drive in-game alchemy and crafting mechanics.
- **Contract Address:** `0xe04f131Ce90eb6CFde8B5810c15A0dD159A5ebD1`
- **Source:** `contracts/cocktail_oracle.py`

### 5. Exchange Rate Oracle
- **Title:** Forex Exchange Rate Oracle (USD/EUR)
- **Description:** Fetches live USD/EUR exchange rates for in-game currency balancing and global markets.
- **Contract Address:** `0xcAC1d7fFE4E20FF03582070c4C4d79646FB0Db12`
- **Source:** `contracts/exchange_rate_oracle.py`

### 6. Holiday Oracle
- **Title:** Public Holiday Tracking Oracle
- **Description:** Fetches upcoming public holidays using the Nager.Date API to drive time-based game rewards and world states.
- **Contract Address:** `0x0EcB12D9243ea64fa1A75f23dbDC1469AdAE0B4C`
- **Source:** `contracts/holiday_oracle.py`

### 7. Joke Oracle
- **Title:** Deterministic NPC Joke Oracle
- **Description:** Fetches consistent jokes from the Official Joke API for high-consensus NPC dialogue.
- **Contract Address:** `0x3ac1F17738e9aFD873d869e532e7a35268acE66f`
- **Source:** `contracts/joke_oracle.py`

### 8. News Oracle
- **Title:** World News Headline Oracle for Dynamic Events
- **Description:** An intelligent contract that fetches real-time world news headlines to drive dynamic world events and lore updates.
- **Contract Address:** `0x31935478447dA116d6bF54aC5B243d71d02f1b69`
- **Source:** `contracts/news_oracle.py`

### 9. SpaceX Oracle
- **Title:** SpaceX Launch Event Oracle
- **Description:** Fetches latest SpaceX launch data to trigger space-themed game events and cosmic quests.
- **Contract Address:** `0x6E926c653C227a18d942Ab323194EF63565B7BA0`
- **Source:** `contracts/spacex_oracle.py`

### 10. Stock Oracle
- **Title:** Deterministic Corporate Stock Price Oracle
- **Description:** Fetches real corporate stock market data from the Alpha Vantage API using `gl.nondet.web.get()`. Targets the static 'Previous Close' price anchor to guarantee perfect validator consensus consistency.
- **Contract Address:** `0xcF4e9eE0e6886B358De6656c6041C240B42d0E28`
- **Source:** `contracts/stock_oracle.py`
