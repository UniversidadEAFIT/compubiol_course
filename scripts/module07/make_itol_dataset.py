#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from pathlib import Path

PALETTE = {"REF": "#4C78A8", "A": "#59A14F", "B": "#F28E2B", "C": "#E15759"}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("metadata", type=Path)
    p.add_argument("output", type=Path)
    args = p.parse_args()

    rows = list(csv.DictReader(args.metadata.open(encoding="utf-8"), delimiter="\t"))
    lines = [
        "DATASET_COLORSTRIP",
        "SEPARATOR TAB",
        "DATASET_LABEL\tGroup",
        "COLOR\t#000000",
        "LEGEND_TITLE\tGroup",
        "LEGEND_SHAPES\t1\t1\t1\t1",
        "LEGEND_COLORS\t#4C78A8\t#59A14F\t#F28E2B\t#E15759",
        "LEGEND_LABELS\tREF\tA\tB\tC",
        "DATA",
    ]
    for row in rows:
        group = row["group"]
        lines.append(f'{row["sequence_id"]}\t{PALETTE.get(group, "#999999")}\t{group}')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
