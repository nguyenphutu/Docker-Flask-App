from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure database URI (PostgreSQL in this case)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://root:123456@db:5432/dbtest')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Sample model
class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)

def add_sample_data():
    # Kiểm tra xem có dữ liệu mẫu không để tránh thêm trùng lặp
    if Item.query.count() == 0:  # Nếu bảng còn trống
        sample_items = [
            Item(name='Item 1', description='Description for Item 1'),
            Item(name='Item 2', description='Description for Item 2'),
            Item(name='Item 3', description='Description for Item 3'),
            Item(name='Item 3', description='Description for Item 4')
        ]
        db.session.bulk_save_objects(sample_items)  # Thêm nhiều đối tượng
        db.session.commit()  # Lưu thay đổi vào cơ sở dữ liệu
        print("Dữ liệu mẫu đã được thêm vào bảng 'items'.")
    else:
        print("Bảng 'items' đã có dữ liệu.")

# Gọi phương thức để thêm dữ liệu mẫu
with app.app_context():
    db.create_all()  # Tạo bảng nếu chưa tồn tại
    add_sample_data()  # Thêm dữ liệu mẫu

@app.route('/')
def home():
    return jsonify({'message': 'Hello, CI/CD with Jenkins and Docker!'})

# Route to get items
@app.route('/items')
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name} for item in items])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
