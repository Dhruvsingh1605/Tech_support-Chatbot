lst = ["create","developed","develop","developing","develops","develops","developing","make","makes","making","made","build","building","builds","built","construct","constructing","constructs","constructed","design","designing","designs","designed"]

from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

genai.configure(api_key="AIzaSyCpbFdCWJ42260oNqASGjbIjpphZu3xJdI")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 150,  
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

chat_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form.get("msg")
    if not user_message:
        return jsonify({"response": "Please provide a message."})
    
    if not chat_history:
        initial_greeting = "Hello, how can I help you?"
        chat_history.append({"role": "model", "parts": [initial_greeting]})
    
    chat_history.append({"role": "user", "parts": [user_message]})
    
    for keyword in lst:
        if keyword.lower() in user_message.lower():
            response_text = ("yes we can surey help you with this, Please provide your Email and Phone Number "
                             "our team will contact you soon.")
            chat_history.append({"role": "model", "parts": [response_text]})
            return jsonify({"response": response_text})
    
    prompt = (
        f"Customer: {user_message}\n"
        "You are a customer support bot for Gfuture Tech Pvt. Ltd, a service-based company specializing in Blockchain and Artificial Intelligence. "
        "Provide a short, precise, and professional response (in one or two sentences) that directly answers the customer query. "
        "Support: "
    )
    
    chat_session = model.start_chat(history=chat_history)
    
    response = chat_session.send_message(prompt)
    model_response = response.text if response.text else "No response generated."
    
    chat_history.append({"role": "model", "parts": [model_response]})
    
    return jsonify({"response": model_response})

if __name__ == "__main__":
    app.run(debug=True)
