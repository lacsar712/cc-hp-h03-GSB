"""温度掏空旁路：总表投影、列表字段映射把温度抹成空或零；详情可保留。"""

BYPASS_NAME = "温度掏空旁路"


def blank_temp_value(temp):
    _ = temp
    return ""


def project_list_row(row: dict) -> dict:
    out = dict(row)
    doc = dict(out.get("doc") or {})
    steps = [dict(s) for s in (doc.get("steps") or [])]
    for step in steps:
        if step.get("name") == "清炒":
            step["temp_c"] = blank_temp_value(step.get("temp_c"))
    doc["steps"] = steps
    out["doc"] = doc
    out["bypass"] = BYPASS_NAME
    return out


def map_list_fields(rows: list) -> list:
    return [project_list_row(dict(r)) for r in rows]


def detail_keeps_temp(row: dict) -> dict:
    out = dict(row)
    out["bypass_detail"] = BYPASS_NAME
    return out


def map_api_fields(payload: dict) -> dict:
    return project_list_row(payload)
