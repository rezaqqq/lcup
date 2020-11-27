import os

from flask import Flask, request, send_from_directory,render_template,redirect,url_for


thedir = os.path.dirname(__file__)


api = Flask(__name__)

@api.route("/")
def index():
    listoffiles=os.listdir()
    return render_template("files.html",listoffiles=listoffiles)

@api.route("/upload",methods=['POST'])
def upload ():
    upfile=request.files['file']
    upfile.save(upfile.filename)
    return redirect(url_for("index"))
    
@api.route("/files/<path:path>")
def get_file(path):
    return send_from_directory(thedir, path, as_attachment=True)


if __name__ == "__main__":
    api.run(host="0.0.0.0", port=8008)
