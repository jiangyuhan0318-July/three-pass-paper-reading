---
name: three-pass-paper-reading
description: Read research papers using S. Keshav's three-pass method, progressing from five-Cs screening to evidence review and virtual reimplementation. Use for substantive paper reading, critical appraisal, or a literature survey; report the depth actually reached and distinguish paper claims from verified findings.
---

# Three-pass paper reading

Use S. Keshav's *How to Read a Paper* as the method. Read [references/method-origin.md](references/method-origin.md) when checking fidelity to the source or explaining the method. The three passes are progressive decisions, not a requirement to read every paper equally deeply.

## Establish the reading target

- Confirm the actual title, authors, version/date, and PDF page count from the document. A filename is not bibliographic evidence.
- Identify the requested purpose and depth. For an explicit close reading, aim for all three passes; otherwise decide whether to continue after each pass.
- Extract text with page boundaries. Inspect original page images wherever figures, tables, equations, columns, or extraction artifacts affect interpretation. Record unreadable material rather than filling gaps.
- Use PDF page numbers and section/table/figure labels for evidence. If printed page numbering differs, state the convention.

## Pass 1: orientation and the five Cs

Read the title, abstract, and introduction carefully; scan section/subsection headings, read the conclusion, and glance at references. Avoid working through technical details yet.

Record:

| C | Question |
|---|---|
| Category | What kind of paper is this: measurement, analysis, prototype, theory, survey? |
| Context | Which research line, prior methods, and theoretical bases does it use? |
| Correctness | Do the assumptions initially appear reasonable? This is preliminary, not proof. |
| Contributions | What does the paper claim to add? |
| Clarity | Can the research question, method, and result be understood from its presentation? |

Decide: stop, defer pending background reading, or continue; record why. Keshav's 5–10 minutes is human-reader guidance, not a duration the agent must claim to have spent.

## Pass 2: understand the argument and its evidence

Read the body carefully, leaving detailed proofs/derivations for pass 3. Make notes connecting the problem, design choices, experiments/analysis, and conclusions.

- Inspect figures and tables, including axes, units, legends, sample sizes, error bars, and what comparison each supports. Error bars alone do not establish statistical significance.
- For experimental papers, identify datasets, splits, preprocessing/augmentation, baselines, training and evaluation conditions, metric definitions, ablations, and uncertainty reporting. Adapt these checks to the paper's actual design.
- Build a compact claim–evidence ledger: claim, exact locator, reported result, and what the evidence does/does not establish. Do not present an author's result as independently reproduced.
- Mark relevant unread references and why they matter. A citation in the paper is not a reference you have read or verified.
- Summarize the main argument with supporting evidence in your own words. Identify what remains unclear.

If understanding is still insufficient, choose and record: stop, revisit after background reading, or proceed to pass 3. Keshav suggests up to one hour for a human reader; do not invent elapsed time.

## Pass 3: virtual reimplementation and critical reconstruction

Before rechecking details, write a short reconstruction from the working understanding: inputs, assumptions, intermediate operations, objective/derivation, outputs, and evaluation. Then compare it against the paper and record corrections. Do not call this human memory testing.

- Reconstruct the central method at a level another researcher could implement: equations/tensor shapes or algorithm steps as appropriate; data flow, training/evaluation path, and the meaning of outputs. Identify missing specifications explicitly.
- Challenge consequential assumptions. Ask whether comparisons isolate the claimed mechanism; inspect alternative explanations, dataset leakage risks, coordinate conventions, statistical units, and generalization only where relevant.
- Recalculate important reported deltas with explicit denominators. Distinguish percentage-point changes from relative percentage changes, and reconcile conflicting prose, tables, figures, and units.
- Identify strengths, weaknesses, relevant citation gaps, and future-work ideas. Distinguish a confirmed internal inconsistency from an untested risk or hypothesis.
- Explain how you would present the idea more clearly, and which single experiment or missing artifact would most improve confidence.

Virtual reimplementation is a reasoning exercise. Mark independently: text/figure review, arithmetic checks, runnable reconstruction, and full empirical replication. Never equate reading, pseudocode, or a toy calculation with reproducing the reported model performance. Keshav's human time estimates (4–5 hours for beginners; about one hour for experienced readers) are not agent completion claims.

## Literature-survey mode (only when requested)

Start with 3–5 recent relevant papers from an academic search; first-pass each and inspect related work for a survey. Follow shared citations and recurring authors as discovery cues, inspect recent relevant venues, then make two passes through the selected papers and iterate on missed key references. A pairwise comparison alone is not an exhaustive survey. Citation frequency, author reputation, and venue prestige are discovery heuristics, not proof of quality.

## Deliverables and self-check

Match the user's desired format. A full reading normally includes bibliographic identity; five Cs and continuation decision; problem/method/evidence summary; third-pass reconstruction; supported critique; unread references; and actual completion limits. For multiple papers, compare only commensurable claims and metrics.

Keep a usage record with the loaded skill path, source documents, work completed per pass, inspected figure/table pages, checks performed, and unresolved items. Report actual execution, not merely the planned checklist.

Before delivery verify:

1. Every important number and critical claim has a document locator or a labeled external source; uncertain information remains uncertain.
2. No unread reference, unrun experiment, or unavailable code is described as checked or reproduced.
3. Author claims, direct observations/calculations, and reader interpretations are distinguishable.
4. The final judgment fits the evidence and states consequential limitations without assuming misconduct.
5. The usage record accurately states the depth achieved and any remaining gap. Repair factual errors found during this check.
