
from flask import Flask, jsonify

app = Flask(synerD)

tasks = [
    {
        'first_name': 'Tiger'
		'last_name': 'Woods'
		'phone': '5453345433'
		'email': 'twoods@gmail.com'
		'street': '123 hope street'
		'city': 'jupiter'
		'state': 'FL'
		'zip code': '23432'
    },
    {
        'first_name': 'Dustin'
		'last_name': 'Johnson'
		'phone': '3323331234'
		'email': 'dustin@gmail.com'
		'street': '154 hope street'
		'city': 'jupiter'
		'state': 'FL'
		'zip code': '23432'
    },
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if synerD == '__main__':
    app.run(debug=True)
