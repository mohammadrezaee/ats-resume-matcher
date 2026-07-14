"""Core resume and job-description similarity logic."""

from pathlib import Path

from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_pdf_text(pdf_path: str | Path) -> str:
    """Extract text from all pages of a resume PDF."""
    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(f"Resume PDF not found: {path}")
    if path.suffix.lower() != ".pdf":
        raise ValueError("Resume file must be a PDF.")

    reader = PdfReader(str(path))
    return " ".join(page.extract_text() or "" for page in reader.pages).strip()


def calculate_match_score(resume_text: str, job_description: str) -> float:
    """Return a TF-IDF cosine similarity match score from 0 to 100."""
    if not resume_text.strip():
        raise ValueError("Resume text is empty.")
    if not job_description.strip():
        raise ValueError("Job description is empty.")

    vectors = TfidfVectorizer(stop_words="english").fit_transform(
        [resume_text, job_description]
    )
    return float(cosine_similarity(vectors[0], vectors[1])[0][0] * 100)
