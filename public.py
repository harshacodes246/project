from flask import Flask,Blueprint,render_template,request,redirect,url_for,session
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template("index.html")
@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		username=request.form['uname']
		password=request.form['pass']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		print(res)
		if res:
			session['lid']=res[0]['login_id']
			if res[0]['usertype']=="admin":
				return redirect(url_for('admin.admin_home'))
			if res[0]['usertype']=="member":
				a="select * from members where login_id='%s'"%(session['lid'])
				res=select(a)
				if res:
					session['member_id']=res[0]['member_id']
					return redirect(url_for('member.member_home'))
			if res[0]['usertype']=="supplier":
			 	a="select * from suppliers where login_id='%s'"%(session['lid'])
			 	res=select(a)
			 	if res:
			 		session['supplier_id']=res[0]['supplier_id']
			 		return redirect(url_for('supplier.supplier_home'))
		

	return render_template("login.html")
@public.route('/supplier_register',methods=['get','post'])
def supplier_register():
		if 'register' in request.form:
			fname=request.form['fname']
			lname=request.form['lname']
			place=request.form['pl']
			phone=request.form['phone']
			email=request.form['Email']
			pin=request.form['Pincode']
			Licensenumber=request.form['Licensenumber']
			username=request.form['uname']
			password=request.form['pass']
			q="insert into login values(null,'%s','%s','pending')"%(username,password)
			id=insert(q)
			z="insert into suppliers values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email,pin,Licensenumber)
			insert(z)
		return render_template("supplier_registration.html")


@public.route('/member_registration',methods=['get','post'])
def member_registration():
	if 'register' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['pl']
		phone=request.form['phone']
		email=request.form['Email']
		pin=request.form['Pincode']
		username=request.form['uname']
		password=request.form['pass']
		q="insert into login values(null,'%s','%s','pending')"%(username,password)
		id=insert(q)
		z="insert into members values(null,'%s','%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email,pin)
		insert(z)
	return render_template('member_registration.html')	





