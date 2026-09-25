"""批次记录出参映射。

炮制记录是一整包文书（doc 内为工序数组），清炒温度等字段必须从原文书
原样透传到总表、列表行与详情页，任何投影都不得把温度改写成空串或 0。
"""

from copy import deepcopy


def project_list_row(row: dict) -> dict:
    """投影单行记录：深拷贝原文书，完整保留各工序（含清炒温度）。"""
    out = dict(row)
    if out.get("doc") is not None:
        out["doc"] = deepcopy(out["doc"])
    return out


def map_list_fields(rows: list) -> list:
    """总表 / 列表出参映射。"""
    return [project_list_row(dict(r)) for r in rows]


def detail_keeps_temp(row: dict) -> dict:
    """详情出参：与列表走同一投影，三处读数保持一致。"""
    return project_list_row(row)


def map_api_fields(payload: dict) -> dict:
    """写入回包出参映射，同样原样保留温度。"""
    return project_list_row(payload)
