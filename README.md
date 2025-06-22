# 🔍 Anomaly Detection UI with Isolation Forest

This project provides a simple and interactive UI for running **Anomaly Detection** using the **Isolation Forest** algorithm via **Streamlit**. It allows users to upload a CSV file, tune the contamination rate, and visualize or download the anomaly detection results.

---

## 📦 Features

- Upload your own CSV data
- Tune contamination rate interactively
- Detect anomalies using Isolation Forest
- Download results with anomaly flags
- Built using Python and Streamlit — beginner friendly!

---

## 🖼️ Demo

![UI Demo](demo.gif) <!-- Optional: You can create a screen recording later -->

---

## 📁 Project Structure

```
anomaly_ui/
│
├── app.py            # Streamlit UI code
├── model.py          # Isolation Forest training & prediction logic
├── sample_data.csv   # Optional sample CSV for testing
└── README.md         # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-org/anomaly_ui.git
cd anomaly_ui
```

### 2️⃣ Set Up the Environment

Using `conda` or `miniforge`:

```bash
conda create -n anomaly-ui python=3.9 -y
conda activate anomaly-ui
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
streamlit run app.py
```

This will open a browser window with the UI.

---

## 🧪 How to Use

1. Upload a CSV file with numeric data.
2. Adjust the **contamination slider** (controls expected % of anomalies).
3. Click **"Run Anomaly Detection"**.
4. View the table with "Normal"/"Anomaly" results.
5. Download the annotated CSV file.

---

## 📌 Sample Data Format

```csv
temperature,pressure,vibration
70,101.3,0.05
80,98.7,0.07
100,110.5,0.10
...
```

Ensure your CSV contains **only numeric columns** for best results.

---

## 📚 Dependencies

- Python 3.8+
- Streamlit
- Pandas
- scikit-learn

You can create a `requirements.txt` with:

```
streamlit
pandas
scikit-learn
```

---

## 🧠 Learn More

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Isolation Forest – Scikit-learn Docs](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html)

---

## 🛠️ TODO (Optional)

- [ ] Add support for categorical column handling
- [ ] Visualize anomalies using plots
- [ ] Deploy using Streamlit Cloud or Docker

---

## 👤 Author

ABC
[GitHub](https://github.com/your-github-handle)

---

## 📄 License

MIT License – Use it freely with attribution.