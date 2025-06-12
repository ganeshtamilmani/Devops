from flash import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello from Bitbucker CI/CD"
if __name__ == '__main__':
    app.run(debub=True)