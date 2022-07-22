import pymysql


def insert():
    conn = pymysql.connect(host='localhost',user='root',password='',database='sierra')
    cursor =conn.cursor()
    mwanzo = 'Mombasa'
    mwisho = 'Athi River'
    date = '22/8/2022'
    time = '18:00'
    amount = 500

    sql = 'insert into bookings(mwanzo,mwisho,date,time,amount)values(%s,%s,%s,%s,%s)'
    cursor.execute(sql,(mwanzo,mwisho,date,time,amount))
    conn.commit()
print('saved successfully')

insert()

def insert():
    conn = pymysql.connect(host='localhost',user='root',password='',database='sierra')
    cursor =conn.cursor()
    first_name = 'Vivian'
    last_name = 'Ndakala'
    dob = '13/9/2002'
    phone = '0700987612'
    gender = 'Female'
    reg_date = '06'

    sql = 'insert into patient(first_name,last_name,dob,phone,gender,reg_date)values(%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql,(first_name,last_name,dob,phone,gender,reg_date))
    conn.commit()
print('patient one')
insert()

def insert():
    conn = pymysql.connect(host='localhost',user='root',password='',database='sierra')
    cursor =conn.cursor()
    first_name ='Jacob'
    last_name ='Lemashon'
    speciality ='Surgeon'
    gender ='Male'
    phone ='0745780634'

    sql = 'insert into doctors (first_name,last_name,speciality,gender,phone)values(%s,%s,%s,%s,%s)'
    cursor.execute(sql,(first_name,last_name,speciality,gender,phone))
    conn.commit()
print('one doctor')
insert()

def insert():
    conn = pymysql.connect(host='localhost',user='root',password='',database='sierra')
    cursor =conn.cursor()
    first_name ='Josphat'
    last_name ='Kibet'
    gender ='Male'
    phone ='0745780634'
    crop = 'Yams'

    sql = 'insert into farmer (first_name,last_name,gender,phone,crop)values(%s,%s,%s,%s,%s)'
    cursor.execute(sql,(first_name,last_name,gender,phone,crop))
    conn.commit()
print('one farmer')
insert()

