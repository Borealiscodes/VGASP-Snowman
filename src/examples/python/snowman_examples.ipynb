# ⭐ VGASP Snowman — Notebook Cells (Python 3.11)
Below is the complete set of notebook cells, in order.

You can paste them directly into VS Code’s Notebook editor (.ipynb), one cell at a time, or use “Paste Notebook Cells” to import them all at once.

---

📘 Cell 1 — Full Snowman Module (inline)
`python
"""
VGASP Snowman — Python Binding
Version: 1.0 (2026-10-08)
Author: Borealis S. Hedling

This module provides the canonical Python implementation of the VGASP Snowman
operator system. It enforces:

- invariant surfaces (I_ij)
- curvature surfaces (K_ij)
- holonomy surfaces (H_ijk)
- dissipation rules (D_ij)
- JSON operator ordering (roll → stack → decorate)

All operators emit JSON structures defined in:
docs/governance/vgasp-snowman-json-operators.md
"""

from dataclasses import dataclass, field
from typing import Dict, Any

---------------------------------------------------------------------------

Tensor Containers

---------------------------------------------------------------------------

@dataclass
class InvariantTensor:
    data: Dict[str, float]

@dataclass
class CurvatureTensor:
    data: Dict[str, float]

@dataclass
class HolonomyTensor:
    data: Dict[str, float]

@dataclass
class DissipationTensor:
    data: Dict[str, float]

---------------------------------------------------------------------------

Validation Errors

---------------------------------------------------------------------------

class SnowmanError(Exception):
    """Base class for Snowman operator errors."""

class OrderingError(SnowmanError):
    """Raised when operator ordering is violated."""

class InvariantError(SnowmanError):
    """Raised when invariant constraints are violated."""

class CurvatureError(SnowmanError):
    """Raised when curvature constraints are violated."""

class HolonomyError(SnowmanError):
    """Raised when holonomy constraints are violated."""

class DissipationError(SnowmanError):
    """Raised when dissipation constraints are violated."""

---------------------------------------------------------------------------

Snowman State Machine

---------------------------------------------------------------------------

@dataclass
class SnowmanState:
    invariant: InvariantTensor
    curvature: CurvatureTensor
    holonomy: HolonomyTensor
    dissipation: DissipationTensor

    last_op: str = field(default=None)

    def checkorder(self, op: str):
        """Enforce roll → stack → decorate ordering."""
        if self.last_op is None:
            if op != "roll":
                raise OrderingError("First operator must be roll.")
        elif self.last_op == "roll":
            if op not in ("stack",):
                raise OrderingError("After roll, only stack is allowed.")
        elif self.last_op == "stack":
            if op not in ("decorate",):
                raise OrderingError("After stack, only decorate is allowed.")
        elif self.last_op == "decorate":
            raise OrderingError("No operators allowed after decorate.")

    def checkinvariant(self):
        if not self.invariant.data:
            raise InvariantError("Invariant tensor is empty or undefined.")

    def checkcurvature(self):
        if any(v < 0 for v in self.curvature.data.values()):
            raise CurvatureError("Negative curvature surfaces are forbidden.")

    def checkholonomy(self):
        if any(abs(v) > 1.0 for v in self.holonomy.data.values()):
            raise HolonomyError("Holonomy drift exceeds stability threshold.")

    def checkdissipation(self):
        if any(v > 1.0 for v in self.dissipation.data.values()):
            raise DissipationError("Dissipation exceeds D_crit threshold.")

    # -----------------------------------------------------------------------
    # Operators
    # -----------------------------------------------------------------------

    def roll(self) -> Dict[str, Any]:
        self.checkorder("roll")
        self.checkinvariant()
        self.checkholonomy()
        self.checkdissipation()

        self.last_op = "roll"

        return {
            "op": "roll",
            "invariant": self.invariant.data,
            "curvature": self.curvature.data,
            "holonomy": self.holonomy.data,
            "dissipation": self.dissipation.data,
        }

    def stack(self) -> Dict[str, Any]:
        self.checkorder("stack")
        self.checkinvariant()
        self.checkcurvature()
        self.checkdissipation()

        self.last_op = "stack"

        return {
            "op": "stack",
            "invariant": self.invariant.data,
            "curvature": self.curvature.data,
        }

    def decorate(self) -> Dict[str, Any]:
        self.checkorder("decorate")
        self.checkinvariant()
        self.checkholonomy()
        self.checkdissipation()

        self.last_op = "decorate"

        return {
            "op": "decorate",
            "invariant": self.invariant.data,
        }
`

---

📘 Cell 2 — Bill Nye Tile
`markdown

🧊 Bill Nye Tile: “Show the Science Live!”

A Snowman isn’t just an idea — it’s a state machine with tensors, governance
rules, and operator ordering. This notebook shows the Snowman executing live,
with real JSON outputs from roll → stack → decorate.
`

---

📘 Cell 3 — Attenborough Tile
`markdown

🌿 Attenborough Tile: “Let the Snowman Move…”

In this frozen meadow of computation, the Snowman emerges through gentle,
law‑bound motion. Each operator leaves footprints in fresh snow — visible here
as JSON traces.
`

---

📘 Cell 4 — Notebook Overview
`markdown

📘 Notebook Overview

This notebook demonstrates:

- tensor creation  
- SnowmanState initialization  
- operator ordering  
- governance errors  
- dissipation limits  
- tensor inspection  
- provenance  

All examples use the canonical VGASP Snowman Python binding.
`

---

📘 Cell 5 — How to Run This Notebook
`markdown

▶️ How to Run This Notebook

Just run each cell in order.  
The Snowman module is fully embedded in Cell 1 — no imports required.
`

---

📘 Cell 6 — Create Tensors
`python
invariant = InvariantTensor({"symmetry": 1.0})
curvature = CurvatureTensor({"k1": 0.5, "k2": 0.3})
holonomy = HolonomyTensor({"h1": 0.2})
dissipation = DissipationTensor({"d1": 0.1})

(invariant.data, curvature.data, holonomy.data, dissipation.data)
`

---

📘 Cell 7 — Create SnowmanState
`python
state = SnowmanState(
    invariant=invariant,
    curvature=curvature,
    holonomy=holonomy,
    dissipation=dissipation
)

state.last_op
`

---

📘 Cell 8 — Execute roll()
`python
state.roll()
`

---

📘 Cell 9 — Execute stack()
`python
state.stack()
`

---

📘 Cell 10 — Execute decorate()
`python
state.decorate()
`

---

📘 Cell 11 — OrderingError Demo
`python
try:
    state.roll()
except OrderingError as e:
    str(e)
`

---

📘 Cell 12 — DissipationError Demo
`python
bad_diss = DissipationTensor({"d1": 2.0})
badstate = SnowmanState(invariant, curvature, holonomy, baddiss)

try:
    bad_state.roll()
except DissipationError as e:
    str(e)
`

---

📘 Cell 13 — Tensor Inspection
`python
{
    "invariant": state.invariant.data,
    "curvature": state.curvature.data,
    "holonomy": state.holonomy.data,
    "dissipation": state.dissipation.data,
    "lastop": state.lastop
}
`

---

📘 Cell 14 — Provenance Footer
`markdown
---
Provenance:
Created by Borealis S. Hedling (Dublin, Ireland) as part of the VGASP Snowman
v2.0 pedagogy tier. Demonstrates canonical operator ordering, governance errors,
tensor inspection, and dissipation limits. Python 3.11 kernel.
---
`

---

