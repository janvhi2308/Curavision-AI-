"""
CuraVision AI – Backend API Tests
===================================
Author : Janhvi Chaurasia  <janvhi2308@gmail.com>
Role   : Backend & API Engineer
Module : Functional tests for the FastAPI REST endpoints.
         Validates request/response contracts for all three endpoints.
"""
import requests

BASE_URL = "http://127.0.0.1:8000"


def test_health_check():
    """Test that the backend is online and responding."""
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    print("✅ Health check passed")


def test_predict_risk_low():
    """Test predict-risk endpoint with a low-risk patient profile."""
    payload = {
        "gender": 0,
        "age": 28.0,
        "hypertension": 0,
        "heart_disease": 0,
        "bmi": 22.5,
        "HbA1c_level": 5.1,
        "blood_glucose_level": 90,
        "smoking_history": "never"
    }
    response = requests.post(f"{BASE_URL}/predict-risk", json=payload, timeout=60)
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert "risk_score" in data
    assert "status" in data
    print(f"✅ predict-risk (low-risk) → {data['status']} ({data['risk_score']:.2%})")


def test_predict_risk_high():
    """Test predict-risk endpoint with a high-risk patient profile."""
    payload = {
        "gender": 1,
        "age": 60.0,
        "hypertension": 1,
        "heart_disease": 1,
        "bmi": 35.0,
        "HbA1c_level": 8.5,
        "blood_glucose_level": 210,
        "smoking_history": "current"
    }
    response = requests.post(f"{BASE_URL}/predict-risk", json=payload, timeout=60)
    assert response.status_code == 200
    data = response.json()
    assert data["prediction"] in [0, 1]
    print(f"✅ predict-risk (high-risk) → {data['status']} ({data['risk_score']:.2%})")


def test_clinical_rag_chat():
    """Test the RAG chat endpoint returns a grounded clinical response."""
    payload = {"question": "What are the warning signs of melanoma?"}
    response = requests.post(f"{BASE_URL}/clinical-rag-chat", json=payload, timeout=120)
    assert response.status_code == 200
    data = response.json()
    assert "clinical_response" in data
    assert len(data["clinical_response"]) > 10
    print(f"✅ clinical-rag-chat → response length: {len(data['clinical_response'])} chars")


def test_integrated_diagnosis():
    """Test the integrated diagnosis endpoint with a sample prediction."""
    payload = {
        "vision_prediction": "Melanocytic nevi (nv)",
        "confidence": 0.87,
        "symptom_description": "Slight itching around the mole for 2 weeks"
    }
    response = requests.post(
        f"{BASE_URL}/analyze/integrated-diagnosis", json=payload, timeout=120
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "diagnosis_report" in data
    print(f"✅ integrated-diagnosis → report generated ({len(data['diagnosis_report'])} chars)")


if __name__ == "__main__":
    print("🧪 Running CuraVision AI Backend Tests\n")
    test_health_check()
    test_predict_risk_low()
    test_predict_risk_high()
    test_clinical_rag_chat()
    test_integrated_diagnosis()
    print("\n🎉 All tests passed!")
