from flask import Flask,render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
@app.route('/retrieve',methods=['POST','GET'])
def retrieve():
    if request.method=='POST':
        quantity=request.form['quantity']
        con=sql.connect("user_db.db")
        con.row_factory=sql.Row
        cur=con.cursor()
        cur.execute("select * from product_table where quantity<=?",[quantity])
        data=cur.fetchall()
        return render_template('retrieve.html',datas=data)
    return render_template('retrieve.html')

if __name__ =='__main__':
    app.secret_key='admin123'
    app.run(debug=True)
