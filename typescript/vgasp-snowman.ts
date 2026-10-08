/**
 * VGASP Snowman — TypeScript Binding
 * Version: 1.0 (2026-10-08)
 * Author: Borealis S. Hedling
 *
 * This module provides the canonical TypeScript implementation of the VGASP
 * Snowman operator system. It enforces:
 *
 * - invariant surfaces (I_ij)
 * - curvature surfaces (K_ij)
 * - holonomy surfaces (H_ijk)
 * - dissipation rules (D_ij)
 * - JSON operator ordering (roll → stack → decorate)
 *
 * All operators emit JSON structures defined in:
 * docs/governance/vgasp-snowman-json-operators.md
 */

export interface Tensor {
    [key: string]: number;
}

export interface InvariantTensor {
    data: Tensor;
}

export interface CurvatureTensor {
    data: Tensor;
}

export interface HolonomyTensor {
    data: Tensor;
}

export interface DissipationTensor {
    data: Tensor;
}

// ---------------------------------------------------------------------------
// Errors
// ---------------------------------------------------------------------------

export class SnowmanError extends Error {}
export class OrderingError extends SnowmanError {}
export class InvariantError extends SnowmanError {}
export class CurvatureError extends SnowmanError {}
export class HolonomyError extends SnowmanError {}
export class DissipationError extends SnowmanError {}

// ---------------------------------------------------------------------------
// Snowman State Machine
// ---------------------------------------------------------------------------

export class SnowmanState {
    invariant: InvariantTensor;
    curvature: CurvatureTensor;
    holonomy: HolonomyTensor;
    dissipation: DissipationTensor;

    private lastOp: string | null = null;

    constructor(
        invariant: InvariantTensor,
        curvature: CurvatureTensor,
        holonomy: HolonomyTensor,
        dissipation: DissipationTensor
    ) {
        this.invariant = invariant;
        this.curvature = curvature;
        this.holonomy = holonomy;
        this.dissipation = dissipation;
    }

    // -----------------------------------------------------------------------
    // Ordering Enforcement
    // -----------------------------------------------------------------------

    private checkOrder(op: string): void {
        if (this.lastOp === null) {
            if (op !== "roll") {
                throw new OrderingError("First operator must be roll.");
            }
        } else if (this.lastOp === "roll") {
            if (op !== "stack") {
                throw new OrderingError("After roll, only stack is allowed.");
            }
        } else if (this.lastOp === "stack") {
            if (op !== "decorate") {
                throw new OrderingError("After stack, only decorate is allowed.");
            }
        } else if (this.lastOp === "decorate") {
            throw new OrderingError("No operators allowed after decorate.");
        }
    }

    // -----------------------------------------------------------------------
    // Constraint Enforcement
    // -----------------------------------------------------------------------

    private checkInvariant(): void {
        if (!this.invariant.data || Object.keys(this.invariant.data).length === 0) {
            throw new InvariantError("Invariant tensor is empty or undefined.");
        }
    }

    private checkCurvature(): void {
        for (const v of Object.values(this.curvature.data)) {
            if (v < 0) {
                throw new CurvatureError("Negative curvature surfaces are forbidden.");
            }
        }
    }

    private checkHolonomy(): void {
        for (const v of Object.values(this.holonomy.data)) {
            if (Math.abs(v) > 1.0) {
                throw new HolonomyError("Holonomy drift exceeds stability threshold.");
            }
        }
    }

    private checkDissipation(): void {
        for (const v of Object.values(this.dissipation.data)) {
            if (v > 1.0) {
                throw new DissipationError("Dissipation exceeds D_crit threshold.");
            }
        }
    }

    // -----------------------------------------------------------------------
    // Operators
    // -----------------------------------------------------------------------

    roll(): Record<string, any> {
        this.checkOrder("roll");
        this.checkInvariant();
        this.checkHolonomy();
        this.checkDissipation();

        this.lastOp = "roll";

        return {
            op: "roll",
            invariant: this.invariant.data,
            curvature: this.curvature.data,
            holonomy: this.holonomy.data,
            dissipation: this.dissipation.data,
        };
    }

    stack(): Record<string, any> {
        this.checkOrder("stack");
        this.checkInvariant();
        this.checkCurvature();
        this.checkDissipation();

        this.lastOp = "stack";

        return {
            op: "stack",
            invariant: this.invariant.data,
            curvature: this.curvature.data,
        };
    }

    decorate(): Record<string, any> {
        this.checkOrder("decorate");
        this.checkInvariant();
        this.checkHolonomy();
        this.checkDissipation();

        this.lastOp = "decorate";

        return {
            op: "decorate",
            invariant: this.invariant.data,
        };
    }
}
