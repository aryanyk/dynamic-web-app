import pymysql

connection = pymysql.connect(host="mysql-3dd6389a-pro-98.a.aivencloud.com",
                             port=26794,
                             user="avnadmin",
                             passwd="AVNS_mByd-weDMqNu3TvgDkp",
                             db="defaultdb",
                             cursorclass=pymysql.cursors.DictCursor)

# with connection.cursor() as cursor:
#     cursor.execute("SELECT * FROM JOBS")
#     result = cursor.fetchall()
#     # print(type(result))
#     # print(type(cursor))
#     # print(result)
#     # print(type(result[0]))
# result_dict=[]
# for i in result:
#     result_dict.append(i)
# print(result_dict)

def get_jobs_load():
  
  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM JOBS")
    result = cursor.fetchall()
  result_dict=[]
  for i in result:
    result_dict.append(i)
  return result_dict

def get_jobs(id):
  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM JOBS WHERE id=%s",id)
    result = cursor.fetchall()
  if result is None:
    return None
  else:
    return result[0]