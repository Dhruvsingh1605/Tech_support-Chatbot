# Gfuture Tech Support Chatbot

This project is a Flask-based customer support chatbot for **Gfuture Tech Pvt. Ltd**, a service-based company specializing in Blockchain and Artificial Intelligence. The chatbot uses Google Generative AI's Gemini-2.0-flash-exp model to generate responses and includes custom logic to detect certain keywords in user input. If a keyword is detected, the chatbot responds with a predefined message asking for the customer's email and phone number.

## Features

- **Flask Backend:** Serves the chatbot UI and handles chat interactions.
- **Google Generative AI Integration:** Uses the Gemini-2.0-flash-exp model for generating concise, professional responses.
- **Keyword Detection:** Checks user input for specific keywords (e.g., "develop", "build", "design") to provide tailored responses.
- **Chat History:** Maintains conversation context to improve response relevance.
- **Responsive UI:** Built with HTML, CSS, and JavaScript for a smooth user experience.

## Requirements

- Python 3.8 or higher
- [Flask](https://flask.palletsprojects.com/)
- [google-generativeai](https://pypi.org/project/google-generativeai/)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
