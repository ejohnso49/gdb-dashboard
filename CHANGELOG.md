# Fork Changes

This file will document differences between this fork and upstream `gdb-dashboard`.
This repo was originally forked from 0.17.4.

## Development Environment Changes

- Use `uv` to manage project
- Use `lefthook` to manage pre-commit checks for linting, formatting, etc.
- Use `ruff` for linting/formatting
- Use `mypy` for type-checking

## Repo Structural Changes

- Extract Python code into the `gdb_dashboard` package
- Rework existing `.gdbinit` to use `gdbundle` to load the plugin
- Move GDB configuration commands into `scripts/config.gdb`
- Move the original `.gdbinit` contents into `gdbinit-no-gdbundle`

## Code Improvements

## Testing Improvements
