#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from Bio import SeqIO


def main() -> None:
    p = argparse.ArgumentParser(description="Extrae sujetos BLAST y añade la consulta.")
    p.add_argument("--query", required=True, type=Path)
    p.add_argument("--database", required=True, type=Path)
    p.add_argument("--hits", required=True, type=Path, help="TSV con sseqid en la segunda columna")
    p.add_argument("--output", required=True, type=Path)
    args = p.parse_args()

    ids = set()
    with args.hits.open(encoding="utf-8") as handle:
        header = next(handle, None)
        for line in handle:
            if line.strip():
                ids.add(line.rstrip("\n").split("\t")[1])

    db = SeqIO.to_dict(SeqIO.parse(args.database, "fasta"))
    missing = sorted(ids - db.keys())
    if missing:
        raise SystemExit(f"IDs no encontrados en la base: {', '.join(missing)}")

    records = list(SeqIO.parse(args.query, "fasta")) + [db[i] for i in sorted(ids)]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    SeqIO.write(records, args.output, "fasta")
    print(f"Se escribieron {len(records)} secuencias en {args.output}")


if __name__ == "__main__":
    main()
