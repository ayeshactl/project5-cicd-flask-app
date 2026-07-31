from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>🚀 Hello from Project 5 CI/CD Pipeline</h1>
    <p>This application was deployed using Jenkins, Docker, GitHub and AWS EC2.</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
