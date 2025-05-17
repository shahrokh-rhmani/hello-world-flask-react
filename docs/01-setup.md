<p dir="rtl" align="justify">ساختار پروژه</p>

```
hello-world-app/
├── backend/          # بخش Flask
│   ├── venv/         # محیط مجازی
│   ├── app.py
│   └── requirements.txt
├── frontend/         # بخش React
│   ├── src/
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   └── ...
├── .gitignore
└── README.md
```

# <p dir="rtl" align="justify">بخش ۱: راه‌اندازی بک‌اند با Flask</p>

<p dir="rtl" align="justify">1. ابتدا پوشه پروژه و بخش بک‌اند را ایجاد کنید:</p>

```
mkdir -p hello-world-app/backend
cd hello-world-app/backend
```

<p dir="rtl" align="justify">2. محیط مجازی ایجاد و فعال کنید:</p>

```
# برای ویندوز:
python -m venv venv
venv\Scripts\activate

# برای مک/لینوکس:
python3 -m venv venv
source venv/bin/activate
```

<p dir="rtl" align="justify">3. Flask و نسخه‌های سازگار را نصب کنید:</p>

```
pip install flask==2.0.1 werkzeug==2.0.1 flask-cors==3.0.10
```

<p dir="rtl" align="justify">4. نیازمندی‌ها را در فایل ذخیره کنید:</p>

```
pip freeze > requirements.txt
```

<p dir="rtl" align="justify">5. فایل app.py را ایجاد کنید:</p>

```python
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # این خط برای اجازه ارتباط بین React و Flask لازم است

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({
        'message': 'Hello from Flask!',
        'status': 'success',
        'framework': 'Flask',
        'version': '2.0.1'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

# <p dir="rtl" align="justify">بخش ۲: راه‌اندازی فرانت‌اند با React</p>

```
cd ..
npx create-react-app frontend
cd frontend
```

<p dir="rtl" align="justify">1. فایل src/App.js را به صورت زیر ویرایش کنید:</p>

```javascript
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000/api/hello')
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Hello World App</h1>
        <p>Message from Flask backend: {message}</p>
      </header>
    </div>
  );
}

export default App;
```

<p dir="rtl" align="justify">2. فایل src/App.css را بهبود دهید:</p>

```css
.App {
  text-align: center;
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}
```

# <p dir="rtl" align="justify">بخش ۳: اجرای پروژه</p>

<p dir="rtl" align="justify">1. در یک ترمینال، بک‌اند را اجرا کنید (ابتدا محیط مجازی را فعال کنید):</p>

```
cd backend
venv\Scripts\activate  # ویندوز
# یا source venv/bin/activate برای مک/لینوکس
python app.py
```

<p dir="rtl" align="justify">2. در ترمینال دیگری، فرانت‌اند را اجرا کنید:</p>

```
cd frontend
npm start
```





