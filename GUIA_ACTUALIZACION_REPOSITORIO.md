# Guía para actualizar `UniversidadEAFIT/compubiol_course`

Esta guía sustituye la rama de trabajo por la estructura 2026 **sin perder la historia**. El repositorio antiguo queda accesible mediante un tag. Haga la migración primero en una rama y fusiónela mediante pull request.

## 0. Requisitos

- permisos para crear ramas, tags y pull requests;
- Git instalado;
- copia descargada de `compubiol_course_2026_update/`;
- árbol de trabajo limpio.

## 1. Clonar y comprobar el estado actual

```bash
git clone https://github.com/UniversidadEAFIT/compubiol_course.git
cd compubiol_course
git switch master
git pull --ff-only
git status --short
```

`git status --short` debe quedar vacío. Si tiene cambios propios, confírmelos en otra rama o guárdelos antes de continuar.

## 2. Crear un punto de restauración

```bash
git tag -a legacy-2026-07-28 -m "Repositorio antes de la reorganización 2026"
git push origin legacy-2026-07-28
git switch -c refresh/course-2026
```

Compruebe el tag:

```bash
git show --stat legacy-2026-07-28
git ls-remote --tags origin | grep legacy-2026-07-28
```

## 3. Sustituir el árbol de la rama de migración

Desde la raíz del clon:

```bash
git rm -r .
```

Esto elimina los archivos **de la rama**, no la historia ni el tag. Ahora copie todo el contenido de la carpeta entregada `compubiol_course_2026_update/` a la raíz del clon. Con `rsync`:

```bash
rsync -av /RUTA/compubiol_course_2026_update/ ./
```

No copie el archivo ZIP dentro del repositorio.

## 4. Validar localmente

```bash
python -m pip install nbformat pyyaml biopython
python scripts/validate_repo.py
bash scripts/run_smoke_tests.sh
```

Opcionalmente, construya el sitio:

```bash
python -m pip install -r requirements-docs.txt
mkdocs build --strict
```

## 5. Revisar el cambio antes de confirmar

```bash
git status --short
git diff --stat
git diff -- README.md environment.yml CONTRIBUTING.md
```

Revise especialmente:

- licencia y atribución institucional;
- nombre del curso y del docente;
- URLs de Colab y GitHub Pages;
- parámetros de Apolo/Apolo-Learning;
- política de entregas en GitHub Classroom.

## 6. Confirmar y abrir pull request

```bash
git add -A
git commit -m "Reorganiza el curso de bioinformática para 2026"
git push -u origin refresh/course-2026
```

Abra un pull request `refresh/course-2026 → master`. Espere que las validaciones queden en verde y revise el sitio generado.

## 7. Configurar el repositorio después de fusionar

En **Settings → Branches / Rulesets**:

- proteja `master`;
- exija pull request;
- exija la validación `Validar materiales`;
- ejecute `Validar ambiente Conda` cuando cambie `environment.yml`;
- impida `force push` y eliminación de la rama.

En **Settings → Pages** seleccione **GitHub Actions** como fuente. El workflow `pages.yml` construirá MkDocs.

En GitHub Classroom, cree repositorios separados para entregas. El repositorio canónico debe permanecer limpio.

## 8. Verificar el material histórico

```bash
git switch --detach legacy-2026-07-28
ls
git switch master
```

También puede crear una rama histórica de solo lectura:

```bash
git branch legacy/semester-folders legacy-2026-07-28
git push origin legacy/semester-folders
```

El tag suele ser suficiente y evita presentar material obsoleto como rama activa.

## 9. Reversión de emergencia

Si el pull request aún no se ha fusionado, ciérrelo y elimine la rama. Si ya se fusionó, no reescriba la historia; cree un commit de reversión desde GitHub o:

```bash
git switch master
git pull --ff-only
git revert -m 1 MERGE_COMMIT_SHA   # solo si la fusión fue un merge commit
git push origin master
```

Antes de revertir, confirme el tipo de fusión. El tag `legacy-2026-07-28` siempre conserva el estado anterior.

## 10. Mantenimiento por semestre

1. Crear tag de cierre.
2. Probar ambientes y notebooks limpios.
3. Revisar enlaces y documentación oficial.
4. Actualizar parámetros institucionales del HPC.
5. Integrar solo mejoras generalizables.
6. Publicar notas en `CHANGELOG.md`.
