from flask import Flask, request, jsonify, render_template
from google import genai

client = genai.Client(api_key="AIzaSyA17TrPeEbaRqOaRXib4eLhwVL2GVT7yOc")
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.json.get("message")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return jsonify({"reply": response.text})

app.run(port=5000)