import pytest

import {{cookiecutter.project_slug}}


@pytest.mark.parametrize(
    "question, expected",
    (
        ("What's the meaning of life?", "42"),
        ("Are you serious?", "42"),
        ("How old are you?", "42"),
        ("", "42"),
        ("This is not a question!", "42"),
    )
)
def test_deep_thought(question, expected):
    assert {{cookiecutter.project_slug}}.DeepThought.get_answer(question) == expected
