🌾 Crop Recommendation System
A machine learning-based full-stack web application that recommends the most suitable crop to grow based on soil and weather parameters.

<!-- Replace with real screenshot URL -->

🚀 Features
✅ Manual input of agro-climatic data (N, P, K, temperature, humidity, pH, rainfall)

✅ Crop prediction using trained ML model

✅ Flask backend with HTML/CSS frontend

✅ Responsive UI with animations

✅ Ready for future live integration using GPS & APIs

🧪 Tech Stack
Frontend: HTML5, CSS3 (with animations), Bootstrap (optional)

Backend: Flask (Python)

ML Model: Scikit-learn (Random Forest or similar)

Deployment: Render / Streamlit / Vercel (not preferred for large model)

📦 Installation (Local)
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/chethan722003/cropRecommendation.git
cd cropRecommendation
2. Create virtual environment
bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the app
bash
Copy
Edit
python app.py
Then open: http://localhost:5000

💡 Future Work
🌐 Live weather & soil data using APIs

📍 Auto-locate user via GPS for local crop suggestions

📊 Dashboard with analytics for farmers

☁️ Cloud deployment on Render / Railway

📁 Project Structure
csharp
Copy
Edit
cropRecommendation/
│
├── app.py                  # Flask application
├── model/                  # Trained ML model (.pkl)
├── train_model.py          # Model training script
├── Crop_recommendation.csv# Dataset (if needed)
├── requirements.txt        # Python dependencies
├── static/
│   └── style.css           # Custom CSS
├── templates/
│   └── index.html          # Frontend template
└── vercel.json (optional)
🤝 Contributing
Pull requests are welcome. For major changes, open an issue first to discuss what you’d like to change.
