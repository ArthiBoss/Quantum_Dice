

from flask_socketio import SocketIO, emit
from flask import Flask, request, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event
import numpy as np
from qiskit import *



app = Flask(__name__)
app.config['SECRET_KEY'] = '8675309'
app.config['DEBUG'] = True
socketio = SocketIO(app)

thread = Thread(daemon=True)
thread_stop_event = Event()


class MessageThread(Thread):
	'''
	MessageThread class to allow SocketIO RESTful operations within the app.
	'''
	def __init__(self):
		self.delay = 1
		super(MessageThread, self).__init__()

	def gameEngine(self):
		'''
		Game engine comprising the dice number choice logic with the IBM
		quantum computer.
		'''
		try:
			

			message = 'Creating circuit of three quantum registers and three classical registers.'
			socketio.emit('newmessage', {'message': message}, namespace='/temp')
			sleep(self.delay)
			# Create a circuit with 1000 shots with 2 quantum regs and 2 classic regs.
			shots = 1000
			qr = QuantumRegister(3)
			cr = ClassicalRegister(3)
			circuit = QuantumCircuit(qr, cr)

			message = 'Initializing quantum states of Dice'
			socketio.emit('newmessage', {'message': message}, namespace='/temp')
			sleep(self.delay)
			circuit.h(qr[0])
			circuit.h(qr[1])
			circuit.h(qr[2])
		
			# Create superposition.
			#circuit.h(qr[0])
			
		
			# Create entanglement.
			#circuit.cx(qr[0], qr[1])

			message = 'Measuing qubits and irrevocably disturbing the superposition state.'
			socketio.emit('newmessage', {'message': message}, namespace='/temp')
			sleep(self.delay)
			# Measure circuit.
			circuit.measure(qr, cr)
			
			
			try:
				# Load IBMQ account.

				IBMQ.load_account()
			except:
				# Handle if account is not setup to help the user gain access to 
				# the IBM Q Experience.
				message = 'Please ensure you have your IBM Q Experience account setup properly.  Visit https://github.com/mytechnotalent/qapp for details of how to properly setup your IBM Q Experience account.'
				socketio.emit('newmessage', {'message': message}, namespace='/temp')
				sleep(self.delay)
				temp_disconnect()
			# Look for the least busy quantum computer with the fewest number of queues.
			from qiskit.providers.ibmq import least_busy
			provider = IBMQ.get_provider(hub='ibm-q')
			IBMQ.get_provider(project='main')
			least_busy_device = provider.backends(filters=lambda x: x.configuration().n_qubits >= 5 
												  and not x.configuration().simulator)
			backend = least_busy(least_busy_device)
			backend_name = backend.name()
			backend_new_name = provider.get_backend(backend_name)
			
			message = 'Executing application on the REAL IBMQ {} quantum computer!'.format(backend_new_name)
			socketio.emit('newmessage', {'message': message}, namespace='/temp')
			sleep(self.delay)
			# Execute job on our quantum computer and store the results in new
			
			job = execute(circuit, shots=shots, backend=backend_new_name)
			from qiskit.tools.monitor import job_monitor
			job_monitor(job)
			result = job.result()
			counts = result.get_counts(circuit)
			zero = int(counts['000'])
			one = int(counts['001'])
			two = int(counts['010'])  
			three = int(counts['011'])  
			four = int(counts['100'])  
			five = int(counts['101'])  
			six = int(counts['110'])  
			twelve = int(counts['111'])  			
		
			# In order to print out our variables we need to cast them to a string.
			str_zero = str(zero)
			str_one = str(one)
			str_two = str(two)
			str_three = str(three)
			str_four = str(four)
			str_five = str(five)
			str_six = str(six)
			str_twelve = str(twelve)
			
			try:
				message = 'Your Choice: ' + choice
				socketio.emit('newmessage', {'message': message}, namespace='/temp')
				sleep(self.delay)
			except NameError:
				pass

			message = 'Zero has {} counts out of 1000 shots.'.format(str_zero)
			socketio.emit('newmessage', {'message': message}, namespace='/temp')
			message = 'One has {} counts out of 1000 shots.'.format(str_one)
			socketio.emit('newmessage', {'message': message}, namespace='/temp')
			message = 'Two has {} counts out of 1000 shots.'.format(str_two)
			socketio.emit('newmessage', {'message': message}, namespace='/temp')
			message = 'Three has {} counts out of 1000 shots.'.format(str_three)
			socketio.emit('newmessage', {'message': message}, namespace='/temp')
			message = 'Four has {} counts out of 1000 shots.'.format(str_four)
			socketio.emit('newmessage', {'message': message}, namespace='/temp')
			message = 'Five has {} counts out of 1000 shots.'.format(str_five)
			socketio.emit('newmessage', {'message': message}, namespace='/temp')
			message = 'Six has {} counts out of 1000 shots.'.format(str_six)
			socketio.emit('newmessage', {'message': message}, namespace='/temp')
			message = 'Twelve has {} counts out of 1000 shots.'.format(str_twelve)
			socketio.emit('newmessage', {'message': message}, namespace='/temp')
			
			sleep(self.delay)
			# Logic to determine outcome of the game and present to the results
			# to the user.
			if choice == 'zero' and zero > one and zero > two and zero > three and zero > four and zero > five and zero > six and zero > twelve :
				message = 'YOU WON!'
				socketio.emit('newmessage', {'message': message}, namespace='/temp')
				sleep(self.delay)
			elif choice == 'one' and one > zero and one > two and one > three and one > four and one > five and one > six and one > twelve :
				message = 'YOU WON!'
				socketio.emit('newmessage', {'message': message}, namespace='/temp')
				sleep(self.delay)
			elif choice == 'two' and two > zero and two > one and two > three and two > four and two > five and two > six and two > twelve:
				message = 'YOU WON!'
				socketio.emit('newmessage', {'message': message}, namespace='/temp')
				sleep(self.delay)
			elif choice == 'three' and three > zero and three > one and three > two and two > four and three > five and three > six and three > twelve:
				message = 'YOU WON!'
				socketio.emit('newmessage', {'message': message}, namespace='/temp')
				sleep(self.delay)
			elif choice == 'four' and four > zero and four > one and four > two and four > three and four > five and four > six and four > twelve:
				message = 'YOU WON!'
				socketio.emit('newmessage', {'message': message}, namespace='/temp')
				sleep(self.delay)
			elif choice == 'five' and five > zero and five > one and five > two and five > four and five > three and five > six and five > twelve:
				message = 'YOU WON!'
				socketio.emit('newmessage', {'message': message}, namespace='/temp')
				sleep(self.delay)
			elif choice == 'six' and six > zero and six > one and six > two and six > four and six > five and six > three and six > twelve:
				message = 'YOU WON!'
				socketio.emit('newmessage', {'message': message}, namespace='/temp')
				sleep(self.delay)
			elif choice == 'twelve' and twelve > zero and twelve > one and twelve > two and twelve > four and twelve > five and twelve > six and twelve > three:
				message = 'YOU WON!'
				socketio.emit('newmessage', {'message': message}, namespace='/temp')
				sleep(self.delay)
			else:
				message = 'YOU LOST!'
				socketio.emit('newmessage', {'message': message}, namespace='/temp')
				sleep(self.delay)
			

			temp_disconnect()
		
		except:
			temp_disconnect()

	def run(self):
		self.gameEngine()


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		global choice
		choice = request.form.get('choice')

		return render_template('index.html', choice=choice)   

	return render_template('index0.html')



@socketio.on('connect', namespace='/temp')
def temp_connect():
	global thread
	print('Client Connected...')

	if not thread.isAlive():
		print("Starting Thread...")
		thread = MessageThread()
		thread.start()

@socketio.on('disconnect', namespace='/temp')
def temp_disconnect():
	print('Client Disconnected...')
	print("Stopping Thread...")


if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0')
