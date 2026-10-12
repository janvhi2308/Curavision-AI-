# Contributors

CuraVision AI is a group project built by a team of five. Each contributor
owns a distinct layer of the system, described below.

---

## 👩‍💻 Maahi Chaurasiya — Frontend Developer
**GitHub:** [@maahichaurasiya](https://github.com/maahichaurasiya)  
**Email:** mahichaurasiya70@gmail.com

Designed and implemented the entire Streamlit user interface:

| File | Description |
|------|-------------|
| `curavision-ai(2)/app.py` | Landing page and app entry point |
| `curavision-ai(2)/theme.py` | Shared CSS design tokens, typography, colour palette and reusable UI components |
| `curavision-ai(2)/pages/home.py` | Home / overview page post-login |
| `curavision-ai(2)/pages/dashboard.py` | Interactive Plotly health dashboard and charts |
| `curavision-ai(2)/pages/disease_detection.py` | Disease detection UI (skin + chronic risk) |
| `curavision-ai(2)/pages/assistant.py` | Clinical assistant chat interface |
| `curavision-ai(2)/pages/reports.py` | Assessment reports history and presentation |
| `curavision-ai(2)/pages/profile.py` | User profile and settings page |

---

## 👩‍💻 Janhvi Chaurasia — Backend & API Engineer
**GitHub:** [@janvhi2308](https://github.com/janvhi2308)  
**Email:** janvhi2308@gmail.com

Built the FastAPI backend, REST endpoints and all database/auth integration:

| File | Description |
|------|-------------|
| `main.py` | FastAPI app — `/predict-risk`, `/clinical-rag-chat` and `/analyze/integrated-diagnosis` endpoints |
| `curavision-ai(2)/backend.py` | HTTP client connecting Streamlit frontend to FastAPI |
| `curavision-ai(2)/supabase_client.py` | Supabase client for auth and report persistence |
| `curavision-ai(2)/pages/login.py` | Login flow and session management |
| `curavision-ai(2)/pages/signup.py` | New user registration with Supabase Auth |

---

## 👩‍💻 Nehal Verma — Computer Vision Expert
**GitHub:** [@vermanehal](https://github.com/vermanehal)  
**Email:** nehalverma9d@gmail.com

Trained and evaluated the skin-lesion classifier and built the explainability pipeline:

| File | Description |
|------|-------------|
| `curavision-ai(2)/skin_model/inference.py` | EfficientNet-B4 inference engine with Grad-CAM saliency overlay generation |
| `curavision-ai(2)/skin_model/best_skin_model.pth` | Trained model weights (HAM10000, 7-class) |
| `data/02_RAG_ChromaDB_Pipeline.ipynb` | Model training and evaluation notebook |

**Model details:** EfficientNet-B4 trained on the HAM10000 dataset across 7 skin-lesion classes (akiec, bcc, bkl, df, mel, nv, vasc) with Grad-CAM visual explanations.

---

## 👩‍💻 Khushi Burman — NLP & LLM Engineer
**GitHub:** [@khushiBurman](https://github.com/khushiBurman)  
**Email:** khushiiix077@gmail.com

Designed and built the full RAG pipeline and clinical LLM synthesis layer:

| File | Description |
|------|-------------|
| `rag_chat.py` | Standalone RAG query runner (ChromaDB + Llama 3.2) |
| `ingest.py` | Clinical guideline document ingestion into ChromaDB |
| `ingest_mtsamples.py` | MT-Samples medical transcription ingestion |
| `chroma_db/` | Persisted vector database for clinical RAG |
| `docs/sample_guideline.txt` | Sample clinical guideline documents |

**Tech stack:** ChromaDB · nomic-embed-text · Llama 3.2:3b · LangChain

---

## 👩‍💻 Malishka Chawdhery — DevOps, Data & Testing Engineer
**GitHub:** [@malishka491](https://github.com/malishka491)  
**Email:** Malishkachawdhery@gmail.com

Handled data preparation, environment setup, deployment and functional testing:

| File | Description |
|------|-------------|
| `preprocessing.py` | Diabetes dataset and HAM10000 image cleaning and feature engineering |
| `check_deps.py` | Dependency validation script for environment setup |
| `test_query.py` | Functional tests for RAG query pipeline |
| `data/Medical_Data_Cleaning.ipynb` | Data cleaning and EDA notebook |
| `data/diabetes_prediction_dataset.csv` | Raw diabetes dataset |
| `data/cleaned_diabetes_data.csv` | Preprocessed diabetes dataset |
| `data/diabetes_model.joblib` | Trained scikit-learn diabetes risk model |
| `curavision-ai(2)/requirements.txt` | Python dependency manifest |
| `.gitignore` | Git ignore rules |

---

## Architecture Overview

```
┌────────────────────────────────────────────────────────┐
│              CuraVision AI — System Map                │
├──────────────┬─────────────────────────────────────────┤
│  Streamlit   │  app.py · pages/ · theme.py             │
│  Frontend    │  ← Maahi Chaurasiya                     │
├──────────────┼─────────────────────────────────────────┤
│  Auth &      │  login.py · signup.py · supabase_client │
│  Reports     │  ← Janhvi Chaurasia                     │
├──────────────┼─────────────────────────────────────────┤
│  FastAPI     │  main.py · backend.py                   │
│  Backend     │  ← Janhvi Chaurasia                     │
├──────────────┼─────────────────────────────────────────┤
│  Computer    │  skin_model/inference.py · .pth weights │
│  Vision      │  ← Nehal Verma                          │
├──────────────┼─────────────────────────────────────────┤
│  RAG /       │  rag_chat.py · ingest*.py · chroma_db/  │
│  NLP         │  ← Khushi Burman                        │
├──────────────┼─────────────────────────────────────────┤
│  Data &      │  preprocessing.py · data/ · check_deps  │
│  DevOps      │  ← Malishka Chawdhery                   │
└──────────────┴─────────────────────────────────────────┘
```
