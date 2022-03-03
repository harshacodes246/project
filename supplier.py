from public import * 

supplier=Blueprint('supplier',__name__)


@supplier.route('/supplier_home')
def supplier_home():
	return render_template("supplier_home.html")

@supplier.route('/supplier_viewrequest')
def supplier_viewrequest():
	data={}
	sid=session['supplier_id']
	q="select * from mrequest inner join members using(member_id)  where supplier_id='%s'"%(sid)
	res=select(q)
	print(q)
	print(res)
	data['request']=res

	if 'action' in request.args:
		action=request.args['action']
		mrequest_id=request.args['rid']
	else:
		action=None

	if action=="reject":
		q="update mrequest set status='reject' where mrequest_id='%s'"%(mrequest_id)
		update(q)
		return redirect(url_for('supplier.supplier_viewrequest'))
	if action=="accept":
		q="update mrequest set status='accept' where mrequest_id='%s'"%(mrequest_id)
		update(q)
		return redirect(url_for('supplier.supplier_viewrequest'))
	return render_template('supplier_viewrequest.html',data=data)











