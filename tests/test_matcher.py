"""Tests for ATS resume matching behavior."""

import pytest

from ats_resume_matcher.matcher import calculate_match_score


def test_calculate_match_score_higher_for_related_text() -> None:
    resume = "Python machine learning data engineering FastAPI"
    related_job = "Python developer with machine learning and data engineering"
    unrelated_job = "Graphic designer with illustration and typography"

    related_score = calculate_match_score(resume, related_job)
    unrelated_score = calculate_match_score(resume, unrelated_job)

    assert related_score > unrelated_score


def test_calculate_match_score_rejects_empty_resume() -> None:
    with pytest.raises(ValueError, match="Resume text is empty"):
        calculate_match_score("", "Python developer")


def test_calculate_match_score_rejects_empty_job_description() -> None:
    with pytest.raises(ValueError, match="Job description is empty"):
        calculate_match_score("Python developer", "")
