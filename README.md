# 📉 Denoising ECG Signals Using Conv1D-Based Autoencoder and Wavelet-MLP

This project explores the application of a denoising **Convolutional Autoencoder (CAE)** using **1D convolutional layers (Conv1D)** for removing noise from **electrocardiogram (ECG)** signals.

---

## 🧠 Background

ECG signals are essential for diagnosing cardiac abnormalities but are often affected by various types of noise, such as:

- **Baseline Wander (BW)**
- **Muscle Artifact (MA)**
- **Electrode Motion (EM)**

These disturbances can hinder accurate interpretation and analysis.

---

## 🧰 Methods

### ✅ Convolutional Autoencoder (CAE)

- Operates in the **time domain**
- Uses Conv1D layers to reconstruct clean signals
- Learns a mapping from noisy to clean ECG signals

---

## 📊 Experiments & Results

Two types of composite noise datasets (Noise 1 and Noise 2) were tested on two ECG channels (MLII and V5). The following metrics were used for evaluation:

- **RMSE (Root Mean Square Error)**
- **PRD (Percentage Root-mean-square Difference)**

### 🔬 Channel MLII vs Noise 1

| Noise Type       | Avg. RMSE | Avg. PRD (%) |
| ---------------- | --------- | ------------ |
| Baseline Wander  | 0.0324    | 18.20%       |
| Muscle Artifact  | 0.0360    | 20.27%       |
| Electrode Motion | 0.0396    | 22.11%       |

### 🔬 Channel MLII vs Noise 2

| Noise Type       | Avg. RMSE | Avg. PRD (%) |
| ---------------- | --------- | ------------ |
| Baseline Wander  | 0.0365    | 20.29%       |
| Muscle Artifact  | 0.0359    | 20.09%       |
| Electrode Motion | 0.0410    | 22.78%       |

### 🔬 Channel V5 vs Noise 1

| Noise Type       | Avg. RMSE | Avg. PRD (%) |
| ---------------- | --------- | ------------ |
| Baseline Wander  | 0.0411    | 17.75%       |
| Muscle Artifact  | 0.0457    | 20.23%       |
| Electrode Motion | 0.0501    | 21.55%       |

### 🔬 Channel V5 vs Noise 2

| Noise Type       | Avg. RMSE | Avg. PRD (%) |
| ---------------- | --------- | ------------ |
| Baseline Wander  | 0.0421    | 18.08%       |
| Muscle Artifact  | 0.0410    | 17.88%       |
| Electrode Motion | 0.0482    | 20.73%       |

---

## 🧾 Conclusion

The **Denoising Convolutional Autoencoder (CAE)** based on **Conv1D** has proven effective in removing noise from ECG signals while preserving essential physiological waveform structures.

With its **end-to-end architecture**, **high computational efficiency**, and operation purely in the **time domain**—without requiring external transformations—the model is well-suited for deployment in **real-time** or **embedded systems**.

The model's effectiveness varies depending on the **type of noise** and the **ECG channel configuration**:

- **Noise2** type was relatively easier to denoise.
- However, **Muscle Artifact** and **Electrode Motion** noise types remain more challenging and may require additional or hybrid approaches to achieve optimal performance.

This study highlights the CAE model's practical potential while also identifying areas for future enhancement in robust ECG signal denoising.
