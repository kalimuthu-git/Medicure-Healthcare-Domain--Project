from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

doctors = [
    {"id": 1, "name": "Dr. Sarah Johnson", "specialty": "Cardiologist", "experience": "15 years", "image": "doctor1.jpg"},
    {"id": 2, "name": "Dr. Michael Chen", "specialty": "Neurologist", "experience": "12 years", "image": "doctor2.jpg"},
    {"id": 3, "name": "Dr. Emily Davis", "specialty": "Pediatrician", "experience": "10 years", "image": "doctor3.jpg"},
    {"id": 4, "name": "Dr. Robert Wilson", "specialty": "Orthopedic", "experience": "18 years", "image": "doctor4.jpg"},
]
departments = [
    {"name": "Cardiology", "icon": "❤️", "description": "Heart & cardiovascular care"},
    {"name": "Neurology", "icon": "🧠", "description": "Brain & nervous system"},
    {"name": "Pediatrics", "icon": "👶", "description": "Child healthcare specialists"},
    {"name": "Orthopedics", "icon": "🦴", "description": "Bone & joint treatment"},
    {"name": "Oncology", "icon": "🔬", "description": "Cancer diagnosis & treatment"},
    {"name": "Emergency", "icon": "🚑", "description": "24/7 emergency services"},
]

@app.route('/')
def home():
    return render_template('index.html', doctors=doctors, departments=departments)

@app.route('/about')
def about():
    return render_template('index.html', section='about', doctors=doctors, departments=departments)

@app.route('/doctors')
def get_doctors():
    return jsonify(doctors)

@app.route('/departments')
def get_departments():
    return jsonify(departments)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    # In real project, save to DB or send email
    return jsonify({"status": "success", "message": f"Thank you {data.get('name')}, we will contact you soon!"})

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "service": "Medicure Healthcare", "version": "1.0.0"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
