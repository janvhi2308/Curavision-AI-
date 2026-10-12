# Skin-Lesion Classification Model

**Author:** Nehal Verma — Computer Vision Expert  
**GitHub:** [@vermanehal](https://github.com/vermanehal)

---

## Model Architecture

| Property | Detail |
|----------|--------|
| **Architecture** | EfficientNet-B4 (via `timm`) |
| **Dataset** | HAM10000 — 10,015 dermoscopy images |
| **Classes** | 7 skin-lesion categories |
| **Input size** | 224 × 224 RGB |
| **Normalisation** | ImageNet mean/std `[0.485, 0.456, 0.406]` / `[0.229, 0.224, 0.225]` |
| **Output** | Softmax probabilities over 7 classes |

---

## Class Labels

| ID | Code | Full Name |
|----|------|-----------|
| 0 | `akiec` | Actinic keratoses and intraepithelial carcinoma |
| 1 | `bcc` | Basal cell carcinoma |
| 2 | `bkl` | Benign keratosis-like lesions |
| 3 | `df` | Dermatofibroma |
| 4 | `mel` | Melanoma |
| 5 | `nv` | Melanocytic nevi |
| 6 | `vasc` | Vascular lesions |

---

## Grad-CAM Explainability

Grad-CAM (Gradient-weighted Class Activation Mapping) is used to generate
visual explanations of the model's predictions.

- **Target layer:** `model.blocks[-1][-1]` — last spatial block before the
  `conv_head` projection (avoids diffuse corner-biased heatmaps)
- **Output:** RGB heatmap overlay blended onto the original resized image
- **Library:** `pytorch-grad-cam`

---

## Inference Usage

```python
from skin_model.inference import load_skin_model, predict_image

model, device = load_skin_model('skin_model/best_skin_model.pth')
result = predict_image('path/to/lesion.jpg', model, device, generate_heatmap=True)

print(result['label'])           # e.g. "Melanocytic nevi (nv)"
print(result['confidence'])      # e.g. 0.8712
print(result['gradcam_overlay']) # PIL Image with heatmap
```

---

## Training Details

- Pre-trained ImageNet weights loaded via `timm`
- Fine-tuned on HAM10000 with class-balanced sampling
- Evaluated on held-out test split
- Model weights saved as `best_skin_model.pth` (best validation accuracy)

---

> ⚠️ This model is for educational and screening purposes only.
> Always consult a qualified dermatologist for clinical diagnosis.
