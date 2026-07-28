#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def fasta_lengths(path: Path) -> dict[str, int]:
    lengths: dict[str, int] = {}
    current: str | None = None
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                current = line[1:].split()[0]
                if current in lengths:
                    raise ValueError(f"Contig duplicado: {current}")
                lengths[current] = 0
            elif current is None:
                raise ValueError("FASTA sin encabezado inicial")
            else:
                lengths[current] += len(line)
    return lengths


def attributes(text: str) -> dict[str, str]:
    result = {}
    for item in text.split(";"):
        if "=" in item:
            key, value = item.split("=", 1)
            result[key] = value
    return result


def main() -> None:
    p = argparse.ArgumentParser(description="Convierte genes GFF3 en promotores BED6.")
    p.add_argument("--genome", required=True, type=Path)
    p.add_argument("--gff", required=True, type=Path)
    p.add_argument("--length", type=int, default=200)
    p.add_argument("--output", required=True, type=Path)
    args = p.parse_args()
    if args.length <= 0:
        raise SystemExit("--length debe ser positivo")

    sizes = fasta_lengths(args.genome)
    rows: list[tuple[str, int, int, str, str]] = []
    with args.gff.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if not line.strip() or line.startswith("#"):
                continue
            fields = line.rstrip("\n").split("\t")
            if len(fields) != 9:
                raise SystemExit(f"GFF3 inválido en línea {line_no}: se esperaban 9 columnas")
            seqid, _, feature, start_s, end_s, _, strand, _, attr_s = fields
            if feature != "gene":
                continue
            if seqid not in sizes:
                raise SystemExit(f"Contig {seqid} ausente en FASTA")
            start, end = int(start_s), int(end_s)  # GFF3: 1-based inclusive
            gene_id = attributes(attr_s).get("ID")
            if not gene_id:
                raise SystemExit(f"Gene sin ID en línea {line_no}")
            if strand == "+":
                bed_start = max(0, (start - 1) - args.length)
                bed_end = start - 1
            elif strand == "-":
                bed_start = end
                bed_end = min(sizes[seqid], end + args.length)
            else:
                raise SystemExit(f"Hebra no soportada para {gene_id}: {strand}")
            if bed_end <= bed_start:
                raise SystemExit(f"Promotor vacío para {gene_id}")
            rows.append((seqid, bed_start, bed_end, gene_id, strand))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    rows.sort(key=lambda r: (r[0], r[1], r[2], r[3]))
    with args.output.open("w", encoding="utf-8") as out:
        for seqid, start, end, gene_id, strand in rows:
            out.write(f"{seqid}\t{start}\t{end}\t{gene_id}\t.\t{strand}\n")
    print(f"{len(rows)} promotores escritos en {args.output}")


if __name__ == "__main__":
    main()
