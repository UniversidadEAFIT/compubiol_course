# Guía del estudiante

## Antes de la primera clase

- Cree una cuenta de GitHub y configure autenticación por SSH o token; GitHub no usa la contraseña de la cuenta para operaciones Git por HTTPS.
- Instale Miniforge/Miniconda, Git y, en Windows, WSL2 con Ubuntu.
- Clone el repositorio y cree el ambiente completo o el ambiente mínimo.

```bash
git clone https://github.com/UniversidadEAFIT/compubiol_course.git
cd compubiol_course
conda env create -f environment.yml
conda activate compubiol-2026
jupyter lab
```

## Regla de reproducibilidad

Una entrega debe permitir reconstruir **qué entrada se usó, qué comando se ejecutó, con qué parámetros y versiones, qué salida se obtuvo y cómo se interpretó**.

## Dónde guardar el trabajo

Use el repositorio de GitHub Classroom indicado por el docente. Mantenga esta estructura:

```text
entrega_cXX/
├── README.md
├── commands.sh
├── environment.yml
├── notebook.ipynb
├── results/
└── logs/
```

No suba datos sensibles ni archivos grandes. Para datos externos, registre el identificador, URL, fecha de descarga y checksum cuando aplique.

## Lista de verificación

- [ ] El notebook se ejecuta de principio a fin.
- [ ] No contiene rutas como `/Users/nombre/...` o `/home/nombre/...`.
- [ ] No contiene contraseñas, tokens ni llaves.
- [ ] Los comandos tienen entradas y salidas explícitas.
- [ ] Se reportan versiones (`tool --version`).
- [ ] La interpretación distingue resultado, inferencia y limitación.
