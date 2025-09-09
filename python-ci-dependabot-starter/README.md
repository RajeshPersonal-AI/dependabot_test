# Python CI + Dependabot Starter

A tiny Python project with:
- **GitHub Actions CI**: lint (flake8), security scan (bandit), tests (pytest) on 3 Python versions
- **Dependabot**: updates for `pip` dependencies (daily) and GitHub Actions (weekly)

## Quickstart
```bash
# Clone your new repo (after you push this template)
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
pytest -q
flake8 app tests
bandit -r app -x tests
```

## CI
CI runs on pushes and pull requests to `main`:
- Setup Python (3.10, 3.11, 3.12)
- Install deps
- Run flake8, bandit, pytest

See [`.github/workflows/ci.yml`](.github/workflows/ci.yml).

## Dependabot
- `pip` ecosystem checked **daily** at 10:00 Asia/Kolkata
- `github-actions` checked **weekly** (Monday) at 10:00 Asia/Kolkata

See [`.github/dependabot.yml`](.github/dependabot.yml).

## Notes
- Keep your code under `app/`, tests under `tests/`.
- Adjust lint rules in `.flake8` as you like.
- If you want auto-merge for patch updates, set up branch protection and add a separate workflow.
