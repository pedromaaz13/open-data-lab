# Buenas prácticas de repositorios

## Estructura

- Carpetas numeradas y temáticas (ver README raíz).
- Un README por carpeta explicando su propósito.
- `data/` nunca se versiona (salvo catálogos pequeños). Ver `.gitignore`.

## Ramas

- Rama principal protegida.
- Trabajo en ramas `feature/`, `fix/`, `docs/`.
- Pull requests con descripción y checklist.

## Commits

- Mensajes claros en imperativo: *"Add housing-salary ratio notebook"*.
- Convención recomendada: [Conventional Commits](https://www.conventionalcommits.org/)
  (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`).
- Commits atómicos: un cambio lógico por commit.

## Calidad de código

- `ruff` + `black` para Python.
- `sqlfluff` para SQL.
- `pre-commit` para ejecutar checks antes de commitear.
- `pytest` para tests de la lógica en `src/`.

## CI/CD

- GitHub Actions: lint + tests en cada push/PR.
- Builds reproducibles (versiones fijadas en `requirements.txt`).

## Documentación

- README potente en raíz.
- ADRs para decisiones técnicas (ver `11_stack_tecnologico/13_decision_records/`).
- Diccionario de datos por dataset publicado.
