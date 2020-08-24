from flask import Flask , render_template ,url_for,request,redirect
import csv

app = Flask(__name__)



@app.route('/')
def my_home():

	return render_template('index.html')




@app.route('/components.html')
def component():
	return render_template('components.html')


@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)


def write_to_csv(data):
	with open("databases.csv" , mode = 'a') as dataget:
		email = data['email']
		subject = data['subject']
		message = data['message']
		cv_writer = csv.writer(dataget , delimiter = ',', quotechar = '|',quoting = csv.QUOTE_MINIMAL)
		cv_writer.writerow([email , subject , message])

	    
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
			data = request.form.to_dict()
			write_to_csv(data)
			return "form submitted.....!"
		    
		    
		

		  
	else:
		return 'something went wrong..Try again!!!'