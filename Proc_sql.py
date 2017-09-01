#coding=utf-8
import MySQLdb

class Proc_SQL():
	def __init__(self,host = '127.0.0.1', port = 8091, user = '*', passwd = '**', db = '*'):
		self._host = host
		self._port = port
		self._user = user
		self._passwd = passwd
		self._db = db
		self.connect = MySQLdb.connect(
			host = self._host,
			port = self._port,
			user = self._user,
			passwd = self._passwd,
			db = self._db,
			)
		self.cursor = self.connect.cursor()
		self.cursor.execute('SET NAMES GBK')
		print 'Init class success'
		
	def select_sql(self, brand):
	    test_sql = "insert into brand_info(brand) \
				select %s from dual where not exists \
				(select brand from brand_info t where t.brand=%s);" % ('%s', '%s')
		sql = "select * from brand_info where brand=%s" % '%s'
		result = ''
		try:
			self.cursor.execute(test_sql, (brand, brand))
			self.cursor.execute(sql, brand)
			data = self.cursor.fetchall()
			for item in data:
				result = str(item[0]) + '\t' + str(item[1]) + '\t' + str(item[2]) + '\t' + str(item[3]) + '\t' + str(item[4])
		except Exception, e:
			print e
			print sql
		return result

	def insert_competitor_sql(self, brand, competitor):
		#find brand, competitor id
		result = self.select_sql(brand)
		brand_id = result.split('\t')[0]
		comp_list = []
		for item in competitor.split('\t'):
			res = select_sql(item).split('\t')[0]
			comp_list.append(res)
		sql = "insert into brand_competitor values(%s, %s) \
				on duplicate key update competitor=%s;" % ('%s', '%s', '%s')
		try:
			comp_str = '\t'.join(comp_list)
			self.cursor.execute(sql, (brand_id, comp_str, comp_str))
			self.connect.commit()
		except Exception, e:
			self.connect.rollback()
			print e
			print sql
	
	def insert_info_sql(self, brand, show_url = '', domain = '', material = ''):
		sql = "insert into brand_info(brand,show_url,domain,material) values(%s,%s,%s,%s) \
				on duplicate key update show_url=%s,domain=%s,material=%s;" % ('%s', '%s', '%s', '%s','%s','%s','%s')
		try:
			self.cursor.execute(sql, (brand, show_url, domain, material, show_url, domain, material))
			self.connect.commit()
		except Exception, e:
			self.connect.rollback()
			print e
			print sql
			
	def insert_normalize_sql(self, query, brand):
		res = self.select_sql(brand)
		brand_id = res.split('\t')[0]
		#print brand_id
		sql = "insert into brand_normalize(query,brand_id) values(%s,%s) \
				on duplicate key update query=%s,brand_id=%s;" % ('%s','%s','%s','%s')
		try:
			self.cursor.execute(sql, (query,brand_id,query,brand_id))
			self.connect.commit()
		except Exception, e:
			self.connect.rollback()
			print e
			print query + '\t' + brand	
		
	def delete_info_competitor(self, brand):
		brand_id = self.select_sql(brand).split('\t')[0]
		sql = "delete from brand_competitor where brand=%s" % '%s'
		try:
			self.cursor.execute(sql, brand_id)
			self.connect.commit()
		except Exception, e:
			print e
			print sql
			self.connect.rollback()
		
	def delete_info_sql(self, brand):
		self.delete_info_competitor(self, brand)
		sql = "delete from brand_info where brand=%s;" % '%s'
		try:
			self.cursor.execute(sql, brand)
			self.connect.commit()
		except Exception, e:
			print e
			print sql
			self.connect.rollback()

	def __del__(self):
		self.cursor.close()
		self.connect.close()
		print "disconnect datebase"

if __name__ == '__main__':
	p = Proc_SQL()
	with open('./e.txt', 'r') as f:
		for line in f:
			arr = line.strip().split('\t')
			if len(arr) != 2:
				continue
			p.insert_normalize_sql(arr[0], arr[1])
	
	
