# 欄位定義（自動產生，勿手改；來源 scripts/schema.py）

規則：欄位順序固定；只在最後新增，不刪不改名。CSV 以 UTF-8 with BOM 存檔。

## candidates.csv（Scanner）

```
candidate_id,trial_or_title,source_found,source_url,found_date,pub_date_guess,item_type,first_seen_section_guess,note
```

## evidence.csv（Verifier 填 A、B、D 組；Curator 填 C 組）

```
candidate_id,trial_name,first_author,title_full,journal_full,year,doi,pmid,pub_date,evidence_level,source_url,design,n,population,intervention,comparator,primary_outcome,effect_size,ci_95,p_value,key_secondary,safety_signal,section,status,practice_impact,takeaway_zh,teaching_point,local_applicability,week_id,extracted_date,audit_status
```

## index/trials.csv（Curator）

```
trial_name,doi,first_seen_week,last_updated_week,section,status,practice_impact,takeaway_zh,previous_value
```

## index/excluded.csv（Curator）

```
candidate_id,trial_name,week_id,reason
```

## 列舉值

- `evidence_level`：abstract-only / full-text / guideline / preprint / unverified
- `status`：[更新] / 新 / 追蹤中
- `practice_impact`：不足以改變 / 待驗證 / 支持現況 / 改變
- `item_type`：RCT / conference-abstract / guideline / meta-analysis / narrative-review / observational / other
