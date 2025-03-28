import pytest
from faq.models import FAQ


@pytest.mark.django_db
def test_faq_object_creation():
    """Test for FAQ object creation."""
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a Python web framework."
    )

    assert faq.question == "What is Django?"
    assert faq.answer == "Django is a Python web framework."


@pytest.mark.django_db
def test_get_translation_generation():
    """Test retrieving translation using the get_translation method."""
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a Python web framework."
    )

    assert faq.get_translation("hi") == {
        "question": "Django क्या है?",
        "answer": "Django पायथन वेब फ्रेमवर्क है"
    }

    assert faq.get_translation("te") == {
        "question": "జంగో అంటే ఏమిటి?",
        "answer": "జంగో పైథాన్ వెబ్ ఫ్రేమ్‌వర్క్"
    }

    assert faq.get_translation("tn") == faq.get_translation("en")
