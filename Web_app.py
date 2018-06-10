from flask import Flask, render_template, request ,send_file
import pandas as pd
import os
import tablib
app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def Choose_Sort():
	print "Loading CSV file to get column values"
	df = pd.read_csv("Medal_table.csv")
	df =list(df.columns.values)
	print "returning column values to application"
	return render_template('application.html', catagory=df)
		
@app.route("/output",methods=['GET', 'POST'])
def Final():
	print "one option selected"
	select = request.args.get('options')
	print "option selected is "+str(select)
	df = pd.read_csv("Medal_table.csv")
	print "dataframe sorted"
	df = df.sort_values(select)
	df.to_csv('sorted_output.csv')
	dataset = tablib.Dataset()
	with open(os.path.join(os.path.dirname(__file__),'sorted_output.csv')) as f:
		dataset.csv = f.read()
	return dataset.html

@app.route('/get_image')
def get_image():
    if request.args.get('type') == '1':
       filename = 'Medal_graph.jpg'
    else:
       filename = 'Medal_graph.jpg'
    return send_file(filename, mimetype='image/gif')	

if __name__ == "__main__":
    app.run()
