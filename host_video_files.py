from flask import Flask, render_template
from glob import glob
from random import randint

app=Flask(__name__,static_url_path='',template_folder='static',static_folder='.')

@app.route('/')
def loadMasterPage():
    files=glob("*.mp4")
    print(files)
    return render_template('index.html',files=files)


if __name__ == '__main__':
    port=randint(1025,9999)
    app.run('0.0.0.0',port)