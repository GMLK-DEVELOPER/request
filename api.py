from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)
BASE_DIR = os.getcwd()
@app.route('/files', methods=['GET'])
@app.route('/files/<path:subpath>', methods=['GET'])
def list_files(subpath=""):
    folder_path = os.path.join(BASE_DIR, subpath)
    if not os.path.isdir(folder_path):
        return jsonify({"error": "Diretório não encontrado"}), 404
    files = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            files.append({"name": item, "type": "folder"})
        else:
            files.append({"name": item, "type": "file"})
    return jsonify(files)
@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    file_path = os.path.join(BASE_DIR, filename)
    if not os.path.isfile(file_path):
        return jsonify({"error": "Arquivo não encontrado"}), 404
    return send_from_directory(BASE_DIR, filename, as_attachment=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
