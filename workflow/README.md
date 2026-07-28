# Flujo C6–C7 con Snakemake

```bash
conda activate compubiol-2026
snakemake -s workflow/Snakefile -n -p
snakemake -s workflow/Snakefile --cores 2 -p
```

El primer comando es un *dry run*. El flujo enlaza BLAST+/filtrado/MAFFT con IQ-TREE y registra dependencias explícitas. Para un proyecto real, se recomienda separar ambientes por regla y fijar versiones mediante perfiles o contenedores.
