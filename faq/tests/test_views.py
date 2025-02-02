import pytest
from django.urls import reverse
from django.test import Client
from faq.models import FAQ


client = Client()


@pytest.mark.django_db
def test_get_faqs():
    """Test for GET api/faqs/ which returns FAQs in default (English) language."""
    FAQ.objects.create(
        question="What is Django ?",
        answer="Django is a Python web framework."
    )
    url = reverse("faqs")
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["en"]["question"] == "What is Django ?"


@pytest.mark.django_db
def test_get_faq_in_hindi():
    """Test for GET api/faqs/?lang="hi" which returns FAQs in Hindi language."""
    FAQ.objects.create(
        question="What is Django ?",
        answer="Django is a Python web framework."
    )
    url = reverse("faqs") + "?lang=hi"
    response = client.get(url)
    assert response.status_code == 200
    assert response.json()[0]["hi"]["question"] == "Django क्या है?"


@pytest.mark.django_db
def test_get_faq_invalid_language():
    """Test for GET api/faqs/?lang="tn" which returns an invalid language message."""
    FAQ.objects.create(
        question="What is Django ?",
        answer="Django is a Python web framework."
    )
    url = reverse("faqs") + "?lang=tn"
    response = client.get(url)
    assert response.status_code == 400
    assert response.json()["error"] == "Invalid language code"
    assert response.json()["message"] == "Supported languages are: hi, bn, te, en"


@pytest.mark.django_db
def test_post_faq():
    """Test for POST api/faqs-create/ which creates a new FAQ successfully."""
    url = reverse("faqs_create")
    data = {
        "question": "What is Python?",
        "answer": "Python is a programming language"
    }
    response = client.post(path=url, data=data, format="json")
    assert response.status_code == 201
    assert response.json()["message"] == "FAQ created successfully!"
    assert response.json()["data"]["en"]["question"] == "What is Python?"
