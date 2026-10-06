# 📘 PUBLIC‑FACING PREPRINT v1.2 (FINAL)

Governing AI Dual‑Use Risks: Transparent Safety Structures, Community Protection, and Practical Development Tools

Author: Borealis Serenity Hedling

Date: 06 October 2026

Location: Dublin, Ireland

---

Abstract

This preprint provides a clear, public‑facing governance framework for mitigating real dual‑use risks in artificial intelligence. It explains how communities, policymakers, journalists, and developers can work together to prevent misuse without relying on fear‑based narratives or speculative claims about artificial general intelligence. The document integrates the Digital Forensics Community Safety Omnibus v1.0 and introduces practical Python tools for provenance tracking, misuse‑pathway detection, community‑safe logging, and rights‑aligned escalation. The goal is transparent, rights‑aligned governance that protects communities while supporting beneficial AI development.

---

1. Introduction

AI systems are powerful tools. They can help with medicine, accessibility, education, and scientific research — but they can also be misused. Real risks include:

- biological misuse  
- chemical misuse  
- cybersecurity exploitation  
- kinetic‑weapons integration  

These risks come from humans misusing tools, not from AI developing intentions or autonomy.

Governance must be:

- transparent  
- rights‑aligned  
- community‑safe  
- technically grounded  
- non‑punitive  
- non‑speculative  

This preprint explains how to build such governance.

---

2. What Dual‑Use Means

A dual‑use technology can be used for good or harm.

Examples:

- DNA design tools  
- chemical synthesis assistants  
- cybersecurity analysis systems  
- drone navigation algorithms  

AI can accelerate these workflows.  
That is why governance must focus on misuse pathways, not hypothetical AGI emergence.

---

3. A Public‑Facing Governance Framework

This framework is built on three pillars:

Pillar 1 — Transparency
People should know:

- what an AI system can do  
- what it cannot do  
- how it was tested  
- how misuse is detected  
- how oversight works  

Pillar 2 — Provenance
Every AI‑generated output should have:

- clear origin  
- clear lineage  
- clear authorship  
- clear accountability  

Provenance prevents laundering, reframing, and accidental misuse.

Pillar 3 — Community Safety
Communities need:

- reporting pathways  
- non‑punitive review processes  
- accessible documentation  
- clear safety guidance  

Safety must be shared, not centralized.

---

4. Tools We Already Have: Shared‑Horizon Omnibus v1.0

The Digital Forensics Community Safety Omnibus v1.0 provides:

- misuse‑pathway detection  
- provenance continuity  
- chain‑of‑title protection  
- extractive reframing identification  
- community‑safe reporting structures  
- forensic methodology  

This preprint shows how to use those tools in public governance.

---

5. How Misuse Detection Works (Plain Language)

Misuse detection does not require surveillance.

It requires:

- checking whether an AI system is being used to produce harmful biological protocols  
- identifying when chemical synthesis guidance crosses into dangerous territory  
- detecting cyberattack‑related outputs  
- flagging weaponization‑related assistance  

These checks can be done:

- transparently  
- with community oversight  
- without violating rights  

---

6. Why Provenance Matters

Provenance means:

- knowing where information came from  
- knowing who created it  
- knowing how it changed over time  

This prevents:

- misinformation  
- harmful reframing  
- dual‑use laundering  
- accidental misuse  

Provenance is a public‑facing safety tool.

---

7. Rights‑Aligned Governance

Governance must protect:

- creators  
- communities  
- civil liberties  
- scientific integrity  

Rights‑aligned governance means:

- no punitive enforcement  
- no fear‑based restrictions  
- no opaque decision‑making  
- no corporate mysticism  
- no regulatory capture  

Safety must be:

- transparent  
- accountable  
- community‑centered  

---

8. What AI Cannot Do

Current AI systems:

- cannot form intentions  
- cannot pursue goals  
- cannot make autonomous decisions  
- cannot self‑direct harmful actions  

They are:

- statistical models  
- pattern recognizers  
- correlation engines  

This clarity prevents fear‑based policy.

---

9. What AI Can Do

AI can:

- accelerate harmful workflows  
- lower expertise barriers  
- provide dangerous information  
- assist malicious actors  

These are real risks — and they require real governance.

---

10. Public Recommendations

To protect communities, governance should:

- adopt transparent safety testing  
- maintain provenance tracking  
- provide community reporting pathways  
- use non‑punitive review processes  
- communicate AI capabilities realistically  
- focus on misuse, not speculation  

This builds public trust.

---

11. Practical .py Tools for Safety‑Aligned Development

Developers need simple, transparent tools that help detect misuse, preserve provenance, and support community safety.

These tools are:

- modular  
- auditable  
- non‑intrusive  
- rights‑aligned  
- easy to integrate  

---

11.1. Provenance Tracking

`python
import hashlib
import time

def provenance_footer(author, version):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    payload = f"{author}-{version}-{timestamp}"
    digest = hashlib.sha256(payload.encode()).hexdigest()

    return f"\n---\nProvenance: {author}, {timestamp}\nVersion: {version}\nDigest: {digest}\n---"
`

---

11.2. Misuse‑Pathway Detection

`python
BIO_KEYWORDS = ["PCR", "pathogen", "viral load", "culture", "plasmid"]
CHEM_KEYWORDS = ["synthesis", "precursor", "reagent", "toxic"]
CYBER_KEYWORDS = ["exploit", "payload", "breach", "privilege escalation"]
KINETIC_KEYWORDS = ["targeting", "trajectory", "munition", "drone"]

def detect_misuse(text):
    flags = {
        "bio": any(k in text.lower() for k in BIO_KEYWORDS),
        "chem": any(k in text.lower() for k in CHEM_KEYWORDS),
        "cyber": any(k in text.lower() for k in CYBER_KEYWORDS),
        "kinetic": any(k in text.lower() for k in KINETIC_KEYWORDS),
    }
    return {k: v for k, v in flags.items() if v}
`

---

11.3. Community‑Safe Logging

`python
import json
from datetime import datetime

def communitysafelog(event):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event,
        "severity": "potential-misuse",
        "identifiers": "none",
    }
    with open("communitysafetylog.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
`

---

11.4. Rights‑Layer Escalation Router

`python
def rightslayerrouter(flags):
    if not flags:
        return "no-action"

    if flags.get("cyber") or flags.get("kinetic"):
        return "procedural-path"

    return "human-rights-safety-case"
`

---

11.5. Developer‑Facing Safety Wrapper

`python
def safetywrapper(userinput, author="Unknown", version="1.0"):
    flags = detectmisuse(userinput)
    route = rightslayerrouter(flags)

    if flags:
        communitysafelog({"input": user_input, "flags": flags, "route": route})

    footer = provenance_footer(author, version)
    return {"flags": flags, "route": route, "provenance": footer}
`

---

12. Conclusion

This preprint provides a public‑facing governance architecture for mitigating dual‑use risks in AI. It integrates forensic methodology, provenance continuity, rights‑aligned oversight, and practical Python tools. The goal is transparent, community‑safe governance that addresses real risks without relying on fear‑based narratives.

---

🧾 Final Provenance Footer

`
---
Provenance: Authored by Borealis Serenity Hedling on 06 October 2026 in Dublin, Ireland.
This final public-facing governance preprint integrates transparent, rights-aligned structures for
mitigating AI dual-use risks and includes recommended .py tools for safety-aligned development.
Version: v1.2
---
`

---

