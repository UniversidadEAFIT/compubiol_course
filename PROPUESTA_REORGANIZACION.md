# Propuesta de reorganización del repositorio

## Recomendación central

Transformar `compubiol_course` en un **repositorio canónico de enseñanza**, no en un contenedor de entregas. La navegación principal debe seguir la progresión C1–C9 del syllabus, mientras las versiones antiguas se preservan con tags y los trabajos estudiantiles se administran con GitHub Classroom.

## Qué se conserva y mejora

- **IntroLinux → C3:** conserva navegación, comandos, `grep`, pipes y FASTA; añade WSL actual, rutas relativas, seguridad, regex, normalización y validaciones.
- **Github → C2:** conserva repositorio/fork/commit; añade Conda, ramas, pull request, autenticación segura, recuperación y notebooks limpios.
- **blasting → C6:** conserva fundamentos y uso local/HPC; añade elección de programa, base reproducible, tabla estándar, filtros, MAFFT y criterios biológicos.
- **manejo de errores + LinuxII → C4:** integra variables, bucles y permisos con códigos de salida, `set -Eeuo pipefail`, `trap`, logs y pruebas negativas.

## Temas nuevos derivados del syllabus

C1 datos/FAIR; C5 HPC/Slurm/Seqtk; C7 curación/filogenia/iTOL/workflows; C8 tecnologías/FASTQ/FastQC; C9 GFF3/coordenadas/bedtools.

## Beneficios

- una única versión vigente por tema;
- menor dependencia de instrucciones orales;
- prácticas ejecutables en Colab, terminal y HPC;
- separación entre material, datos, scripts y resultados;
- trazabilidad semestral sin duplicar carpetas;
- revisión automática de notebooks y scripts;
- sitio navegable semejante al patrón lecture/lab/homework/resources del curso de referencia.
