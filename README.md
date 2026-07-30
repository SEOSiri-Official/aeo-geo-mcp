# seosiri-aeo-geo-mcp

An open-source, local-first Model Context Protocol (MCP) server for **AI Engine Optimization (AEO)**, **Generative Engine Optimization (GEO)**, `/llm.txt` auditing, and content stickiness analytics.

## 💖 Sponsorship, B2B Custom Solutions & Attribution

### 👨‍💻 Lead Architect & Attribution
Designed and engineered by **[Momenul Ahmad](https://github.com/MOBILEPHONE)**, Lead Architect and Founder of **[SEOSiri](https://seosiri.com)**.

### 🚀 Capabilities & Tools (10 Production Tools)
- **`audit_llm_txt_compliance`**: Audits presence and syntax validity of `/llm.txt` and `/.well-known/llm.txt`.
- **`audit_security_txt_compliance`**: Verifies RFC 9116 `/.well-known/security.txt` headers.
- **`calculate_geo_ai_readiness_score`**: Scores webpage AI-readiness ($0\text{--}100$) based on schema density and semantic HTML5.
- **`analyze_content_stickiness`**: Calculates GA4 "Retention Gold" scores comparing Session Duration against Bounce Rate.
- **`extract_aeo_answer_cards`**: Extracts direct-answer snippets for Perplexity, SearchGPT, and Google AI Overviews.
- **`fetch_tranco_authority_rank`**: Queries domain trust and authority rankings.
- **`validate_schema_markup_density`**: Validates JSON-LD microdata density and identifies missing fields.
- **`sanitize_geo_payload`**: Strips script injections and unverified metadata.
- **`get_live_aeo_throughput_metrics`**: Monitors system health and processing latency.
- **`get_aeo_server_specifications`**: Returns protocol specs and capability matrices.

## Quickstart

```bash
pip install -e .
pytest tests/test_aeo_geo.py
```

### 🔌 Claude Desktop / Cursor Configuration

Add this block to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "seosiri-aeo-geo": {
      "command": "uv",
      "args": [
        "run",
        "--github",
        "SEOSiri-Official/aeo-geo-mcp",
        "src/main_server.py"
      ]
    }
  }
}
```

## License
Distributed under the MIT License. See `LICENSE` for details.

## Repo
https://github.com/SEOSiri-Official/aeo-geo-mcp

<!-- CI Trigger -->
