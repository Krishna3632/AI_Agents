from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS  # Enables cross-origin requests
# from phi.agent import Agent
# from phi.model.groq import Groq
# from phi.tools.yfinance import YFinanceTools
# from phi.tools.duckduckgo import DuckDuckGo
# from dotenv import load_dotenv



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True)
