# CuraVision AI — API Reference

**Author:** Janhvi Chaurasia — Backend & API Engineer  
**GitHub:** [@janvhi2308](https://github.com/janvhi2308)

Base URL: `http://localhost:8000`

---

## Endpoints

### `GET /`
Health check — confirms the backend is running.

**Response:**
```json
{
  "status": "online",
  "system": "CuraVision AI Core Engine"
}
```

---

### `POST /predict-risk`
Predicts chronic disease (diabetes) risk from patient vitals and returns an LLM-generated explanation.

**Request body:**
```json
{
  "gender": 1,
  "age": 45.0,
  "hypertension": 0,
  "heart_disease": 0,
  "bmi": 27.5,
  "HbA1c_level": 6.2,
  "blood_glucose_level": 130,
  "smoking_history": "never"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `gender` | int | `0` = Female, `1` = Male |
| `age` | float | Patient age in years |
| `hypertension` | int | `0` or `1` |
| `heart_disease` | int | `0` or `1` |
| `bmi` | float | Body Mass Index |
| `HbA1c_level` | float | HbA1c percentage |
| `blood_glucose_level` | float | Blood glucose in mg/dL |
| `smoking_history` | str | `"never"`, `"current"`, or `"former"` |

**Response:**
```json
{
  "prediction": 0,
  "status": "Low Risk",
  "risk_score": 0.1243,
  "explanation": "## Assessment Breakdown\n..."
}
```

---

### `POST /clinical-rag-chat`
Answers a medical question using the RAG pipeline (ChromaDB + Llama 3.2).

**Request body:**
```json
{
  "question": "What are the early warning signs of melanoma?"
}
```

**Response:**
```json
{
  "query": "What are the early warning signs of melanoma?",
  "clinical_response": "Based on the clinical context...",
  "retrieved_context": ["...chunk 1...", "...chunk 2..."]
}
```

---

### `POST /analyze/integrated-diagnosis`
Synthesises a skin-vision model prediction with patient-reported symptoms into a structured clinical report.

**Request body:**
```json
{
  "vision_prediction": "Melanocytic nevi (nv)",
  "confidence": 0.8712,
  "symptom_description": "Itching around the mole for 2 weeks"
}
```

**Response:**
```json
{
  "status": "success",
  "vision_prediction": "Melanocytic nevi (nv)",
  "confidence": 0.8712,
  "diagnosis_report": "## Clinical Correlation\n..."
}
```

---

## Error Handling

All endpoints return HTTP `500` with a `detail` field on internal errors:

```json
{
  "detail": "error message here"
}
```

---

## Notes

- LLM calls (Ollama / Llama 3.2) have a **300-second timeout**
- The model is warmed up on startup via a background thread
- Interactive docs available at `http://localhost:8000/docs` (Swagger UI)
