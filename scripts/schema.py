"""所有 CSV 欄位的唯一定義。欄位規則：只加不刪、不改名；新欄位一律加在最後。"""

CANDIDATES = [
    "candidate_id", "trial_or_title", "source_found", "source_url", "found_date",
    "pub_date_guess", "item_type", "first_seen_section_guess", "note",
]

FEEDS = ["feed_id", "source", "title", "url", "doi", "pub_date", "matched_keywords"]

EVIDENCE_A = ["candidate_id", "trial_name", "first_author", "title_full", "journal_full",
              "year", "doi", "pmid", "pub_date", "evidence_level", "source_url"]
EVIDENCE_B = ["design", "n", "population", "intervention", "comparator", "primary_outcome",
              "effect_size", "ci_95", "p_value", "key_secondary", "safety_signal"]
EVIDENCE_C = ["section", "status", "practice_impact", "takeaway_zh", "teaching_point",
              "local_applicability"]
EVIDENCE_D = ["week_id", "extracted_date", "audit_status"]
EVIDENCE = EVIDENCE_A + EVIDENCE_B + EVIDENCE_C + EVIDENCE_D

TRIALS_INDEX = ["trial_name", "doi", "first_seen_week", "last_updated_week", "section",
                "status", "practice_impact", "takeaway_zh", "previous_value"]
EXCLUDED = ["candidate_id", "trial_name", "week_id", "reason"]

ENUMS = {
    "evidence_level": {"full-text", "abstract-only", "preprint", "guideline", "unverified"},
    "status": {"新", "[更新]", "追蹤中"},
    "practice_impact": {"改變", "支持現況", "不足以改變", "待驗證"},
    "item_type": {"RCT", "observational", "guideline", "meta-analysis", "conference-abstract", "other"},
}
