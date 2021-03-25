from flask import Flask, render_template,request
import numpy as np
import pickle

app = Flask(__name__)

filename = 'model/finalized_model.sav'
model = pickle.load(open(filename, 'rb'))

@app.route('/')
def registrarse():
    result={'profit':'',
        'descr':''  }
    return render_template('registrarse.html',result=result)

@app.route("/upload", methods=['GET','POST'])
def uploader():
   if request.method == 'POST':
  # obtenemos el archivo del input "archivo"

      km=request.form['km']
      company=request.form['company']
      city=request.form['city']
      day=request.form['day']
      month=request.form['month']

      print(type(km),type(company),type(city),type(day),type(month))

      int_features = [float(km),int(month),int(day),int(company),int(city)]
      final_features = [np.array(int_features)]
      prediction =model.predict(final_features)

      output = round(prediction[0],2)
      print(output)
      
      result={
      	'profit':output,
        'descr':'The profit should be: $' }
      return render_template('registrarse.html',result=result)


if __name__ == '__main__':
    app.run( port = 5000, debug=False)









