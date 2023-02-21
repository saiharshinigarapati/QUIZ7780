
#https://harshini7780quiz2.azurewebsites.net/
#GARAPATI SAI HARSHINI
#1002027780
from flask import Flask, render_template, request
import pyodbc

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/q1',methods=["POST","GET"])
def q1():
    if(request.method=="POST"):
       mags=float(request.form['small'])
       magr=float(request.form['large'])
       count1=request.form['count']
       cnxn=pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:harshinibigdata.database.windows.net,1433;Database=harshini;Uid=harshini7780;Pwd=MADHUbala.123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
       cursor=cnxn.cursor()
       query="select Population,City,State from dataquiz2 where Population >= ? and Population <= ? "
       parameters=(mags,magr)
       results=cursor.execute(query,parameters)
       rows=cursor.fetchall()
       results=[]
       for r in rows:
        results.append(r)
       result=sorted(results)
       print(result)
       l=[]
       l.append(result[:int(count1)])
       print(l)
       p=result[::-1]
       l.append(p[:int(count1)]) 
       print(l)
       return render_template("q11.html",results=l)
    else:
        return render_template("q1.html")

@app.route('/q2',methods=["POST","GET"])
def q2():
    if(request.method=="POST"):
        min_lat=request.form['ml']
        min_lon=request.form['mlo']
        max_lat=request.form['max_lat']
        max_lon=request.form['max_lo']
        cnxn=pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:harshinibigdata.database.windows.net,1433;Database=harshini;Uid=harshini7780;Pwd=MADHUbala.123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
        cursor=cnxn.cursor()
        query="select * from dataquiz2 where  lat >= ? and lat <= ? and lon >= ? and lon <=?"
        parameters=(min_lat,max_lat,min_lon,max_lat)
        results=cursor.execute(query,parameters)
        rows=cursor.fetchall()
        results=[]
        for r in rows:
            results.append(r)
        return render_template("q22.html",results=results)
    else:
        return render_template("q2.html")

    
@app.route('/q3',methods=["POST","GET"])
def q3():
    if request.method=="POST":
        nc=request.form["nc"]
        mag1=request.form['mag1']
        mag2=request.form['mag2']
        value=request.form["value"]
        cnxn=pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:harshinibigdata.database.windows.net,1433;Database=harshini;Uid=harshini7780;Pwd=MADHUbala.123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
        cursor=cnxn.cursor()
        query="update dataquiz2 set Population = Population+ ? where State=? and Population >= ? and Population <= ? "
        parameters=(value,nc,mag1,mag2)
        cursor.execute(query,parameters)
        query1="select State,City,Population from dataquiz2 where State=? and Population >= ? and Population <= ? order by Population"
        parameters=(nc,mag1,mag2)
        cursor.execute(query1,parameters)
        row1=cursor.fetchall()
        a=len(row1)
        results=[]
        for r in row1:
            results.append(r)
        a=tuple([len(row1),0,0])    
        results.append(a)
        print(results)
        return render_template("q33.html",results=results)
    else:
        return render_template("q3.html")
#need to do    
@app.route('/q4',methods=["POST","GET"])
def q4():
    if request.method=="POST":
        state=request.form["state"]
        city=request.form["city"]
        pop=request.form["pop"]
        lat=request.form["lat"]
        lon=request.form["lon"]
        cnxn=pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:harshinibigdata.database.windows.net,1433;Database=harshini;Uid=harshini7780;Pwd=MADHUbala.123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
        cursor=cnxn.cursor()
        query=" insert into dataquiz2 (State,City,Population,lat,lon) values (?,?,?,?,?)"
        parameters=(state,city,pop,lat,lon)
        cursor.execute(query,parameters)
        query1="select * from dataquiz2 "
        cursor.execute(query1)
        row1=cursor.fetchall()
        results=[]
       
        for r in row1:
            results.append(r)
        return render_template("q44.html",results=results)
    else:
        return render_template("q4.html")
@app.route('/q5',methods=["POST","GET"])
def q5():
    if request.method=="POST":
        state=request.form["state"]
        city=request.form["city"]
        cnxn=pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:harshinibigdata.database.windows.net,1433;Database=harshini;Uid=harshini7780;Pwd=MADHUbala.123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
        cursor=cnxn.cursor()
        query=" delete from dataquiz2 where State= ? and City = ?"
        parameters=(state,city)
        cursor.execute(query,parameters)
        query1="select * from dataquiz2 "
        cursor.execute(query1)
        row1=cursor.fetchall()
        results=[]
       
        for r in row1:
            results.append(r)
        return render_template("q55.html",results=results)
    else:
        return render_template("q5.html")
    



if __name__ == '__main__':
    app.run(debug=True)
