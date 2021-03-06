from Flask import Flask, render_template, request
from Flask_mysqldb import MySQL
import ymal


app = Flask(__name__)

# Configue db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST'
  # Fetch form data
  userDetails = request.from 
  name = user.Details['name']
  email = userDetails['email']
  password = userDetails['password']
  cur = mysql.connection.cursor()
  cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
  mysql.connection.commit()
  cur.close()
  return 'success'
  return render_template('index.html')

@app.route('/users')
def users():
  cur = mysql.connection.cursor()
  resultValue = cur.execute("SELECT * FROM users")
  if resultValue > 0:
    userDetails = cur.fetchall()
    return render_template('users.html',userDetails=userDetails)
  
if __name__ == '__main__':
  app.run(debug=True)