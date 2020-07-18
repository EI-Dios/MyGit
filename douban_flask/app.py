from flask import Flask,render_template
import  sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def home():
    #return render_template('index.html')
    return index()


@app.route('/movie')
def movie():
    datalist = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template('movie.html',movies = datalist)


@app.route('/score')
def score():
    score = []
    num = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score "
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        num.append(item[1])
    cur.close()
    con.close()
    return render_template('score.html',score = score,num = num)


@app.route('/word')
def word():
    return render_template('word.html')


@app.route('/image')
def image():
    datalist = []
    num = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select pic_link from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item[0])
    for i in range(250):
        a = datalist[i][60:-4]
        num.append(a)
    cur.close()
    con.close()
    return render_template('image.html',num = num)

if __name__ == '__main__':
    app.run()
