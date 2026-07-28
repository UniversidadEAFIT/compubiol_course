# Auditoría y propuesta de actualización

## Hallazgos de la auditoría

- La raíz del repositorio combina carpetas por semestre (`20181`–`2025`), archivos generales y numerosas carpetas personales.
- La carpeta `20201` solo conserva `IntroLinux`; las copias más completas de `Github`, `IntroLinux`, `LinuxII`, `blasting` y `Error_handling.pdf` están en `20221/20231`.
- `Intro_Linux.ipynb` cubre comandos útiles, pero conserva referencias y configuraciones antiguas, imágenes dispersas y resultados con rutas locales.
- `Intro_a_GitHub.ipynb` enseña creación, fork y commit, pero incluye cifras obsoletas, aconseja un flujo de `push` directo a `master` y necesita actualizar autenticación y pull requests.
- `Blasting.ipynb` depende de módulos y rutas de Apolo, crea un ambiente incompleto y no deja un flujo cerrado de BLAST+, filtrado y MAFFT.
- `LinuxII_Ejercicios.ipynb` y `Error_handling.pdf` se integran mejor como una sola clase de scripting robusto con parámetros, códigos de salida, `set -Eeuo pipefail`, `trap`, validaciones y logs.

## Decisión de arquitectura

Se reemplaza la navegación “por semestre” por una navegación “por resultado de aprendizaje”:

```text
C1 datos → C2 reproducibilidad → C3 terminal → C4 automatización →
C5 HPC → C6 homología → C7 filogenia → C8 calidad → C9 anotación
```

Cada clase tiene la misma unidad pedagógica: concepto, laboratorio, checkpoint, reto y entrega.

## Política de contenido

- **Rama principal:** solamente material canónico mantenido.
- **Tags:** instantáneas históricas por semestre y antes de migraciones mayores.
- **GitHub Classroom:** entregas individuales o grupales.
- **Pull requests:** correcciones y ejemplos generalizables.
- **Datos:** pequeños, públicos, sintéticos o redistribuibles; datos grandes se descargan mediante script y checksum.
