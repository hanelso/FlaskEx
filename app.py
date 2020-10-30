﻿import os           # 파일 핸들링
from flask import Flask
from flask import render_template
from models import db

app = Flask(__name__ )

@app.route('/register')     # app의 main route가 '/'가 된다는 것이다.
def register():
    return render_template("register.html")

@app.route('/')     # app의 main route가 '/'가 된다는 것이다.
def hello():
    return render_template("hello.html")

if __name__=="__main__":
    print("app.py start!")
    # 현재 파일이 실행되는 경로
    basedir = os.path.abspath(os.path.dirname(__file__))        # 절대 경로 ( abspath )로 현재파일( __file__ )의 디렉토리 경로( dirname )를 이용하겠다.
    print( "basedir:{}".format(basedir) )

    # db파일이 저장되는 경로
    dbfile = os.path.join( basedir, "db.sqlite")                # basedir ( /home/hanelso/smb_dir/FlaskEx )에  db.sqlite 를 연결한다. -> /home/hanelso/smb_dir/FlaskEx/db.sqlite
    print("file:{}".format(dbfile))

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True                  # 요청 받은 것에 대해서 응답을 할때를 Teardown 이라고 하는데 이때 commit을 하겠다는 의미
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    db.init_app(app)
    db.app = app
    db.create_all()
    app.run( host="0.0.0.0", port = 5000, debug= True )


