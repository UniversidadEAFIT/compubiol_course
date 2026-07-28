# Contribuir al curso

## Regla principal

No cree carpetas personales en la raíz ni agregue entregas de clase al repositorio canónico. Las entregas deben vivir en un repositorio de GitHub Classroom o en el repositorio personal indicado por el docente.

## Correcciones y mejoras reutilizables

1. Cree un fork o una rama con nombre descriptivo: `fix/c03-rutas` o `feature/c06-ejercicio-blast`.
2. Cambie un solo tema por pull request.
3. No incluya credenciales, datos sensibles, rutas absolutas, archivos mayores de 5 MB ni resultados generados.
4. Limpie las salidas de los notebooks: **Kernel → Restart Kernel and Clear All Outputs**.
5. Ejecute:

```bash
python scripts/validate_repo.py
bash scripts/run_smoke_tests.sh
```

6. Abra un pull request explicando: problema, solución, prueba realizada e impacto docente.

## Convenciones

- Español claro; términos técnicos en inglés cuando sea el uso estándar.
- Archivos y carpetas en `snake_case`, sin espacios ni tildes.
- Scripts Bash con `set -Eeuo pipefail`, ayuda, validación de entradas y mensajes de error útiles.
- Datos didácticos con `README`, procedencia, licencia y descripción de columnas.
- Las referencias deben apuntar preferentemente a documentación oficial o artículos primarios.
