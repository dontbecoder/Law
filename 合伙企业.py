class Enterprise: # 	
	types # 公司（有限、股份、一人、上市）、合伙企业（普通合伙、有限合伙）
	limit # 国有、上市公司、公益性事业单位、社会团体不能做普通合伙人，只能做有限合伙人
	RegisteredCapital # 注册资本
	Profit=20 # 利润
	Loss # 亏损
	Equity # 股权
	Fund_1 = Profit*0.1 # 法定公积金 （提取：Profit*0.1 == Fund_1 <Profit*0.5，增资：Profit*0.25< Fund_1）
	Fund_2 # 任意公积金 , 取用Decide by Decision_1
	Fund_3 # 基本公积金
	#  人
	Share_holder='' #  股东 = 自然人 / 法人
	Initiator    #  发起人 有限公司：Initiator<50,股份公司：Initiator<200
	Director # 董事
	Supervisor # 监事
	TopManager # 高管 (CEO、CFO、经理、财务负责人...)
	Cleaner # 清算组
	#   文件
	Company_policy 		# 公司章程
	Shareholders_file 	# 股东名册
	Financial_report 	# 财务会计报告 必须有 + 要外审
			#  决议
	Decision_1 # 股东会
	Decision_2 # 董事会
	Decision_3 # 监事会



unit = Enterprise()

def Captial_Increase():	# 增资
	pass
def Captial_Decrease():	# 减资
	pass	
def merge(): 			# 合并
	pass 
def Separate(): 		# 分立
	pass 
def Equity_Rpurchase(): # 股权回购
	pass
def Disband(): 			# 解散
	pass
def Bankrupt(): 		# 破产
	pass	
def Clear():			# 清算	
	if('清算、申报债权期间'):		
		'Can Not Do':	# 不能开展与清算无关的经营活动 / 不能对债权人进行清偿
		'Can Do':		# 清理财产、编制资产负债表和财产清单 / 通知、公告债权人 / 处理与清算有关未了结业务/ 清税 / 代表参与民诉...
	
def Reorganize(): # 重组
	pass	
def ExtraordinaryMeeting(obj): # 召开临时会
	if(obj.Share_holder> (1/10)) or (obj.Supervisor) or (obj.Director>(1/3)):
		pass
def guarantee():	# 担保
	pass
def investment():	# 投资
	pass 
def EquityTransaction(): # 股权交易
	pass