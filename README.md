# 🩺 CuraVision AI

> AI-assisted health screening platform combining skin-lesion computer vision,
> chronic-disease risk prediction, and a grounded clinical RAG assistant.

---

## What it does

CuraVision AI brings three AI capabilities into a single, focused health workspace:

| Feature | Description |
|---------|-------------|
| 🔬 **Skin-lesion detection** | Upload a dermatology image — EfficientNet-B4 classifies it across 7 HAM10000 categories and Grad-CAM highlights the region of interest |
| 📊 **Chronic-disease risk** | Enter vitals and lab values — a trained scikit-learn model predicts diabetes risk and an LLM generates a patient-friendly explanation |
| 💬 **Clinical RAG assistant** | Ask medical questions — Llama 3.2 answers strictly from a ChromaDB knowledge base of clinical guidelines and MT-Samples transcriptions |

> ⚠️ CuraVision is an educational AI screening tool. It does **not** replace examination, diagnosis, or treatment by a qualified healthcare professional.

---

## Tech Stack

| Layer | Technologies |
|-------|-------------|
| Frontend | Streamlit, Plotly |
| Backend API | FastAPI, Pydantic, Uvicorn |
| Computer Vision | EfficientNet-B4 (timm), PyTorch, Grad-CAM |
| NLP / LLM | Llama 3.2:3b (Ollama), nomic-embed-text, ChromaDB, LangChain |
| Data / ML | scikit-learn, pandas, NumPy, joblib |
| Auth & Storage | Supabase |

---

## Project Structure

```
Curavision-Ai/
├── main.py                      # FastAPI backend (Janhvi Chaurasia)
├── rag_chat.py                  # RAG pipeline runner (Khushi Burman)
├── ingest.py                    # Document ingestion (Khushi Burman)
├── ingest_mtsamples.py          # MT-Samples ingestion (Khushi Burman)
├── preprocessing.py             # Data preprocessing (Malishka Chawdhery)
├── check_deps.py                # Dependency checker (Malishka Chawdhery)
├── test_query.py                # RAG tests (Malishka Chawdhery)
├── chroma_db/                   # Persisted vector DB (Khushi Burman)
├── data/                        # Datasets & notebooks (Malishka Chawdhery)
│   ├── diabetes_model.joblib
│   ├── diabetes_prediction_dataset.csv
│   └── *.ipynb
├── docs/                        # Clinical guideline docs
└── curavision-ai(2)/            # Streamlit frontend
    ├── app.py                   # Landing page (Maahi Chaurasiya)
    ├── theme.py                 # Shared UI theme (Maahi Chaurasiya)
    ├── backend.py               # API client (Janhvi Chaurasia)
    ├── supabase_client.py       # DB/auth client (Janhvi Chaurasia)
    ├── requirements.txt
    ├── pages/
    │   ├── home.py              # Overview (Maahi Chaurasiya)
    │   ├── dashboard.py         # Charts & trends (Maahi Chaurasiya)
    │   ├── disease_detection.py # Detection UI (Maahi + Nehal)
    │   ├── assistant.py         # Chat UI (Maahi + Khushi)
    │   ├── reports.py           # Reports (Maahi Chaurasiya)
    │   ├── profile.py           # User profile (Maahi Chaurasiya)
    │   ├── login.py             # Auth (Janhvi Chaurasia)
    │   └── signup.py            # Registration (Janhvi Chaurasia)
    └── skin_model/
        ├── inference.py         # EfficientNet-B4 + Grad-CAM (Nehal Verma)
        └── best_skin_model.pth  # Trained weights (Nehal Verma)
```

---

## Quick Start

### 1. Clone and set up environment

```bash
git clone https://github.com/khushi-burman/curavision-ai.git
cd curavision-ai
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r curavision-ai(2)/requirements.txt
```

### 2. Set up Supabase secrets

Create `curavision-ai(2)/.streamlit/secrets.toml`:

```toml
SUPABASE_URL = "your-supabase-url"
SUPABASE_KEY = "your-supabase-anon-key"
```

### 3. Pull and start Ollama models

```bash
ollama pull llama3.2:3b
ollama pull nomic-embed-text
```

### 4. Ingest clinical documents into ChromaDB

```bash
python ingest.py
python ingest_mtsamples.py
```

### 5. Start the FastAPI backend

```bash
uvicorn main:app --reload --port 8000
```

### 6. Start the Streamlit frontend

```bash
cd "curavision-ai(2)"
streamlit run app.py
```

---

## Team

| Name | Role | GitHub |
|------|------|--------|
| Maahi Chaurasiya | Frontend Developer | [@maahichaurasiya](https://github.com/maahichaurasiya) |
| Janhvi Chaurasia | Backend & API Engineer | [@janvhi2308](https://github.com/janvhi2308) |
| Nehal Verma | Computer Vision Expert | [@vermanehal](https://github.com/vermanehal) |
| Khushi Burman | NLP & LLM Engineer | [@khushiBurman](https://github.com/khushiBurman) |
| Malishka Chawdhery | DevOps, Data & Testing | [@malishka491](https://github.com/malishka491) |

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for a full breakdown of each person's file ownership.

---

## Disclaimer

CuraVision AI provides AI-assisted screening and educational guidance.
It does not replace examination, diagnosis, or treatment by a qualified healthcare professional.
For urgent symptoms or serious concerns, seek appropriate medical care directly.
