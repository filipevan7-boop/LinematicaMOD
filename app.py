from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download():
    file_path = "linematica_mod.zip"
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name="Linematica_Mod.rar")
    else:
        return """
        <html>
            <body style="background: black; color: white; text-align: center; padding: 50px; font-family: Arial;">
                <h1>📦 Linematica Mod</h1>
                <p>Plik z modem będzie dostępny wkrótce!</p>
                <a href="/" style="color: #4CAF50;">← Powrót do strony głównej</a>
            </body>
        </html>
        """

# Ważne dla Render.com - użyj portu z zmiennej środowiskowej
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
