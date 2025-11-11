from flask import Flask, render_template, send_file
import os
import threading
import webbrowser
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download():
    # TU WSTAW ŚCIEŻKĘ DO SWOJEGO PLIKU Z MODEM
    file_path = "linematica_mod.rar"
    try:
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return f"Błąd podczas pobierania: {str(e)}"

def open_browser():
    time.sleep(2)
    webbrowser.open_new('http://localhost:5000')

if __name__ == '__main__':
    print("🦹‍♂️ Serwer Linematica uruchamia się...")
    print("🌐 Strona będzie dostępna pod: http://localhost:5000")
    print("🛑 Aby zatrzymać serwer, naciśnij Ctrl+C")
    
    # Uruchom przeglądarkę automatycznie
    threading.Thread(target=open_browser).start()
    
    # Uruchom serwer z lepszymi ustawieniami
    app.run(
        debug=True, 
        host='127.0.0.1', 
        port=5000, 
        use_reloader=False,
        threaded=True
    )