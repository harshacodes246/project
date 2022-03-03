from flask import Flask
from public import public
from admin import admin
from member import member
from supplier import supplier

app=Flask(__name__)
app.secret_key="abc"

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(member,url_prefix='/member')
app.register_blueprint(supplier,url_prefix='/supplier')
app.run(debug=True,port=5002)