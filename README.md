# Bioinformática y Biología Computacional

[![Validación](https://github.com/UniversidadEAFIT/compubiol_course/actions/workflows/validate.yml/badge.svg)](https://github.com/UniversidadEAFIT/compubiol_course/actions/workflows/validate.yml)
[![Ambiente Conda](https://github.com/UniversidadEAFIT/compubiol_course/actions/workflows/conda-environment.yml/badge.svg)](https://github.com/UniversidadEAFIT/compubiol_course/actions/workflows/conda-environment.yml)
[![Sitio del curso](https://img.shields.io/badge/sitio-GitHub%20Pages-17365d)](https://universidadeafit.github.io/compubiol_course/)
[![Licencia: CC BY 4.0](https://img.shields.io/badge/licencia-CC%20BY%204.0-lightgrey.svg)](LICENSE)

Repositorio canónico del curso de **Bioinformática y Biología Computacional de la Universidad EAFIT**. La ruta combina explicación conceptual, práctica guiada, datos pequeños versionables, scripts auditables y actividades que producen evidencia reproducible.

> Las entregas de estudiantes no se almacenan en la raíz ni dentro de los notebooks docentes. Se recomienda usar repositorios separados de GitHub Classroom; este repositorio recibe únicamente correcciones o mejoras reutilizables mediante pull request.

## Ruta del curso

| Clase | Tema | Material principal | Evidencia |
|---|---|---|---|
| C1 | Datos biológicos, FAIR y organización | [Notebook](notebooks/01_datos_fair/01_datos_fair.ipynb) | [Actividad](assignments/C01_datos_fair.md) |
| C2 | Conda, Git, GitHub y cuadernos reproducibles | [Notebook](notebooks/02_reproducibilidad_git/02_conda_git_github.ipynb) | [Actividad](assignments/C02_reproducibilidad_git.md) |
| C3 | Introducción a Linux y Bash | [Notebook](notebooks/03_linux/03_intro_linux.ipynb) | [Actividad](assignments/C03_linux.md) |
| C4 | Bash intermedio y manejo de errores | [Notebook](notebooks/04_bash_robusto/04_bash_manejo_errores.ipynb) | [Actividad](assignments/C04_bash_robusto.md) |
| C5 | HPC, Slurm y Seqtk | [Notebook](notebooks/05_hpc_slurm/05_hpc_slurm_seqtk.ipynb) | [Actividad](assignments/C05_hpc_slurm.md) |
| C6 | Alineamiento, BLAST+ y MAFFT | [Notebook](notebooks/06_alineamiento_blast/06_alineamiento_blast_mafft.ipynb) | [Actividad](assignments/C06_blast_mafft.md) |
| C7 | Curación, IQ-TREE e iTOL | [Notebook](notebooks/07_filogenia/07_filogenia_iqtree_itol.ipynb) | [Actividad](assignments/C07_filogenia.md) |
| C8 | Secuenciación, FASTQ y FastQC | [Notebook](notebooks/08_fastq_qc/08_fastq_fastqc.ipynb) | [Actividad](assignments/C08_fastq_qc.md) |
| C9 | GFF3, coordenadas y bedtools | [Notebook](notebooks/09_gff3_bedtools/09_gff3_bedtools.ipynb) | [Actividad](assignments/C09_gff3_bedtools.md) |

## Cómo comenzar

1. Lea la [guía del estudiante](docs/guia-estudiante.md).
2. Cree el ambiente con `conda env create -f environment.yml` y actívelo con `conda activate compubiol-2026`.
3. Abra `jupyter lab` desde la raíz del repositorio o use el botón de Colab de cada notebook.
4. Trabaje siempre en una rama propia y conserve comandos, parámetros, versiones y resultados esenciales.

## Estructura

```text
compubiol_course/
├── docs/          # sitio navegable y syllabus operativo
├── notebooks/     # un cuaderno canónico por clase
├── data/          # datos didácticos pequeños y documentados
├── scripts/       # scripts Bash, Python y Slurm reutilizables
├── assignments/   # consignas y rúbrica común
├── workflow/      # ejemplo de flujo reproducible con Snakemake
├── instructor/    # migración, decisiones y notas docentes
└── .github/       # validación automática y despliegue del sitio
```

## Modos de ejecución

- **Google Colab:** Python, inspección tabular y ejercicios que no dependan de servicios institucionales.
- **Linux, macOS o WSL:** Bash, Git y herramientas instaladas con Conda.
- **Apolo/Apolo-Learning:** prácticas de Slurm, recursos y datos de mayor tamaño. Ajuste `--account` y `--partition` según la documentación institucional vigente.

## Material heredado

Las versiones por semestre quedaron preservadas mediante el tag recomendado `legacy-2026-07-28`. El mapa de equivalencias está en [instructor/MIGRATION_MAP.md](instructor/MIGRATION_MAP.md).

## Validar antes de publicar

```bash
python scripts/validate_repo.py
bash scripts/run_smoke_tests.sh
```

## Cita y licencia

Consulte [`CITATION.cff`](CITATION.cff). Los materiales originales se proponen bajo CC BY 4.0; confirme la compatibilidad con la política institucional antes de hacer pública la nueva versión.
