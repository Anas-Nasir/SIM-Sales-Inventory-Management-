from flask import Flask, redirect, render_template,request,redirect
import psycopg2

app = Flask(__name__)

#conn=psycopg2.connect(user="postgres",password="Penina505",
#076'/'''yhost="127.0.0.1",port="5432",database="myduka")
conn=psycopg2.connect(user="yergcplseszdqg",password="3ad258c09f03132ec7565c65f82d5cadc9c47c2908c60db1037580b3ae983208",
host="ec2-52-208-164-5.eu-west-1.compute.amazonaws.com",port="5432",database="dblscdfvr346if")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS products (id serial PRIMARY KEY,name VARCHAR(100),buying_price INT,selling_price INT,stock_quantity INT);")
cur.execute("CREATE TABLE IF NOT EXISTS sales (id serial PRIMARY KEY,pid INT, quantity INT, created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(), FOREIGN KEY(pid) REFERENCES products(id) ON DELETE CASCADE);")
conn.commit()

@app.route("/dashboard")
def dashboard():
    cur.execute("""select sum((products.selling_price-products.buying_price)*sales.quantity) 
    as profit, products.name from sales 
    join products on products.id=sales.pid
    GROUP BY products.name""")
    graph=cur.fetchall()
    print(graph)
    products_names=[]
    profits=[]
    for tpl in graph:
        products_names.append(tpl[1])
    print(products_names)
    for tpl in graph:
        profits.append(tpl[0])
    print(profits)
   
    return render_template("dashboard.html", products_name=products_names, profits=profits)  
    

def home():
    hello = "hello BRO"
    return render_template("index.html",h=hello)

    cur.execute("SELECT * from sales")
    sales=cur.fetchall()
    print(sales)
    return render_template("sales.html",sales=sales)  


@app.route("/form_true",methods = ['POST','GET'])
def form():
    if request.method == 'GET':
        return render_template("form.html")
    else:
        first_name = request.form['fname']
        last_name = request.form['lname'] 
        print(first_name) 
        print(last_name) 
        return redirect("/form_true") 

@app.route("/products",methods = ['POST','GET'])
def form_data():
    if request.method == 'GET':
        cur.execute("SELECT * from products")
        products = cur.fetchall()
        
        return render_template("products.html",products=products)
    else:
        
        name = request.form['name']
        buying_price = request.form['bprice'] 
        selling_price = request.form['sprice']
        stock_quantity = request.form['qt']
         
        print(name) 
        print(buying_price)
        print(selling_price)
        print(stock_quantity) 
        cur.execute("""INSERT INTO products (name,buying_price,selling_price,stock_quantity)
         VALUES(%(n)s,%(bp)s,%(sp)s,%(st)s)""",{"n":name,"bp":buying_price,"sp":selling_price,"st":stock_quantity})
        conn.commit()
        return redirect("/products") 


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sales",methods=['POST','GET'])
def sales():
    if request.method=='POST':
        quantity=request.form['quantity']
        pid=request.form['pid']
        cur.execute("INSERT INTO sales (pid,quantity) VALUES(%s,%s)",(pid,quantity))
        conn.commit()
        return redirect("/products")
    else:
        cur.execute("SELECT * from sales")
        sales=cur.fetchall()
        print(sales)
        return render_template("sales.html",sales=sales)

@app.route("/sales/<int:id>")
def sale(id):
    x=id
    cur.execute("""SELECT * FROM sales WHERE pid=%(id)s""",{"id":x})   
    sales=cur.fetchall()
    print(sales)
    return render_template("sales.html",sales=sales)         
            
if __name__ == "__main__":    
    app.run()
