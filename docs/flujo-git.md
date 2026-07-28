# Flujo Git y entregas

## Flujo recomendado

```bash
git switch master
git pull --ff-only
git switch -c c03-linux-usuario
# editar y probar
git status
git add entrega_c03/
git commit -m "Completa actividad C3 de Linux"
git push -u origin c03-linux-usuario
```

Después, abra un pull request en el repositorio de la entrega o siga el mecanismo de GitHub Classroom. No haga `push` directo a la rama protegida del material docente.

## Recuperar sin perder trabajo

```bash
git status
git diff
git restore --staged archivo
git restore archivo              # descarta cambios no confirmados: úselo con cuidado
git log --oneline --graph -10
git show COMMIT:archivo
```

## Conflictos

Un conflicto no es un fallo misterioso: Git necesita que una persona decida qué versión conservar. Lea los marcadores, edite el archivo, pruebe y continúe con `git add` y `git commit`.
