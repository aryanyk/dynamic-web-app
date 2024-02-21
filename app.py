from flask import Flask, jsonify, render_template, request

from database import get_jobs, get_jobs_load,application_to_db

app=Flask(__name__)

# Prog_Lang=[{'Lang':'Java',
#             'Experience':'Intermediate'},
#            {'Lang':'Python',
#             'Experience':'Advanced'},
#            {'Lang':'C',
#             'Experience':'Intermediate'},
#            {'Lang':'JS',
#             'Experience':'Begineer'},
#            {'Lang':'CSS',
#             'Experience':'Intermediate'},
#            {'Lang':'HTML',
#             'Experience':'Expert'},
#            {'Lang':'SQL',
#              'Experience':'Begineer'}
            
#           ]





@app.route("/")
def hello():
  JOBS=get_jobs_load()
  return render_template('index.html',Lang=JOBS)
  # here job is the variable used in template and JOBS is variable passed by main app
  # ,Lang=Prog_Lang


@app.route("/api/job")
def list_lang():
  JOBS=get_jobs_load()
  return jsonify(JOBS)

# <id> for dynamic input and dynamic link
@app.route("/job/<id>") 
def show_job(id):
  job=get_jobs(id)
  # return jsonify(job)
  if not job:
    return "Not Found",404
  return render_template('job.html',job=job)
  
@app.route("/job/<id>/apply",methods=['post'])
def job_apply(id):
  data=request.form  #args when data is in url
  # return jsonify(data)
  application_to_db(id,data)
  return render_template('submission.html',application=data)
  

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)