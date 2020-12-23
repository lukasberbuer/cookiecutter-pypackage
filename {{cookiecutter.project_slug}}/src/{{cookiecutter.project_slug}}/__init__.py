"""Top-level package for {{ cookiecutter.project_name }}."""

import logging

logger = logging.getLogger(__name__)


class DeepThought:
    """
    Provides answer to the ultimate question of life, the universe, and everything.

    References:
        - https://en.wikipedia.org/wiki/List_of_The_Hitchhiker%27s_Guide_to_the_Galaxy_characters
    """

    THE_ANSWER = 42  #: The answer to all questions

    @classmethod
    def get_answer(cls, question: str) -> str:
        """
        Get the answer to your question.

        Args:
            question: Your question - can be anything

        Returns:
            The Answer to your question
        """
        logger.info(f"Deep Thought was asked for an answer to: '{question}'")
        return str(cls.THE_ANSWER)

    def find_better_question(self) -> str:
        """Find a better question to ask for."""
        ...
