import random, datetime
from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'ososecret'

def score():
	if 'score' not in session:
		session['score'] = 0
	

@app.route('/')
def index():
	score()
	return render_template('index.html')

@app.route('/process_money', methods= ['POST'])
def findgold():
	print 'you found gold'
	date = datetime.datetime.now().strftime('date %y/%m/%d time %H:%M:%S')
	if 'act' not in session:
		session['act']= []

	if request.form['action'] == 'farm':
		session['gold']= random.randrange(10,21)
		session['score']+=session['gold']
		session['act'].insert(0, 'You harvest: ' + str(session['gold']) +' gold with your Farm ( '+str(date)+').')
	elif request.form['action'] == 'cave':
		session['gold']= random.randrange(5,11)
		session['score']+=session['gold']
		session['act'].insert(0,'You found: ' + str(session['gold']) +' gold in the Cave( '+str(date)+').' )
	elif request.form['action'] == 'house':
		session['gold']= random.randrange(1,6)
		session['score']+=session['gold']
		session['act'].insert(0,'You robbed : ' + str(session['gold']) +' gold from a House( '+str(date)+').')
	elif request.form['action'] == 'casino':
		session['gold']= random.randrange(-51,50)
		session['score']+=session['gold']
		if session['gold'] < 0:
			session['act'].insert(0,'You Lost : ' + str(abs(session['gold'])) +' gold at the Casino. Try again( '+str(date)+').')
		else:
			session['act'].insert(0,'You Won : ' + str(session['gold']) +' gold at the Casino. Go NINJA( '+str(date)+').')
		
	return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
	session.clear()
	return redirect('/')

app.run(debug = True)
 