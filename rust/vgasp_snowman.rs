// VGASP Snowman — Rust Binding
// Version: 1.0 (2026-10-08)
// Author: Borealis S. Hedling
//
// This module provides the canonical Rust implementation of the VGASP Snowman
// operator system. It enforces:
//
// - invariant surfaces (I_ij)
// - curvature surfaces (K_ij)
// - holonomy surfaces (H_ijk)
// - dissipation rules (D_ij)
// - JSON operator ordering (roll → stack → decorate)
//
// All operators emit JSON structures defined in:
// docs/governance/vgasp-snowman-json-operators.md

use serde::{Serialize, Deserialize};
use std::collections::HashMap;

// ---------------------------------------------------------------------------
// Tensor Containers
// ---------------------------------------------------------------------------

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct InvariantTensor {
    pub data: HashMap<String, f64>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CurvatureTensor {
    pub data: HashMap<String, f64>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HolonomyTensor {
    pub data: HashMap<String, f64>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DissipationTensor {
    pub data: HashMap<String, f64>,
}

// ---------------------------------------------------------------------------
// Errors
// ---------------------------------------------------------------------------

#[derive(Debug)]
pub enum SnowmanError {
    OrderingError(String),
    InvariantError(String),
    CurvatureError(String),
    HolonomyError(String),
    DissipationError(String),
}

// ---------------------------------------------------------------------------
// Snowman State Machine
// ---------------------------------------------------------------------------

#[derive(Debug, Clone)]
pub struct SnowmanState {
    pub invariant: InvariantTensor,
    pub curvature: CurvatureTensor,
    pub holonomy: HolonomyTensor,
    pub dissipation: DissipationTensor,
    last_op: Option<String>,
}

impl SnowmanState {
    pub fn new(
        invariant: InvariantTensor,
        curvature: CurvatureTensor,
        holonomy: HolonomyTensor,
        dissipation: DissipationTensor,
    ) -> Self {
        SnowmanState {
            invariant,
            curvature,
            holonomy,
            dissipation,
            last_op: None,
        }
    }

    // -----------------------------------------------------------------------
    // Ordering Enforcement
    // -----------------------------------------------------------------------

    fn check_order(&self, op: &str) -> Result<(), SnowmanError> {
        match self.last_op.as_deref() {
            None => {
                if op != "roll" {
                    return Err(SnowmanError::OrderingError(
                        "First operator must be roll.".into(),
                    ));
                }
            }
            Some("roll") => {
                if op != "stack" {
                    return Err(SnowmanError::OrderingError(
                        "After roll, only stack is allowed.".into(),
                    ));
                }
            }
            Some("stack") => {
                if op != "decorate" {
                    return Err(SnowmanError::OrderingError(
                        "After stack, only decorate is allowed.".into(),
                    ));
                }
            }
            Some("decorate") => {
                return Err(SnowmanError::OrderingError(
                    "No operators allowed after decorate.".into(),
                ));
            }
            _ => {}
        }
        Ok(())
    }

    // -----------------------------------------------------------------------
    // Constraint Enforcement
    // -----------------------------------------------------------------------

    fn check_invariant(&self) -> Result<(), SnowmanError> {
        if self.invariant.data.is_empty() {
            return Err(SnowmanError::InvariantError(
                "Invariant tensor is empty or undefined.".into(),
            ));
        }
        Ok(())
    }

    fn check_curvature(&self) -> Result<(), SnowmanError> {
        if self.curvature.data.values().any(|v| *v < 0.0) {
            return Err(SnowmanError::CurvatureError(
                "Negative curvature surfaces are forbidden.".into(),
            ));
        }
        Ok(())
    }

    fn check_holonomy(&self) -> Result<(), SnowmanError> {
        if self.holonomy.data.values().any(|v| v.abs() > 1.0) {
            return Err(SnowmanError::HolonomyError(
                "Holonomy drift exceeds stability threshold.".into(),
            ));
        }
        Ok(())
    }

    fn check_dissipation(&self) -> Result<(), SnowmanError> {
        if self.dissipation.data.values().any(|v| *v > 1.0) {
            return Err(SnowmanError::DissipationError(
                "Dissipation exceeds D_crit threshold.".into(),
            ));
        }
        Ok(())
    }

    // -----------------------------------------------------------------------
    // Operators
    // -----------------------------------------------------------------------

    pub fn roll(&mut self) -> Result<serde_json::Value, SnowmanError> {
        self.check_order("roll")?;
        self.check_invariant()?;
        self.check_holonomy()?;
        self.check_dissipation()?;

        self.last_op = Some("roll".into());

        Ok(serde_json::json!({
            "op": "roll",
            "invariant": self.invariant.data,
            "curvature": self.curvature.data,
            "holonomy": self.holonomy.data,
            "dissipation": self.dissipation.data,
        }))
    }

    pub fn stack(&mut self) -> Result<serde_json::Value, SnowmanError> {
        self.check_order("stack")?;
        self.check_invariant()?;
        self.check_curvature()?;
        self.check_dissipation()?;

        self.last_op = Some("stack".into());

        Ok(serde_json::json!({
            "op": "stack",
            "invariant": self.invariant.data,
            "curvature": self.curvature.data,
        }))
    }

    pub fn decorate(&mut self) -> Result<serde_json::Value, SnowmanError> {
        self.check_order("decorate")?;
        self.check_invariant()?;
        self.check_holonomy()?;
        self.check_dissipation()?;

        self.last_op = Some("decorate".into());

        Ok(serde_json::json!({
            "op": "decorate",
            "invariant": self.invariant.data,
        }))
    }
}
