from public import *
from database import *


admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
	return render_template("admin_home.html")

@admin.route('/adminviewsuppliers',methods=['get','post'])
def adminviewsuppliers():
	data={}
	q="select * from suppliers inner join login using(login_id)"
	print(q)
	res=select(q)
	data['supplier']=res
	print(res)
	if 'action' in request.args:
		action=request.args['action']
		login_id=request.args['l_id']
	else:
		action=None
	if action=="accept":
		q="update login set usertype='supplier' where login_id='%s'"%(login_id)
		update(q)	
		return redirect(url_for('admin.adminviewsuppliers'))
	if action=="reject":
		q="update login set usertype='reject' where login_id='%s'"%(login_id)
		update(q)	
		return redirect(url_for('admin.adminviewsuppliers'))
	return render_template('admin_viewsuppliers.html',data=data)


@admin.route('/admin_view_members',methods=['get','post'])
def admin_view_members():
	data={}
	q="select * from members inner join login using(login_id)"
	print(q)
	res=select(q)
	data['member']=res
	print(res)

	if 'action' in request.args:
		action=request.args['action']
		login_id=request.args['lid']
	else:
		action=None

	if action=="reject":
		q="update login set usertype='reject' where login_id='%s'"%(login_id)
		update(q)
		return redirect(url_for('admin.admin_view_members'))
	if action=="accept":
		q="update login set usertype='member' where login_id='%s'"%(login_id)
		update(q)
		return redirect(url_for('admin.admin_view_members'))
	return render_template('admin_view_members.html',data=data)


@admin.route('/admin_view_mrequest_to_s',methods=['get','post'])
def admin_view_mrequest_to_s():
	data={}
	q="SELECT *,`members`.`firstname` AS mfname,`suppliers`.`firstname` AS sfname FROM `mrequest` INNER JOIN `members` USING(`member_id`) INNER JOIN `suppliers` USING(`supplier_id`)"
	res=select(q)
	data['request']=res
	print(res)
	return render_template("admin_view_mrequest_to_s.html",data=data)

@admin.route('/admin_view_srequest_to_m',methods=['get','post'])
def admin_view_srequest_to_m():
	data={}
	q="SELECT *,`members`.`firstname` AS mfname,`suppliers`.`firstname` AS fname FROM `srequest` INNER JOIN `members` USING(`member_id`) INNER JOIN `suppliers` USING(supplier_id)"
	res=select(q)
	data['request']=res
	print(res)
	
	# q="select * from request"
	# res=select(q)
	# data['request']=res
	return render_template("admin_view_srequest_to_m.html",data=data)	

@admin.route('/admin_viewcomplaint',methods=['get','post'])
def admin_viewcomplaint():
	data={}
	q="select * from complaint"
	res=select(q)
	data['complaint']=res
	return render_template("admin_viewcomplaint.html",data=data)


@admin.route('/admin_send_reply',methods=['get','post'])
def admin_send_reply():
	id=request.args['id']
	if 'submit' in request.form:
		reply=request.form['reply']
		q="update complaint set reply='%s' where complaint_id='%s'"%(reply,id)
		update(q)
		return redirect(url_for('admin.admin_viewcomplaint'))
	return render_template("admin_send_reply.html")

