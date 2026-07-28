# Diseño y decisiones

## Problemas corregidos

1. **Organización cronológica, no pedagógica:** las carpetas por semestre obligaban a buscar “la versión correcta”.
2. **Material y entregas mezclados:** carpetas personales y notebooks canónicos coexistían en el mismo nivel.
3. **Dependencia del computador del autor:** varias celdas heredadas contenían rutas, módulos o salidas locales.
4. **Flujos Git desactualizados:** el material guiaba a subir directamente a la rama principal y trataba credenciales de forma insegura.
5. **Prácticas incompletas:** el notebook de BLAST configuraba un ambiente, pero no cerraba un flujo reproducible de búsqueda, filtrado y alineamiento.

## Patrón adoptado

El curso de referencia separa cada clase en explicación, laboratorio, tarea y recursos. Esta actualización conserva ese patrón, pero lo alinea directamente con C1–C9 del syllabus de EAFIT y añade:

- un notebook canónico por clase;
- datos didácticos pequeños y documentados;
- scripts independientes del notebook;
- una actividad evaluable por clase;
- validación automática;
- sitio navegable con GitHub Pages;
- política explícita para aportes y material histórico.
