```markdown
# AGENTS.md for Nitra‑TUI

This file guides AI agents (e.g., Codex) on how to navigate, understand, and contribute to the **Nitra‑TUI** project. It sets out structure, conventions, responsibilities, and test expectations.

---

## 📁 Project Overview

```

Nitra‑TUI/
├── main.py
├── AGENTS.md
├── README.md
├── requirements.txt
└── nitra/
├── app.py
├── layout.py
├── router.py
├── bot\_manager.py
├── styles/base.tcss
├── panels/
│   ├── command\_panel.py
│   ├── metrics\_panel.py
│   ├── signals\_panel.py
│   └── logs\_panel.py
├── data/
│   └── mock\_feeds.py
├── core/
│   ├── config.py
│   ├── logger.py
│   └── state.py

```

---

## 🧩 Terminology

- **Panel**: A TUI component mapped to one of the four corners:
  - `CommandPanel`, `MetricsPanel`, `SignalsPanel`, `LogsPanel`
- **BotManager**: Orchestrates bot lifecycle and maintains shared state.
- **Agents**: Handles AI-assisted operations (Codex integration via `codex_bridge`).

---

## 📝 Coding Conventions

- Use **Python 3.10+**
- Use **Textual v0.38+**
- Imports: group standard → third-party → local; alphabetically sorted.
- Type hints mandatory. Use `typing` library classes.
- Docstrings: Triple-quoted (PEP 257) for all classes/functions.
- Maximum line length: **100 characters**.
- Use black-style formatting: 4-space indentation, blank line separation.

---

## 🧪 Testing & Validation

- Place tests in `nitra/core/tests/`.
- Naming: `test_<module>*.py`
- Run tests with:
```

pytest --maxfail=1 --disable-warnings -q

````
- Ensure that Codex-generated code includes basic test stubs matching the module’s functionality.

---

## 🛠 Workflow Expectations for Codex Agents

1. **Task by task**: Work one file at a time; never cross-modify other modules.
2. Always begin with:
 ```python
 from textual.app import App  # or relevant imports
````

3. Understand and use `BotManager` API for any bot-related operations.
4. UI logic remains in `panels/` files; AI should not inject logic into core files (e.g., `layout.py`) unless it’s UI-related.
5. Always include/update docstrings and adhere to style rules.
6. For new panel files:

   * Create an `update()` or `on_mount()` method to seed placeholder data.
   * Ensure a `styles/base.tcss` rule is added if new styling is required.

---

## 🔁 Code Integration Guidelines

* Commit new files one at a time, with clear commit messages:
  e.g. `"Add MetricsPanel – displays PnL and open trades"`.
* If you generate multiple small changes, group them logically (e.g., updates to both panel & layout files when adding a new panel).
* Always run lint/tests before "final" commits.

---

## 🔍 Example Panel Stub

For new panels, follow this template:

```python
from textual.widgets import Static
from textual.app import ComposeResult
from textual.reactive import reactive

class MyPanel(Static):
    """
    A brief description of what this panel does.
    """

    def __init__(self, bot_manager):
        super().__init__()
        self.bot_manager = bot_manager
        self.value: reactive[int] = reactive(0)

    def compose(self) -> ComposeResult:
        yield Static("My Panel")

    def on_mount(self):
        # placeholder data update
        self.update("Value: loading…")
```

---

## ✅ Summary

* **Understand**: Panel division, BotManager patterns, Agents folder use.
* **Structure**: One file at a time, test-first mindset, docstring style.
* **UI-first**: Keep UI code out of core modules.
* **Quality**: Tests, formatting, docstrings before finalization.

This document should equip Codex (or other AI agents) to generate consistent, project-compliant code as you build Nitra‑TUI.

---

Let me know if you'd like AGENTS.md variations for nested directories or expanded test guidelines!
