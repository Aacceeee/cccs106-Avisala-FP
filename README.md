# umAni

**Smarter Choices for Every Palay Harvest.**
A Flet (Python) app that helps palay farmers compare buyers using their harvest details and selling preferences.

## Team Roles

| Dev | Name | Role |
|---|---|---|
| Dev 1 | Marc Ace Evangelista | Requirements Engineer & UI/UX Lead: Scope, SRS, User Stories, Flet Views |
| Dev 2 | Mark Paul B. Calvelo| Data & Systems Architect (Database, APIs, UML Class/Sequence, Model-View-Controller (MVC)) |
| Dev 3 | Janline B. Lerio| QA & DevOps Lead (GitFlow, Automated Testing, PyInstaller Packaging) |
## Run

```bash
pip install -r requirements.txt
flet run -r app/main.py
```

## Project structure

```
docs/                     Scope, user stories, SRS
assets/                   Logo and background images
app/
  main.py                 Entry point and route registration
  router.py               Screen navigation (go / replace / back)
  theme.py                Colors, shared UI pieces, bottom navigation
  state.py                Shared session data
  services/mock_data.py   Placeholder logic for backend devs to replace
  views/
    shared/               Splash, login, sign up
    farmer/               Farmer screens
    buyer/                Buyer screens
    admin/                Admin screens
```

## Git conventions

- Branch names: `dev1/docs-scope`, `dev1/ui-farmer-flow`
- Commit prefixes: `docs:`, `ui:`, `fix:`, `chore:`
- Open a pull request for every change.
>>>>>>> 19eae85 (docs: add scope, user stories, SRS, and project README)
