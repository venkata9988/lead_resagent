---
name: lead-validation-testing
description: Pre-flight validation and automated regression testing engine for lead signals, ensuring 100% factual grounding and deliverability compliance.
version: 1.0.0
---

# Lead Pre-Testing & Quality Validation Skill

## Objective
Run rigorous automated unit and regression checks on extracted lead data and generated copy before allowing any message into the output queue.

## Pre-Flight Test Suite:

### Test 1: Ground Truth Fact-Checking (Anti-Hallucination)
* **Rule**: Extract all named entities, numbers, and proper nouns from the generated pitch (e.g., "$15M", "Series B", "10 locations", "Dr. Sarah").
* **Verification**: Cross-reference each entity against the raw scraped HTML/context.
* **Failure Condition**: If any key statistic or funding number is not present in the raw source, flag as `HALLUCINATION_DETECTED` and reject the draft.

### Test 2: Deliverability & Spam Score Check
* **Spam Word Filter**: Flags words like *"guaranteed"*, *"risk-free"*, *"free trial"*, *"act now"*, *"cheap"*.
* **Length Constraints**:
  * LinkedIn connection notes must be strictly $\le$ 250 characters.
  * Cold emails must be strictly $\le$ 100 words.
* **Tone Analysis**: Rejects overly enthusiastic exclamation marks (`!`) and passive corporate speak.

### Test 3: Connector Regression Testing
* Runs automated assertions on standard test fixtures in `tests/fixtures/` to verify connectors handle:
  * Redirects (HTTP 301/302).
  * Slow responses (Timeout handling).
  * Empty or single-page static sites.
