📄 Final Report: GPT-2 Text Generator Flask Application
 Project Title:
GPT-2 Text Generator using Flask & Hugging Face (Local Inference)

 Objective:
To build a lightweight web application using Flask that utilizes the GPT-2 language model (from Hugging Face) for generating AI-powered text completions locally without OpenAI API.

 Technologies Used:
Technology	Purpose
Python	Programming language
Flask	Backend web framework
Transformers	Hugging Face GPT-2 model
HTML/CSS/JS	Frontend user interface
Vercel	Hosting/Deployment
dotenv	Environment variable handling

🧰 Installation & Setup:
Clone the Repository



git clone https://github.com/your-username/gpt2-flask-app.git
cd gpt2-flask-app


Create a Virtual Environment
python -m venv .venv
.venv\Scripts\activate


Install Dependencies
pip install -r requirements.txt

Run the App
python app.py

 Project Structure:
llm_flask_app/
│
├── app.py              # Main Flask app
├── llm_wrapper.py      # Text generation logic using GPT2
├── templates/
│   └── index.html      # Frontend interface
├── static/
│   └── style.css       # Styling (optional)
├── .env                # For environment variables
├── requirements.txt    # All required libraries
└── vercel.json         # For deployment on Vercel


 Sample Request/Response
Request:
POST /generate
{
  "prompt": "Importance of AI in education"
}
Response:


{
  "response": "IMPORTANCE OF AI IN EDUCATION.

There are no studies that have been done to demonstrate the existence of a "hard core" of early humans, or the existence of "hard core" humans. In fact, a few studies have suggested a very small number of early humans may have been genetically predisposed to be resistant to certain diseases. There is no evidence to support this hypothesis.

However, we do know that some early humans may have had some kind of genetic predisposition to be resistant to certain diseases."
}

<img width="658" height="606" alt="image" src="https://github.com/user-attachments/assets/ca94523b-1af6-4c38-8307-e7ed5dfecc9b" />

🌐 Deployment
Platform: Vercel
vercel.json:
{
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
🧪 Output Example:
User Prompt:


Write a short paragraph on importance of Flask.
Generated Result:


Flask is a lightweight web framework in Python used for building web applications quickly and with minimal code. It is widely used due to its flexibility, simplicity, and strong community support.



✅ Conclusion
This project successfully demonstrates how to use GPT-2 locally via Hugging Face Transformers in a simple Flask web application. It eliminates the need for paid API keys, and shows how LLMs can be integrated into lightweight, deployable apps using only Python and open-source tools.
