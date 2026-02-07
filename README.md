# iitbbsr-causal-explanation-system

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

A causal explanation system for customer support transcripts. The pipeline detects an outcome category from a query, extracts early-turn triggers, ranks causal factors with TF-IDF, retrieves supporting evidence, and generates a structured explanation.

## Table of Contents
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Full Setup](#full-setup)
- [Data](#data)
- [Preprocessing](#preprocessing)
- [Training](#training)
- [Inference / Run](#inference--run)
- [Evaluation & Metrics](#evaluation--metrics)
- [Scripts & Modules](#scripts--modules)
- [Testing](#testing)
- [Deployment & Docker](#deployment--docker)
- [Troubleshooting & Common Issues](#troubleshooting--common-issues)
- [Contributing](#contributing)
- [License & Attribution](#license--attribution)
- [Contact / Citation](#contact--citation)
- [Notes & Assumptions](#notes--assumptions)

## Quick Start
Minimum steps from clone to a working demo run.

```bash
# 1) Create and activate a virtual environment (Linux/macOS)
python -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
# python -m venv .venv
# .\.venv\Scripts\Activate.ps1

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the interactive demo
python src/main.py
```

When prompted, enter a free-text customer query (e.g., “My order shows delivered but I never received it.”). The system will print a structured causal explanation and append outputs to `outputs/submission_output.csv`.

## Project Structure
```
.
├── data/
│   ├── queries.csv
│   └── transcript.json
├── models/
├── outputs/
├── report/
│   ├── PROJECT_REPORT.docx
│   └── PROJECT_REPORT.pdf
├── requirements.txt
└── src/
    ├── data_loader.py
    ├── evidence_extractor.py
    ├── explanation_generator.py
    ├── factor_analysis.py
    ├── factor_cleaner.py
    ├── main.py
    ├── preprocessing.py
    ├── retrieval.py
    └── trigger_extractor.py
```

## Full Setup
### 1) Environment
```bash
python -m venv .venv
source .venv/bin/activate
# Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2) Verify data is present
The demo expects the transcript dataset at `data/transcript.json` and will write output to `outputs/submission_output.csv`.

## Data
### Source
The dataset is included in this repository:
- `data/transcript.json` (primary transcript dataset)
- `data/queries.csv` (example queries)

### Expected raw data layout
Example directory tree:
```
data/
├── queries.csv
└── transcript.json
```

### Transcript schema (excerpt)
`data/transcript.json` contains a top-level `transcripts` list. Each entry includes:
- `transcript_id` (int)
- `time_of_interaction` (string)
- `domain` (string)
- `intent` (string)
- `reason_for_call` (string)
- `conversation` (list of `{speaker, text}` turns)

### Outputs
The interactive run writes a CSV file to:
- `outputs/submission_output.csv`

Each row includes:
- `Query Id`
- `Query`
- `Query Category`
- `System Output` (text block with factors + evidence)
- `Remarks`

## Preprocessing
There is a placeholder preprocessing module at `src/preprocessing.py`, but no preprocessing steps are currently implemented. If you add preprocessing, document inputs and outputs here and update `src/preprocessing.py`.

## Training
This project currently relies on heuristic outcome detection and TF-IDF-based factor analysis. There is no model training script in the repository.

TODO: Add training instructions if/when a train script or configuration is introduced.

## Inference / Run
### Interactive CLI (primary flow)
Run the interactive mode, which continually prompts for queries and writes results to `outputs/submission_output.csv`:

```bash
python src/main.py
```

Sample input:
```
My account is locked and I cannot log in.
```

Expected console output (example excerpt):
```
Outcome Event: Account Access Issues

Causal Factors:
- Login Failure
- Password Reset

Explanation:
In 'Account Access Issues' cases, customers describe login failures or security holds following credential resets. These access restrictions correspond to account access issue categorization.
```

### Programmatic usage (Python)
```python
import sys
sys.path.append("src")

from data_loader import load_transcripts
from retrieval import detect_outcome_from_query
from trigger_extractor import extract_trigger_text
from factor_analysis import extract_top_factors_from_texts
from evidence_extractor import extract_evidence
from explanation_generator import generate_structured_explanation

transcripts = load_transcripts("data/transcript.json")
query = "My order shows delivered but I never received it."

outcome = detect_outcome_from_query(query, transcripts["intent"].unique())
positive_texts, negative_texts = extract_trigger_text(transcripts, outcome)
terms = extract_top_factors_from_texts(positive_texts, negative_texts, top_n=3)
evidence = extract_evidence(transcripts, outcome, terms)
explanation = generate_structured_explanation(outcome, terms, evidence)

print(explanation)
```

## Evaluation & Metrics
There is no dedicated evaluation script in the repository.

TODO: Add an evaluation script and document expected metrics/log locations once available.

## Scripts & Modules
> **Note:** For the import examples below, ensure `src/` is on your `PYTHONPATH` (e.g., `export PYTHONPATH=src` on Linux/macOS or `set PYTHONPATH=src` on Windows CMD), or use `sys.path.append(\"src\")` in code.

### [`src/main.py`](src/main.py)
- **Purpose:** Interactive CLI that accepts queries, detects outcome events, extracts causal factors and evidence, then writes results to `outputs/submission_output.csv`.
- **Usage:**
  ```bash
  python src/main.py
  ```
- **Inputs:**
  - `data/transcript.json` (transcript dataset)
  - User-provided query text from stdin
- **Outputs:**
  - `outputs/submission_output.csv`
- **Environment variables/config:** None.

### [`src/data_loader.py`](src/data_loader.py)
- **Purpose:** Load transcript JSON into a pandas DataFrame.
- **Usage (import):**
  ```python
  from data_loader import load_transcripts
  df = load_transcripts("data/transcript.json")
  ```
- **Inputs:** `data/transcript.json`
- **Outputs:** pandas DataFrame with `transcript_id`, `domain`, `intent`, `conversation`.
- **Environment variables/config:** None.

### [`src/retrieval.py`](src/retrieval.py)
- **Purpose:** Map a user query to a known outcome intent using keyword matching and normalization.
- **Usage (import):**
  ```python
  from retrieval import detect_outcome_from_query
  outcome = detect_outcome_from_query(query, available_intents)
  ```
- **Inputs:** query string + list of intent labels
- **Outputs:** matched intent label or `None`
- **Environment variables/config:** None.

### [`src/trigger_extractor.py`](src/trigger_extractor.py)
- **Purpose:** Extract early-turn trigger text from conversations for positive/negative samples.
- **Usage (import):**
  ```python
  from trigger_extractor import extract_trigger_text
  positive, negative = extract_trigger_text(df, outcome, num_turns=6, customer_only=True)
  ```
- **Inputs:** DataFrame, target outcome, `num_turns`, `customer_only`
- **Outputs:** list of positive texts, list of negative texts
- **Environment variables/config:** None.

### [`src/factor_analysis.py`](src/factor_analysis.py)
- **Purpose:** Rank candidate causal factors with TF-IDF and select top clean terms.
- **Usage (import):**
  ```python
  from factor_analysis import extract_top_factors_from_texts
  terms = extract_top_factors_from_texts(positive, negative, top_n=20)
  ```
- **Inputs:** positive/negative text lists, `top_n`
- **Outputs:** list of top causal factor terms
- **Environment variables/config:** None.

### [`src/evidence_extractor.py`](src/evidence_extractor.py)
- **Purpose:** Retrieve evidence snippets for each factor from relevant transcripts.
- **Usage (import):**
  ```python
  from evidence_extractor import extract_evidence
  evidence = extract_evidence(df, outcome, terms, max_examples=3)
  ```
- **Inputs:** DataFrame, outcome label, factor list, `max_examples`
- **Outputs:** dict mapping factor -> evidence list
- **Environment variables/config:** None.

### [`src/explanation_generator.py`](src/explanation_generator.py)
- **Purpose:** Build a structured causal explanation with factors and reasoning text.
- **Usage (import):**
  ```python
  from explanation_generator import generate_structured_explanation
  explanation = generate_structured_explanation(outcome, terms, evidence)
  ```
- **Inputs:** outcome label, factor list, evidence dict
- **Outputs:** dict with `outcome_event`, `causal_factors`, `causal_reasoning`
- **Environment variables/config:** None.

### [`src/factor_cleaner.py`](src/factor_cleaner.py)
- **Purpose:** Clean and normalize factor terms (currently unused by default pipeline).
- **Usage (import):**
  ```python
  from factor_cleaner import clean_factor
  clean = clean_factor("Account number")
  ```
- **Inputs:** raw factor term string
- **Outputs:** cleaned term string or `None`
- **Environment variables/config:** None.

### [`src/preprocessing.py`](src/preprocessing.py)
- **Purpose:** Placeholder for future preprocessing steps.
- **Usage:** TODO.
- **Inputs/Outputs:** TODO.
- **Environment variables/config:** None.

## Testing
There are no automated tests currently included.

TODO: Add tests (e.g., `pytest`) to validate retrieval, factor extraction, and evidence selection.

## Deployment & Docker
No Dockerfile or docker-compose configuration is present.

TODO: Add Docker instructions if containerization is needed.

## Troubleshooting & Common Issues
- **`FileNotFoundError: data/transcript.json`**
  - Ensure you are running from the repository root and that `data/transcript.json` exists.
- **`ModuleNotFoundError` for packages**
  - Reinstall dependencies: `pip install -r requirements.txt`.
- **Slow performance on large transcripts**
  - Consider reducing `num_turns` in `extract_trigger_text` or limiting dataset size during development.

## Contributing
If you plan to contribute:
1. Open an issue describing the change or bug.
2. Create a feature branch.
3. Add or update tests when possible.
4. Submit a pull request with a clear description, reproduction steps (if applicable), and screenshots/logs.

Suggested PR template:
```
## Summary
- ...

## Testing
- ...
```

## License & Attribution
No LICENSE file is present.

TODO: Add a LICENSE file (e.g., MIT, Apache-2.0) and update this section.

## Contact / Citation
No maintainer or citation metadata is included.

TODO: Add contact details or a CITATION.cff file for academic use.

## Notes & Assumptions
- TODO: Training instructions are omitted because no training scripts/configs exist in the repo.
- TODO: Evaluation instructions are omitted because no evaluation script is present.
- TODO: Docker instructions are omitted because no Dockerfile/docker-compose file exists.
- TODO: License and contact info are missing and should be added by maintainers.
