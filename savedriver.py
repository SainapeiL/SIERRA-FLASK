from flask import *
import pymysql


app = Flask(__name__)
app.secret_key = '1@3_S1g5kio00'     

@app.route('/savedriver',methods=['GET','POST'])
def savedriver():
    conn = pymysql.connect(host='localhost',user='root',password='',database='sierra')
    cursor = conn.cursor()

    if request.method == 'POST':
        
        driver_name =request.form['driver_name']
        driver_phone =request.form['driver_phone']
        idnumber =request.form['idnumber']
        car_assigned =request.form['car_assigned']

        sql ='insert into driver(driver_name,driver_phone,idnumber,car_assigned)values(%s,%s,%s,%s)'
        cursor.execute(sql,(driver_name,driver_phone,idnumber,car_assigned))
        conn.commit()
        return render_template('savedriver.html',msg='driver succided')
    else:
        return render_template('savedriver.html')


@app.route('/viewdrivers')
def viewdrivers():
    conn =pymysql.connect(host='localhost',user='root',password='',database='sierra')
    cursor = conn.cursor()

    sql ='select * from driver'
    cursor.execute(sql)

    if cursor.rowcount ==0:
     return render_template('viewdrivers.html',msg='No Drivers available')
    else:
        rows = cursor.fetchall()
        return render_template('viewdrivers.html',rows=rows)

if __name__ == '__main__':
    app.run(debug=True)

