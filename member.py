from public import * 

member=Blueprint('member',__name__)


@member.route('/member_home')
def member_home():
	return render_template("member_home.html")

@member.route('/member_request',methods=['get','post'])
def member_request():
	data={}
	m_id=session['member_id']
	q="select * from suppliers"
	res=select(q)
	data['suppliers']=res
	print(data['suppliers'])
	if 'submit' in request.form:
		Food=request.form['foodname']
		Description=request.form['des']
		Date_for_food_deliver=request.form['dfd']
		sid=request.form['sid']
		z="insert into mrequest values(null,'%s','%s','%s','%s','%s',curdate(),'pending')"%(m_id,sid,Food,Description,Date_for_food_deliver)
		insert(z)
	return render_template("member_requestfood.html",data=data)

@member.route('/member_send_complaint_home',methods=['get','post'])
def member_send_complaint_home():
	data={}
	m_id=session['member_id']

	if 'register' in request.form:
		complaint=request.form['Complaint']
		z="INSERT INTO complaint VALUES(NULL,'%s','member','%s','pending',CURDATE())"%(m_id,complaint)
		insert(z)

	q="select * from complaint where sender_id='%s' and sendedby='member'"%(m_id)
	res=select(q)
	data['complaint']=res
	return render_template("member_send_complaint.html",data=data)



@member.route('/member_view_rqst_to_sup')
def member_view_rqst_to_sup():
	q="select * from member_id"
	return render_template("member_view_rqst_to_sup.html")




