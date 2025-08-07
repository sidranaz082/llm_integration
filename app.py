from flask import Flask, request, jsonify, render_template
from llm_wrapper import generate_response  # Import from your wrapper

app = Flask(__name__)

# Home route (HTML form)
@app.route('/')
def index():
    return render_template('index.html')  # Must have templates/index.html

# API route
@app.route('/generate', methods=['POST'])
def generate():
    # Handle JSON (Postman) and Form (Browser)
    if request.is_json:
        data = request.get_json()
        prompt = data.get("prompt")
    else:
        prompt = request.form.get("prompt")

    # Validate prompt
    if not prompt:
        if request.is_json:
            return jsonify({"success": False, "error": "Prompt is required"}), 400
        return render_template('index.html', result="Prompt is required")

    # Call the wrapper
    result = generate_response(prompt)

    # JSON response (Postman)
    if request.is_json:
        return jsonify(result)

    # HTML response (Browser)
    if result["success"]:
        return render_template('index.html', result=result["response"])
    else:
        return render_template('index.html', result=f"Error: {result['error']}")

if __name__ == '__main__':
    app.run(debug=True)
