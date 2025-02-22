# **Weather Prediction Model Using ANN**

An interactive web application to predict weather parameters using **Artificial Neural Networks (ANN)**, built with **Streamlit** and integrated with **GitHub Actions** for continuous deployment.

---

## **Overview**

This project helps users predict temperature at different soil depths based on weather parameters like air temperature, rainfall, and day of the year. The models provided are trained on datasets from **Texas** and **New York**, offering region-specific predictions. The tool provides a simple and interactive interface where users can input values and receive predictions in real-time.

---

## **Features**

- 🌡 **Weather Prediction:** Predict temperature at various depths based on user inputs.
- 🎛 **Interactive UI:** Streamlit-powered interface for a seamless user experience.
- 📈 **Dynamic Input Fields:** Enter air temperature, rainfall, and day of the year for predictions.
- 📊 **Detailed Outputs:**
  - **Texas Model:**
    ```json
    {
      "Temp_0.9m": 26.4251,
      "Temp_1.8m": 26.3385
    }
    ```
  - **New York Model:**
    ```json
    {
      "Temp_0.3m_C": 26.4251,
      "Temp_0.6m_C": 26.3385,
      "Temp_0.91m_C": 26.5102,
      "Temp_1.21m_C": 26.4893
    }
    ```
- 🛡 **Error Handling:** Robust handling of invalid inputs.
- ⚙️ **CI/CD Integration:** Automated deployment using **GitHub Actions**.

---

## **Technologies Used**

- **Python**
- **TensorFlow/Keras** – ANN model development
- **Pandas & NumPy** – Data preprocessing
- **Streamlit** – Web application framework
- **GitHub Actions** – CI/CD pipeline

---

## **Installation & Setup**

### 1️⃣ **Clone the Repository**

```bash
git clone https://github.com/your-username/weather-prediction-model.git
cd weather-prediction-model
```

### 2️⃣ **Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

### 3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 4️⃣ **Add Model & Scaler Files**

Place the following files in the `models/` directory:

- `model_texas.h5`
- `model_newYork.h5`
- `scaler_texas.pkl`
- `scaler_newYork.pkl`

### 5️⃣ **Run the Application**

```bash
streamlit run main.py
```

---

## **CI/CD Pipeline with GitHub Actions**

### ⚡ **Workflow Configuration** (`.github/workflows/main.yml`)

```yaml
name: Streamlit CI/CD

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install Dependencies
        run: |
          pip install -r requirements.txt
      - name: Run Streamlit App
        run: |
          streamlit run main.py --server.headless true
```

---

## **Usage**

1. Launch the application using Streamlit.
2. Select the desired model (**Texas** or **New York**).
3. Enter values for:
   - 🌡 **Air Temperature (°C)**
   - 🌧 **Rainfall (inch)**
   - 📅 **Day of the Year (1-366)**
4. Click **Predict** to see the results.

---


## **Requirements**

```plaintext
streamlit==1.30.0
tensorflow==2.15.0
numpy==1.24.0
pandas==2.2.0
scikit-learn==1.5.0
pickle-mixin
```

---

## **Contributing**

1. 🍴 Fork the repository.
2. 🌿 Create a feature branch:
   ```bash
   git checkout -b feature/feature-name
   ```
3. 💾 Commit your changes:
   ```bash
   git commit -m "Added new feature"
   ```
4. 🚀 Push to the branch:
   ```bash
   git push origin feature/feature-name
   ```
5. 🔃 Open a pull request.

---

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgements**

- [Streamlit](https://streamlit.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [Scikit-Learn](https://scikit-learn.org/)
- [GitHub Actions](https://github.com/features/actions)

---

## **Connect**

- 🔗 GitHub: [sandeepbandi924](https://github.com/sandeepbandi924)
- 🔗 LinkedIn: [bandisandeep](https://www.linkedin.com/in/sandeepbandi/)

---

✨ **Happy Predicting! 🚀**

