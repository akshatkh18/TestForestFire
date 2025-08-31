
# 🌲 Forest Fire Prediction

This project predicts the likelihood of forest fires using machine learning models.  
It takes input features (like temperature, humidity, wind, etc.) and outputs whether a fire is likely to occur.  
The project also includes a simple web interface built with **Flask**.

---

## 🚀 Features
- Pre-trained ML model for fire prediction.
- Flask web app with user-friendly forms.
- Input standardization before prediction.
- HTML templates (`home.html`, `index.html`) for UI.
- Modular project structure.

---

## 📂 Project Structure
```
Algerian_Forest_Fire/
│-- models/ # Contains .pkl model files
│-- templates/ # HTML files (home.html, index.html)
│-- static/ # (optional) CSS/JS files
│-- app.py # Main Flask application
│-- requirements.txt # Dependencies
│-- README.md # Project documentation
```

---

## 🛠 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/akshatkh18/TestForestFire.git
cd TestForestFire
````

### 2. Create and activate virtual environment (recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask app

```bash
python app.py
```

Now open your browser and visit **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 📦 Requirements

* Python 3.8+
* Flask
* Scikit-learn
* Pandas
* Numpy

(Install all via `requirements.txt`)

---

## 🔮 Future Improvements

* Deploy on **Render/Heroku/Streamlit** for public access.
* Add **real-time weather API integration**.
* Improve UI design.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📜 License

This project is licensed under the MIT License.

---
