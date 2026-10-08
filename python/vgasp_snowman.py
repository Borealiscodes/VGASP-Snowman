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


# ---------------------------------------------------------------------------
# Tensor Containers
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Validation Errors
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Snowman State Machine
# ---------------------------------------------------------------------------

@dataclass
class SnowmanState:
    invariant: InvariantTensor
    curvature: CurvatureTensor
    holonomy: HolonomyTensor
    dissipation: DissipationTensor

    last_op: str = field(default=None)

    def _check_order(self, op: str):
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

    def _check_invariant(self):
        if not self.invariant.data:
            raise InvariantError("Invariant tensor is empty or undefined.")

    def _check_curvature(self):
        if any(v < 0 for v in self.curvature.data.values()):
            raise CurvatureError("Negative curvature surfaces are forbidden.")

    def _check_holonomy(self):
        if any(abs(v) > 1.0 for v in self.holonomy.data.values()):
            raise HolonomyError("Holonomy drift exceeds stability threshold.")

    def _check_dissipation(self):
        if any(v > 1.0 for v in self.dissipation.data.values()):
            raise DissipationError("Dissipation exceeds D_crit threshold.")

    # -----------------------------------------------------------------------
    # Operators
    # -----------------------------------------------------------------------

    def roll(self) -> Dict[str, Any]:
        self._check_order("roll")
        self._check_invariant()
        self._check_holonomy()
        self._check_dissipation()

        self.last_op = "roll"

        return {
            "op": "roll",
            "invariant": self.invariant.data,
            "curvature": self.curvature.data,
            "holonomy": self.holonomy.data,
            "dissipation": self.dissipation.data,
        }

    def stack(self) -> Dict[str, Any]:
        self._check_order("stack")
        self._check_invariant()
        self._check_curvature()
        self._check_dissipation()

        self.last_op = "stack"

        return {
            "op": "stack",
            "invariant": self.invariant.data,
            "curvature": self.curvature.data,
        }

    def decorate(self) -> Dict[str, Any]:
        self._check_order("decorate")
        self._check_invariant()
        self._check_holonomy()
        self._check_dissipation()

        self.last_op = "decorate"

        return {
            "op": "decorate",
            "invariant": self.invariant.data,
        }
