import os

# Define the project structure
project_name = "Flask-Portfolio"
folders = [
    f"{project_name}/static",
    f"{project_name}/templates"
]
files = {
    f"{project_name}/app.py": """\
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
""",
    f"{project_name}/requirements.txt": "flask",
    f"{project_name}/README.md": "# Flask Portfolio\nA simple Flask-based portfolio website.",
    f"{project_name}/templates/index.html": """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio - Home</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <h1>Welcome to My Portfolio</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/projects">Projects</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>
    <section>
        <p>Hello! I'm a developer passionate about building impactful projects.</p>
    </section>
</body>
</html>
""",
    f"{project_name}/templates/projects.html": """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projects</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <h1>My Projects</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/projects">Projects</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>
    <section>
        <h2>Project List</h2>
        <ul>
            <li>Face Recognition Voting System</li>
            <li>Crop Yield Prediction</li>
            <li>Optimizing Crop Recommendations using ML</li>
        </ul>
    </section>
</body>
</html>
""",
    f"{project_name}/templates/contact.html": """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <h1>Contact Me</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/projects">Projects</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>
    <section>
        <h2>Let's Connect</h2>
        <p>Email: <a href="mailto:shmohammadarshadali@gmail.com">shmohammadarshadali@gmail.com</a></p>
        <p>GitHub: <a href="https://github.com/arshad1401" target="_blank">arshad1401</a></p>
        <p>LinkedIn: <a href="https://www.linkedin.com/in/shaik-mohammadarshadali-834a75342" target="_blank">Shaik Mohammad Arshad Ali</a></p>
    </section>
</body>
</html>
""",
    f"{project_name}/static/styles.css": """\
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    text-align: center;
    background-color: #f4f4f4;
}
header {
    background-color: #333;
    color: white;
    padding: 1em;
}
nav a {
    color: white;
    text-decoration: none;
    margin: 0 15px;
}
section {
    margin: 20px;
    padding: 20px;
    background: white;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}
"""
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files and write content
for file_path, content in files.items():
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ Flask portfolio project '{project_name}' has been set up successfully!")
