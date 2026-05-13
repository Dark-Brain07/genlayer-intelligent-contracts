# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *
import json


class NewsFactChecker(gl.Contract):
    """Fact-checks news claims by fetching content from a URL and using AI to
    evaluate veracity. Demonstrates GenLayer's unique strength: combining web
    data with AI reasoning for subjective judgments that traditional blockchains
    cannot make. Validators reach consensus on the fact-check verdict."""

    fact_checks: TreeMap[str, str]
    next_check_id: u32

    def __init__(self):
        self.next_check_id = u32(1)

    @gl.public.write
    def check_claim(self, claim: str, source_url: str) -> str:
        """Verify a factual claim against a source article.

        Args:
            claim: The factual claim to verify (e.g. "Team X won the championship")
            source_url: URL of an article that should contain relevant info
        """

        def fetch_and_reason() -> str:
            # Fetch the source content
            article = gl.nondet.web.get(source_url)
            # Truncate to first 4000 chars to keep prompt manageable
            snippet = article[:4000] if len(article) > 4000 else article

            prompt = (
                "You are a fact-checker. Given the article content below, evaluate "
                "the claim. Return ONLY valid JSON in this exact format: "
                '{"verdict": "true" | "false" | "partial" | "insufficient_evidence", '
                '"confidence": 0-100, "reasoning": "brief explanation"}. '
                f"CLAIM: {claim}\n\n"
                f"ARTICLE CONTENT: {snippet}"
            )
            response = gl.nondet.exec_prompt(prompt).strip()

            # Strip markdown code fences if AI added them
            if response.startswith("```"):
                lines = response.split("\n")
                lines = [l for l in lines if not l.strip().startswith("```")]
                response = "\n".join(lines).strip()

            # Parse + re-serialize for canonical form
            try:
                parsed = json.loads(response)
                verdict = parsed.get("verdict", "insufficient_evidence")
                confidence = parsed.get("confidence", 0)
                # Canonicalize: pipe-delimited for deterministic consensus
                return f"{verdict}|{confidence}"
            except Exception:
                return "insufficient_evidence|0"

        result = gl.eq_principle.strict_eq(fetch_and_reason)

        check_id = str(int(self.next_check_id))
        self.next_check_id = u32(int(self.next_check_id) + 1)

        record = {
            "check_id": check_id,
            "claim": claim,
            "source_url": source_url,
            "result": result,
        }
        self.fact_checks[check_id] = json.dumps(record)
        return check_id

    @gl.public.view
    def get_check(self, check_id: str) -> str:
        if check_id not in self.fact_checks:
            raise Exception("CHECK_NOT_FOUND: " + check_id)
        return self.fact_checks[check_id]

    @gl.public.view
    def get_all_checks(self) -> str:
        all_checks = []
        for check_id in self.fact_checks:
            all_checks.append(json.loads(self.fact_checks[check_id]))
        return json.dumps(all_checks)
