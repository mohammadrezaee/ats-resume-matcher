"""Command-line entry point for the ATS resume matcher."""

import argparse
from pathlib import Path

from .matcher import calculate_match_score, extract_pdf_text


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""
    parser = argparse.ArgumentParser(
        description="Compare a resume PDF with a job description using TF-IDF similarity."
    )
    parser.add_argument(
        "resume",
        nargs="?",
        default="resume.pdf",
        help="Path to the resume PDF. Defaults to resume.pdf.",
    )
    parser.add_argument(
        "--job-file",
        type=Path,
        help="Optional text file containing the job description.",
    )
    return parser


def main() -> None:
    """Run the resume matcher from the command line."""
    args = build_parser().parse_args()
    resume_text = extract_pdf_text(args.resume)

    if args.job_file:
        if not args.job_file.exists():
            raise FileNotFoundError(f"Job description file not found: {args.job_file}")
        job_description = args.job_file.read_text(encoding="utf-8")
    else:
        job_description = input("Paste job description:\n")

    score = calculate_match_score(resume_text, job_description)
    print(f"Resume match: {score:.1f}%")


if __name__ == "__main__":
    main()
