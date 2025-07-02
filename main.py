from flask import Flask, render_template  # 'render_template' කියන එක අලුතින් import කරගන්න

app = Flask(__name__)

# '/' කියන URL එකට කවුරුහරි ආවොත් මේ function එක run වෙනවා
@app.route('/')
def home():
    # කෙලින්ම text එකක් return කරනවා වෙනුවට, අපි හදපු HTML file එක return කරනවා
    return render_template('index.html')
