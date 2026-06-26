# Git, GitHub y CI/CD

## Para qué sirve

Versionar, colaborar y automatizar calidad: la base profesional de cualquier proyecto.

## Conceptos principales

- Git: commits, ramas, merge/rebase, PRs.
- Conventional Commits.
- GitHub Actions para CI.
- pre-commit hooks.
- Releases y versionado semántico.

## Librerías útiles

- `git`, `gh`, `pre-commit`, GitHub Actions.
- `ruff`, `black`, `sqlfluff`, `pytest` en CI.

## Ejemplos de uso

```yaml
# .github/workflows/ci.yml (ejemplo)
name: CI
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - run: pip install ruff && ruff check .
```

## Errores comunes

- Commits gigantes sin foco.
- Subir datos pesados o credenciales.
- No tener CI que valide lint y tests.

## Mini proyecto recomendado

Configurar pre-commit con ruff/black/sqlfluff y un workflow de CI básico.

## Recursos para profundizar

- Pro Git book.
- Docs de GitHub Actions y pre-commit.
