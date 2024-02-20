from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime, timedelta
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

items = {}

# Function to check if the file has an allowed extension
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def store_item():
    if 'image' not in request.files:
        return jsonify({'message': 'No file part'})
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'message': 'No selected file'})
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        item_name = request.form.get('itemName')
        items[item_name] = datetime.now()
        return jsonify({'message': 'Item stored successfully'})
    else:
        return jsonify({'message': 'Invalid file format'})

@app.route('/recommend')
def recommend_item():
    today = datetime.now()
    recommendation = []
    for item, last_used in items.items():
        time_diff = today - last_used
        if time_diff.days >= 5:
            recommendation.append(item)
    if recommendation:
        return jsonify({'message': ', '.join(recommendation)})
    else:
        return jsonify({'message': 'No recommended items'})

if __name__ == '__main__':
    app.run(debug=True)
