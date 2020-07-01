from django.shortcuts import render
import pymysql



def index(request):
    if request.method == 'GET':
       return render(request,'index.html', {})
def branche(request):
    if request.method == 'GET':
       return render(request,'branches.html', {})
def ifsc(request):
    if request.method == 'GET':
       return render(request,'index.html', {})
def check(request):
    if request.method == 'POST':
        name = request.POST.get('name', False)
        db_connection = pymysql.connect(host='daggupatimahesh291.mysql.pythonanywhere-services.com',port = 3306,user = 'daggupatimahesh2', password = 'bablumahesh', database = 'daggupatimahesh2$branchdetails',charset='utf8')
        db_cursor = db_connection.cursor()
        sql="select * FROM bank_details where bank_ifsc=%s"
        db_cursor.execute(sql, name)
        myresult = db_cursor.fetchall()
        strdata = '<table border=1 align=center width=100%><tr><th>Bank Id</th><th>Bank Name</th><th>Bank IFSC</th><th>Bank Branch</th><th>Bank Adress</th><th>Bank City</th><th>Bank District</th><th>Bank State</th></th></tr><tr>'
        for row in myresult:
            strdata+='<td>'+str(row[0])+'</td><td>'+row[1]+'</td><td>'+str(row[2])+'</td><td>'+str(row[3])+'</td><td>'+str(row[4])+'</td><td>'+row[5]+'</td><td>'+row[6]+'</td><td>'+row[7]+'</td></tr><tr>'


        context= {'data':strdata}
        return render(request,'index.html', context)

def branch(request):
    if request.method == 'POST':
        name = request.POST.get('bankname', False)
        city =request.POST.get('city', False)
        db_connection = pymysql.connect(host='daggupatimahesh291.mysql.pythonanywhere-services.com',port = 3306,user = 'daggupatimahesh2', password = 'bablumahesh', database = 'daggupatimahesh2$branchdetails',charset='utf8')
        db_cursor = db_connection.cursor()
        sql="select * FROM bank_details where bank_name=%s and bank_city=%s"
        adr=(name,city,)
        db_cursor.execute(sql,adr)
        myresult = db_cursor.fetchall()
        strdata = '<table border=1 align=center width=100%><tr><th>Bank Id</th><th>Bank Name</th><th>Bank IFSC</th><th>Bank Branch</th><th>Bank Adress</th><th>Bank City</th><th>Bank District</th><th>Bank State</th></th></tr><tr>'
        for row in myresult:
            strdata+='<td>'+str(row[0])+'</td><td>'+row[1]+'</td><td>'+str(row[2])+'</td><td>'+str(row[3])+'</td><td>'+str(row[4])+'</td><td>'+row[5]+'</td><td>'+row[6]+'</td><td>'+row[7]+'</td></tr><tr>'


        context= {'data':strdata}
        return render(request,'branches.html', context)
    return render(request,'branches.html', {})

