# Instalación y ambientes

## Opción A · ambiente completo

Incluye Python, Jupyter y las herramientas de línea de comandos de C5–C9.

```bash
conda env create -f environment.yml
conda activate compubiol-2026
python --version
blastp -version
mafft --version
```

## Opción B · ambiente mínimo

Adecuado para C1–C4 y para equipos con restricciones de instalación.

```bash
conda env create -f environment-minimal.yml
conda activate compubiol-minimal
```

## Canales de Bioconda

El archivo declara `conda-forge` y `bioconda` y no agrega `defaults`. Configure una vez la prioridad estricta recomendada por Bioconda:

```bash
conda config --add channels bioconda
conda config --add channels conda-forge
conda config --set channel_priority strict
```

Compruebe el resultado con `conda config --show-sources` y `conda config --show channel_priority`.

## Reconstruir o actualizar

```bash
conda env create -f environment.yml
# Si ya existe y desea sincronizarlo:
conda env update -n compubiol-2026 -f environment.yml --prune
```

## Diagnóstico

```bash
bash scripts/check_environment.sh
```

El diagnóstico no instala nada: informa qué herramientas están disponibles y cuáles faltan.
