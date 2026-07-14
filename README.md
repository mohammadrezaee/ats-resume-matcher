# ATS Resume Matcher

A simple Python tool that compares a resume PDF with a job description and returns a resume match score.

The project uses:

- `pypdf` to extract text from a resume PDF
- `scikit-learn` TF-IDF vectors to represent the resume and job description
- cosine similarity to calculate the match score

## Authors

- Mohammad Rezaee
- Hadis Arefanjazi

## Installation

```bash
python -m pip install -e ".[dev]"
```

## Usage

Place a resume PDF named `resume.pdf` in the project root, then run:

```bash
python -m ats_resume_matcher.main
```

You can also pass a resume path:

```bash
python -m ats_resume_matcher.main path/to/resume.pdf
```

Or read the job description from a text file:

```bash
python -m ats_resume_matcher.main path/to/resume.pdf --job-file job_description.txt
```

## Example

```text
Paste job description:
Python developer with machine learning experience
Resume match: 42.7%
```

## Project Structure

```text
ats-resume-matcher/
├── src/
│   └── ats_resume_matcher/
│       ├── __init__.py
│       ├── matcher.py
│       └── main.py
├── tests/
│   └── test_matcher.py
├── README.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
└── LICENSE
```

## Testing

```bash
pytest
```

## Limitations

- The score is based on word overlap and TF-IDF similarity, not a full ATS system.
- PDF extraction quality depends on the resume PDF format.
- The tool does not rewrite resumes or guarantee hiring outcomes.
