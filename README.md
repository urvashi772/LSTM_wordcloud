**📄 PDF → WordCloud Generator (Streamlit App)**

A fast and interactive Streamlit web application that generates a custom-shaped WordCloud from any PDF document, using a mask image (e.g., India map, heart, logo, etc.).

🚀 No model training – instant results
🎨 Custom shapes using mask images
📄 Any PDF supported

**✨ Features**

📂 Upload any PDF file

🖼️ Upload any mask image (PNG / JPG)

🎨 Generate WordCloud in custom shapes

⚡ Very fast (no ML model training)

🧠 Automatic mask correction & inversion

🌐 Easy-to-use Streamlit UI

**🖥️ Demo Workflow**

Upload a PDF document

Upload a mask image (black shape on white background)

Click Generate WordCloud

View the WordCloud instantly 🎉

**📁 Project Structure**
project/
│── app.py              # Streamlit application
│── requirements.txt    # Required Python libraries
│── README.md           # Project documentation
│── sample_masks/       # (Optional) mask images

**⚙️ Installation**

1️⃣ Clone the repository
git clone https://github.com/urvashi772/LSTM_wordcloud
cd pdf-wordcloud-app

2️⃣ Install dependencies
pip install -r requirements.txt

▶️ Run the Application
streamlit run app.py


The app will open automatically in your browser 🌐

**🖼️ Mask Image Guidelines (Very Important)**

For best results, the mask image should follow these rules:

Requirement	Description
Shape color	Black
Background	White
Format	PNG / JPG
Size	500×500 or larger

✔ Example shapes:

🇮🇳 India map

❤️ Heart

⭐ Star

🧠 Brain

🏷️ Logo

**🧠 How It Works**

Extracts text from the uploaded PDF

Cleans and normalizes the text

Loads and auto-corrects the mask image

Generates a WordCloud constrained to the mask shape

Displays the result instantly

⚡ Model training is intentionally excluded to ensure fast performance.

**🧪 Technologies Used**

Python

Streamlit

WordCloud

PyPDF2

Pillow (PIL)

NumPy

Matplotlib

**🎓 Viva / Interview Explanation**

“This project generates a masked WordCloud directly from PDF text using Streamlit. To ensure fast user interaction, no machine learning model is used during runtime. Custom shapes are applied using binary mask images.”

**🔮 Future Enhancements**

💾 Download WordCloud as image

🎨 Color theme selector

🛑 Stopword removal toggle

🇮🇳 Default India map option

📊 Word frequency table
