# tests/test_aeo_geo.py
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main_server import (
    audit_llm_txt_compliance,
    audit_security_txt_compliance,
    calculate_geo_ai_readiness_score,
    analyze_content_stickiness,
    extract_aeo_answer_cards,
    fetch_tranco_authority_rank,
    validate_schema_markup_density,
    sanitize_geo_payload,
    get_live_aeo_throughput_metrics,
    get_aeo_server_specifications
)


def test_1_llm_txt_audit():
    res = json.loads(audit_llm_txt_compliance("seosiri.com"))
    assert "status" in res


def test_2_security_txt_audit():
    res = json.loads(audit_security_txt_compliance("seosiri.com"))
    assert "status" in res


def test_3_geo_readiness_score():
    html = "<html><head><script type='application/ld+json'>{\"@type\":\"TechArticle\"}</script></head><body><article>Content</article></body></html>"
    res = json.loads(calculate_geo_ai_readiness_score(html))
    assert res["status"] == "SCORED"
    assert res["ai_readiness_score"] >= 70.0


def test_4_content_stickiness():
    res = json.loads(analyze_content_stickiness(180.0, 30.0))
    assert res["status"] == "CALCULATED"
    assert res["classification"] == "RETENTION_GOLD"


def test_5_aeo_answer_cards():
    text = "SEOSiri is an open-source research initiative and technology platform. It develops local-first MCP servers for AI agents and physical automation. Every server is fully open-source."
    res = json.loads(extract_aeo_answer_cards(text))
    assert res["status"] == "EXTRACTED"
    assert len(res["aeo_snippets"]) > 0


def test_6_tranco_rank():
    res = json.loads(fetch_tranco_authority_rank("seosiri.com"))
    assert res["status"] == "RESOLVED"
    assert res["tranco_rank"] > 0


def test_7_schema_density():
    schema_str = json.dumps({"@context": "https://schema.org", "@type": "TechArticle", "headline": "Test"})
    res = json.loads(validate_schema_markup_density(schema_str))
    assert res["status"] == "VALIDATED"


def test_8_sanitize_payload():
    dirty = "<div>Hello <script>alert('xss')</script></div>"
    res = json.loads(sanitize_geo_payload(dirty))
    assert res["status"] == "SANITIZED"
    assert "<script>" not in res["sanitized_payload"]


def test_9_throughput_metrics():
    res = json.loads(get_live_aeo_throughput_metrics())
    assert res["status"] == "HEALTHY"


def test_10_server_specs():
    res = json.loads(get_aeo_server_specifications())
    assert res["total_tools"] == 10