# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *
import json


class GithubVerifier(gl.Contract):
    """Verifies a user's GitHub identity by fetching their profile via the
    GitHub public API. Useful for developer credentialing, bounty platforms,
    or on-chain reputation systems. Validators reach consensus on canonical
    profile data even though the API may return extra fields."""

    verified_users: TreeMap[str, str]
    wallet_to_github: TreeMap[str, str]

    def __init__(self):
        pass

    @gl.public.write
    def verify_profile(self, github_username: str, wallet_address: str) -> str:
        """Fetch and verify a GitHub profile, binding it to a wallet address."""

        api_url = f"https://api.github.com/users/{github_username}"

        def fetch_profile() -> str:
            raw = gl.nondet.web.get(api_url)
            try:
                data = json.loads(raw)
                # Reject if profile doesn't exist
                if "message" in data and data["message"] == "Not Found":
                    return "NOT_FOUND"

                username = data.get("login", "")
                name = data.get("name") or username
                public_repos = data.get("public_repos", 0)
                followers = data.get("followers", 0)
                created_at = data.get("created_at", "")
                # Pipe-delimited for consensus
                return f"{username}|{name}|{public_repos}|{followers}|{created_at}"
            except Exception:
                return "ERROR"

        profile_data = gl.eq_principle.strict_eq(fetch_profile)

        if profile_data == "NOT_FOUND":
            raise Exception("GITHUB_USER_NOT_FOUND: " + github_username)
        if profile_data == "ERROR":
            raise Exception("VERIFICATION_FAILED: Could not fetch profile")

        verification = {
            "github_username": github_username,
            "wallet_address": wallet_address,
            "profile_data": profile_data,
            "verified": True,
        }
        self.verified_users[github_username] = json.dumps(verification)
        self.wallet_to_github[wallet_address] = github_username

        return json.dumps(verification)

    @gl.public.view
    def get_verification(self, github_username: str) -> str:
        if github_username not in self.verified_users:
            raise Exception("NOT_VERIFIED: " + github_username)
        return self.verified_users[github_username]

    @gl.public.view
    def get_wallet_github(self, wallet_address: str) -> str:
        if wallet_address not in self.wallet_to_github:
            raise Exception("NO_BINDING: No GitHub bound to " + wallet_address)
        return self.wallet_to_github[wallet_address]
