class company: # 企业法人	
	types # 股份公司（上市/非上市） / 有限责任公司
	RegisteredCapital # 注册资本
	Profit # 利润
	Loss # 亏损
	Equity # 股权
	Fund_1 = Profit*0.1 # 法定公积金 （提取：Profit*0.1 == Fund_1 <Profit*0.5，增资：Profit*0.25< Fund_1）
	Fund_2 # 任意公积金 , 取用Decide by Decision_1
	Fund_3 # 基本公积金
	class person: # 人
		Share_holder #  股东 = 自然人 / 法人
		Initiator    #  发起人 有限公司：Initiator<50,股份公司：Initiator<200
		Director # 董事
		Supervisor # 监事
		TopManager # 高管 (CEO、CFO、经理、财务负责人...)
		Cleaner # 清算组
	class File: # 文件
		Company_policy 		# 公司章程
		Shareholders_file 	# 股东名册
		Financial_report 	# 财务会计报告 必须有 + 要外审
		Investment_certificate # 出资证明书，在公司成立之后签发，仅出资证明，不影响股东资格
	class Decision: # 决议
		Decision_1 # 股东会
		Decision_2 # 董事会
		Decision_3 # 监事会
	def Captial_Increase:# 增资
		pass
	def Captial_Decrease:# 减资
		pass	
	def merge: # 合并
		(必须经代表2/3以上表决权的股东通过)
		(自作出合并决议之日10日内通知债权人) 
	def Separate: # 分立
		(必须经代表2/3以上表决权的股东通过) 
	def Equity_Rpurchase: # 股权回购
		pass
	def Disband: # 解散
		pass
	def Bankrupt: # 申请破产
		pass	
	def Clear:# 清算	
		if(inClear):# 清算、申报债权期间
			Can Not Do:# 不能开展与清算无关的经营活动 / 不能对债权人进行清偿
			Can Do:# 清理财产、编制资产负债表和财产清单 / 通知、公告债权人 / 处理与清算有关未了结业务/ 清税 / 代表参与民诉...
		if(inClaim):# 可申报债权范围=须以财产给付为内容的请求权 + 赔偿请求权 + （到期/未到期；附利息的，停止计息）债权 + 平等民事主体之间的请求权(即不包括行政处罚等)
			pass # 申报债权

	def Reorganize: # 重组
		pass	
	def ExtraordinaryMeeting: # 召开临时会
		if(person.Share_holder> (1/10)) or (person.Supervisor) or (Director>(1/3)):
			pass
	def guarantee:	# 担保
		pass
	def investment:	# 投资
		pass 
	def EquityTransaction: # 股权交易
		pass
		
		
# 股东代表诉讼 = 派生诉讼 = 股东代位诉讼
	if (公司合法权益受到不法侵害)&&(公司怠于起诉):
		(股东以自己名义其实)
		
	if (股东代表诉讼):
		if (有限责任公司的股东) or (连续180日以上单独或合计持股1%以上的股东):
			if (董事、高管违法) && ((有监事会)or(有监事)):
				(请求监事会或监事向法院提起诉讼)
			if (监事违法) && ((有董事会)or(有董事)):
				(请求董事会或董事向法院提起诉讼)

# 公司法人人格否认制度：在特定的法律关系中，如果公司股东滥用公司法人独立地位和股东有限责任，逃避债务，严重损害公司债权人利益的，应当对公司承担连带责任。
# 债权人可通过提起”法人人格否认之诉“来受偿

# 股份转让与回购
	if (减少公司注册资本) or (与持有本公司股份的其他公司合并) or (奖励给本公司职工) or (股东因对股东大会作出的合并、分立持异议，要求公司收购其股份的):
		(公司可以收购本公司股份)
	else:
		(公司不得收购本公司股份)
		
	if (股东向股东以外的人转让股份):
		if (有限公司):
			(应经其他股东过半数同意)
			(书面通知其他股东) # 其他股东自接收通知之日起满30日未答复的，视为同意；不同意又不优先购买的，视为同意
		elif (股份公司):
			(自由转让)
			
	if (发起人)：
		if (有限公司):
			(持有本公司股份，自公司成立之日起1年内不得转让)
		if (股份公司)：
			(公司公开发行前已发行的股份，自公司股票在证券交易所上市交易之日起1年内部的转让)
	
	if (董事) or (监事) or (高管):
		(向公司申报所持本公司的股份及其变动情况)
		(在任职期间，每年转让的股份不得超过其所持本公司股份的25%)
		(所持本公司股份，自公司股票在证券交易所上市交易之日起1年内部的转让)
		
# 董事会决议的表决，实行一人一票，不得按出资比例行使		
# 有限公司设监事会的必须有适当比例的职工监事		
		
		
# 股东抽逃出资
	if (制作虚假财务会计报表虚增利润进行分配) or 
	   (通过虚构债权债务关系将其出资转出) or 
	   (利用关联交易将出资转出) or 
	   (其他未经法定程序将出资抽回的行为):
			(构成抽逃出资)
			
	if (构成抽逃出资):
		(公司或者其他股东有权请求其向公司返还出资、本息；协助抽逃出资的其他人承担连带责任)
		
# 董监高任职资格
# 以下情形之一的，可以解除资格
# 无民事行为能力或限制民事行为能力
# 因贪污、贿赂、侵占财产、挪用财产或破坏社会主义市场经济秩序，被判处刑罚，执行期间满未逾5年；或被剥夺政治权利，执行期满未逾5年
# 担任破产清算公司、企业的董事或者厂长、经理，对该公司、企业的破产负有个人责任的，自该公司、企业破产清算完结之日起未逾3年
# 担任因违法被吊销营业执照、责令关闭的公司、企业的法定代表人，并负有个人责任的，自该公司、企业被吊销营业执照之日起未逾3年
# 个人所负数额较大的债务到期未清偿

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		