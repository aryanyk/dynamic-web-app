from flask import Flask,render_template,request,redirect,url_for,flash,session,jsonify

app=Flask(__name__)

Prog_Lang=[{'Lang':'Java',
            'Experience':'Intermediate'},
           {'Lang':'Python',
            'Experience':'Advanced'},
           {'Lang':'C',
            'Experience':'Intermediate'},
           {'Lang':'JS',
            'Experience':'Begineer'},
           {'Lang':'CSS',
            'Experience':'Intermediate'},
           {'Lang':'HTML',
            'Experience':'Expert'},
           {'Lang':'SQL',
             'Experience':'Begineer'}
            
          ]
@app.route("/")
def hello():
  return render_template('index.html',Lang=Prog_Lang)


@app.route("/api/job")
def list_lang():
  return jsonify(Prog_Lang)
  


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)