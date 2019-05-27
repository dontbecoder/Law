rule_1 = {'平等原则'     :'诉讼当事人的 诉讼权利 和 诉讼义务 平等！' + '平等包括权利义务相同，也可以是相对应的，但不一定是相等的'}
rule_2 = {'同等 对等原则' :'针对' + '外国人 ' + '无国籍人'}
rule_3 = {'辩论原则'      :{
                         '时间':'整个诉讼过程中' + '不仅限于法庭辩论阶段，包括一审、二审、再审程序',
                         '内容':'实体方面' + '程序方面',
                         '形式':'书面形式' + '口头形式',
                         '例外':['执行程序','特别程序','非诉讼程序'],# 不适用辩论原则的程序
            }}        
rule_4 = {'处分原则'      :{ # 当事人有权在法律规定的范围内处分自己的权利
                        '处分内容':'实体权利' + '诉讼权利',
                        '行使'    :'必须在法律规定范围内',
            }}
rule_5 = '诚实信用原则'    # 贯穿整个民事诉讼全过程，包括 依法行使诉讼权利、履行诉讼义务、遵守诉讼秩序、自觉履行生效文书等
rule_6 = {'检查监督原则':{ # 人民检察院有权对民事诉讼活动进行监督 （只监督公权力的部分！！）
                       '范围':'民事诉讼活动' + '人民法院 + 及其工作人员' +  '行使审判权' + '执行权' + '的行为与结果',
                       '方式':'抗诉' + '检查建议',
                } }
rule_7 = {'支持起诉原则':{
                        '主体':'机关' + '社会团体' + '企事业单位',
                        '起因':'对损害 国家、集体、或者个人民事权益的行为',
                        '方式':'为受害人' + '提供物质、精神、法律上的帮助' + '以受害人的名义起诉'
                } }

system_1 = {'合议制':{
                    '原则':'合议庭成员权利相同' + '少数服从多数' + '不同意见记入评议笔录' + '评议笔录和过程保密',
                    '一审':'由 审判员、人民陪审员 组成' or '由 审判员 组成',
                    '二审':'由 审判员 组成',
                    '再审':{ 
                            '原来是一审的':'按照一审程序 另行组成合议庭(不能适用简易程序)',
                            '原来是二审或上级法院提审的':'按照二审程序 另行组成合议庭',
                            },
                    '特别程序':'选民资格案件'or'重大疑难案件' + '由 审判员 组成合议庭',
            },
            '独任制':{
                    '简易程序':'基层法院（及其派出法庭） 审理简单的 第一审民事案件',
                    '特别程序':'宣告公民失踪、死亡'+'认定公民无、限制民事行为能力'+'认定财产无主'+'确认调解协议效力'+'实现担保物权',# '选民资格案件'or'重大疑难案件' + '由 审判员 组成合议庭',
                    '督促程序':'支付令',
                    '公示催告程序':{
                              '公示催告阶段':'独任',
                              '宣告票据无效':'由审判员组成合议庭',
                    },
            }
            }
system_2 = {'回避制':
                {
                '回避方式':['自行回避','申请回避','指令回避'],
                '申请程序':{ 
                          '方式':'口头'or'书面',
                          '时间':'法庭辩论终结前',
                            },
                '申请效力':'申请后、回避决定作出前' + '被申请人应当暂停本案工作（但需采取紧急措施的除外）',
                '回避决定':'坐审判台上的(审判长、副审判长、人民陪审员等)，由院长决定' + '台下的(书记员、鉴定人员、勘验人员等)，审判长决定' + '院长当然审判长时，由审委会决定',
                '救济':'可以复议一次' + '复议期间，被申请回避人不停止工作'
                }
                }
system_3 = {'公开审判制':{
                        '原则':'除法定不公开的' + '审判过程及结果 应当向外公开',
                        '法定不公开':['涉及国家秘密','个人隐私','法定其他案件'],
                        '经申请不公开':['离婚','涉及商业秘密'],
            }}
system_4 = '两审终审制'

def FormCollegiate(): # 组成合议庭
    if('人民陪审员'):
        ('一审案件' + '诉讼案件')

def ToCommittee(): # 提交审委会的程序
    if('合议庭无法形成多数意见'):
        ('提交院长决定是否提交审委会讨论决定')

def level_Jurisdiction():  # 级别管辖
    return { 
        {'基层法院管辖': ''},
        {'中级法院管辖': ''},
        {'高级法院管辖': ''},
        {'最高人民法院管辖': ''},
        }      

def local_Jurisdiction(): # 地域管辖
    return {
        '一般地域管辖':'原告就被告' + '被告就原告',
        '专属管辖':['不动产纠纷','港口作业','遗产纠纷','涉外专属管辖'],
        '合同纠纷管辖':{ # 没有约定履行地的情况，合同履行地分类
                    '标的为给付货币':'接收货币一方所在地',
                    '交付不动产':'不动产所在地',
                    '交付其他标的':'履行义务一方所在地',
                    '财产租赁合同、融资租赁合同':'租赁物使用地',
                    '网络交付标的':'买受人所在地',
                    '其他方式交付标的':'收货地',
                }, 
        '协议管辖':'',
        '侵权纠纷管辖':['侵权行为发生地','侵权产品生产地','侵权产品销售地','侵权产品服务提供地' + 'etc'],
        '其他特殊管辖':['公司诉讼','保险合同纠纷','票据纠纷','运输合同纠纷','运输侵权纠纷','海难救助','共同海损',],

    }
def decide_Jurisdiction(): # 裁定管辖
    return {
            '移送管辖': '纠错' + '上下级之间、平级之间',
            '指定管辖': '由共同上级指定',
            '管辖权转移': '变通' + '上下级之间',
        }
def Raise_objections(): # 提管辖权异议
    return {
        '主体':'本案当事人，有独三和无独三除外',
        '对象':'第一审民事案件管辖权',
        '时间':'提交 答辩状 期间',
        '应诉管辖':'当事人未提异议，并应诉答辩的，视为受诉法院有管辖权' + '但违法级别管辖 和 专属管辖的除外',
        '对异议处理':{
                    '异议成立的':'裁定移送',
                    '异议不成立的':'裁定驳回',
                    },
        '救济':'不服可以上诉', # 可以上诉的裁定有：管辖权异议、不予受理、驳回起诉
    }
     

def Determine_Jurisdiction():  # 管辖
       
    Jrule_1 = '管辖权恒定原则'
    Jrule_2 = '专门管辖' # 军事法院、知识产权法院、海事法院 etc

    if(Jrule_1 and not Jrule_2 ):
        level_Jurisdiction() # 级别管辖
        local_Jurisdiction() # 地域管辖
        decide_Jurisdiction() # 裁定管辖
        # 复杂合同纠纷的管辖问题
        if('专属管辖'):
            do = '专属管辖'
        elif ('协议管辖'):
            do = '协议管辖'
        elif ('法定管辖'):
            do = '被告住所地管辖'
            if('合同没履行') and ('约定履行地不在一方住所地'):
                do = '被告住所地管辖'
            elif ('合同已经履行') and ('约定履行地 != 实际履行地'):
                do += '约定履行地'

        if('有管辖异议'):  # 有管辖异议
            Raise_objections()

def Proof_procedure(): # 证明程序
	{ # 举证
	'及时举证':['法院在审理前的准备阶段确定当事人的举证期限','或者当事人协商后经法院准许'],
	'期限':['法院确定的，第一审普通程序案件不得少于15日','当事人提供新证据的二审案件不得少于10日'],
	'逾期后果':[
		'拒不说明理由或理由不成立的,法院可以不采纳',
		'拒不说明理由或理由不成立的,法院可以采纳,但予以训诫、罚款',
		'当事人因客观原因逾期的，或对方当事人对逾期提供证据未提出异议的，视为未逾期',
		'当事人因故意或重大过失逾期的,法院不予采纳',
		'当事人因故意或重大过失逾期的,但证据与案件基本事实有关,法院应当采纳,并予以训诫、罚款',
		'当事人非因故意或重大过失逾期的,法院应当采纳,并予以训诫'
	    ],
	}
	{ # 法院调查收集证据
	'以当事人申请':{
		'情形':['该证据属于国家有关部门保存并须经法院职权调取的档案材料','涉及国家秘密，商业秘密，个人隐私',
		'当事人及诉讼代理人因客观原因无法自行收集的'],
		'申请时间':'举证期限届满前',
		'救济':'对于法院不予准许的通知，可以复议一次(原级复议)'
        },
	
	'以职权':{
		'涉及国家、社会、第三人利益的事实':['可能损坏国家、社会公共利益的','涉及公益诉讼的','当事人恶意串通损害他人合法权益的'],
		'涉及身份关系的事实':['身份关系的'],
		'涉及程序性事项':['涉及依职权追加当事人、中止诉讼、终结诉讼、回避等程序性事项的'],
		}
	}
	{ # 质证
	'概念':'未经当事人质证的证据，不得作为认定案件事实的根据',
	'质证程序':['原则上公开质证，但涉及国家秘密，商业秘密，个人隐私的不得在公开开庭时质证',
			'当事人在审理准备阶段认可的证据，经审判人员在庭审中说明后，视为质证过的证据'
				]
	}
	{ # 非法证据排除
	'形成或获取方式':'严重侵害他人合法权益' or '违反法律禁止性规定'or'严重违背公序良俗的'
	}
	# 文书提出命令
	if('书证在对方当事人的控制下'):
		do='承担举证证明责任的当事人可以在 举证期限届满前 书面 申请法院责令对方提交'
	if('对方当事人无正当理由拒不提交'):
		do='法院可以认定书证内容为真实'
	if('持有书证的当事人以妨碍对方当事人使用书证为目的，毁灭书证等情形的'):
		do='法院可以对其罚款、拘留'
	

def Prov():  # 证明
    non_need_prov = {
	'免征事实':[
		'自然规律和定理',
        '众所周知的事实，一定范围内为人所知晓的事实',
		'根据已知事实和日常生活经验法则，能推定出的另一事实',
		'已为人民法院生效判决所确定的事实',
        '已为仲裁机构生效判决所确认的事实',
		'已生效公证文书所证明的事实',
        '自认事实'
	    ]
	}
    prov_responsiblity = '证明责任' # 谁主张，谁举证
    proof_standard = ['一般标准,高度可能性','特殊标准,排除合理怀疑']  # 证明标准
    if(prov_responsiblity): # 有举证责任
        prof = '本证'
        if(proof_standard): # 本证达到证明标准
            return True # 举证成功
        else:
		    return False # 举证人应当承担证明责任的不利后果
        
        if(not prov_responsiblity):    # 无举证责任，没有提供证据的义务，有提供证据的权利
            prof = '反证' 
	    if(proof_standard): 
		    return True # 反证达到证明标准,对对方不利
	    else:
		    pass		# 反证未达到证明标准,无影响


def JointLitigation():  # 共同诉讼
    pass


def Preservation_1():  # 证据保全
    if('诉前证据保全'):
		if('情况紧急,证据可能灭失或日后难以取得') and ('利害关系人')and('起诉或申请仲裁前')and('应当责令提供担保'):
			if('在48小时内'):
				do = '证据所在地、被申请人住所地、对案件有管辖权的法院执行'
			if('申请人自保全之日起30天内不起诉、或申请仲裁的'):
				do = '解除保全'
    elif ('诉中证据保全'):
        if(('证据可能灭失或日后难以取得') and (('当事人申请')or('法院依职权')) and('举证期限届满前')):
            if('在48小时内'):
			    if('可能给他人造成损失'):
				    do = '受理案件法院执行，应当责令提供担保'
			    else:
				    do = '受理案件法院执行'
def Preservation_2():  # 保全                    
    if ('诉讼前保全'):
        do={
            '适用情形':'不立即采取保全措施，将使申请人合法权益受到难以弥补的损害',
            '启动方式':['依当事人申请'],
            '担保':['应当'+'责令提供担保'],
            '管辖':['被保全财产所在地','被申请人住所地','对案件有管辖权的法院'],
            '期限':['48小时内作出裁定','申请人自保全之日起30天内不起诉、或申请仲裁的,法院解除保全措施'],
        }
    elif ('诉讼中保全'):
        do = {
            '适用情形':'可能因一方当事人的行为或其他原因，使判决难以执行，或者造成当事人其他损害的案件',
            '启动方式':['依当事人申请','法院依职权'],
            '担保':['可以'+'责令提供担保','申请人不提供的，裁定驳回'],
            '管辖':'受理案件的法院'+'上诉案件中，二审法院收到报送案件前，由一审法院采取',
            '期限':'情况紧急的，48小时内作出裁定',
        }
    elif ('执行前保全'):
        do = {
            '适用情形':'债权人应对方转移财产等紧急情况，使得生效法律文书可能不能执行或难以执行的',
            '启动方式':'依当事人申请',
            '申请时间':'法律文书生效后，进入执行程序前',
            '管辖':'执行法院',
            '解除':'债权人应当在法律文书指定的履行期限届满后5日内申请执行，否则，法院应当解除保全'            
        }
    do.update(
        {
        '财产保全的范围':['与本案有关的财物','抵押物、留置物可以冻结、查封，但抵押权人和留置权人有优先受偿权'],
        '救济':'对保全裁定不服，可以申请复议一次'+'复议期间，不停止原裁定执行',
        '应当解除保全裁定的情形':[ '保全错误的','申请人撤回保全申请的',
                        '申请人的起诉或者诉讼请求被生效裁决驳回的',
                        '财产纠纷案件，被申请人向法院提供担保的'
                    ]    
        }
    )

def ExecuteFirst():  # 先予执行
    name = {
        '定义':'法院终局判决之前'+'为解决权利人生活或生产经营的急需'+'权利人申请'+'依法裁定义务人先行履行义务的制度',
        '适用情形':['追索赡养费，抚养费，抚育费，抚恤金，医疗费等案件',
                   '追索劳动报酬',
                   '需要立即停止侵害，排除妨碍的' or '需要立即停止某项行为的' or 
                   '追索恢复生产、经营急需的保险理赔费用的' or '需要立即返还社会保险金、社会救助资金的'or
                   '不立即返还款项，将严重影响权利人生活和生产经营的'
                   ]
    }
    if('当事人之间权利义务关系明确') and ('申请人有实现权利的迫切需要') and ('当事人向法院提出申请') and('被申请人有履行能力'):
       do={
           '申请':'向受诉法院申请'+'法院不能主动依职采取',
           '担保':'法院可以责令提供担保'+'不提供担保,驳回申请',
           '范围':'限于当事人诉讼请求的范围'+'且以当事人生活、生产经营的急需为限',
           '救济':'对裁定不服，可以申请复议一次'+'复议期间，不停止原裁定执行',
       } 

def MandatoryAction():  # (对妨碍诉讼的)强制措施
    p=[ #必须到庭的当事人
        '负有赡养、抚育、抚养义务和不到庭就无法查清案情的被告',
        '必须到庭才能查清案件基本事实的原告'
    ]
    if('拘传'):
        if('经两次传票传唤,无正当理由据不到庭'):
            do = '院长签发拘传票'
    if('罚款') or ('拘留'):
        if('妨碍诉讼、妨碍执行的行为'):
            do = {
                '程序':['均使用决定书,由院长批准',
                       '对决定不服，向上一级法院申请复议一次，复议不停止原决定的执行',
                       '法院对被拘留人采取拘留措施后，应当在24小时内通知其家属'or'确实无法按时通知或通知不到的，应当记录在案'
                ],
                '期限':'拘留，15日以下',
                '罚款':'对个人，10万以下' or '对单位，5万以上，100万以下',
                '执行':[
                    '有义务协助调查、执行的单位拒绝协助的',
                    '可以对单位罚款，对主要负责人罚款'+'对仍不履行义务的，可以拘留',
                    '同时向监察或有关机关提出给予纪律处分的司法建议'
                ]
            }

def TheTerm():  # 期间
    name = '法院、诉讼参与人进行或完成某种诉讼行为应当遵守的时间'
    term={
    '期间分类':{
        '法定期间':{ # 法律明确确定
            '绝对不可变期':['上诉期','第三人撤销之诉的起诉期','申请再审的期间'],
            '相对不可变期':[ # 经法律确定后，一般不得变更，特殊情况，可以依法变更
                            '一审审限',
                            '涉外案件中在中国境内没有住所的当事人的答辩、上诉期'
                    ] 
        },
        '指定期间':[
                    '法院根据审理案件的需要，依职权指定，通常不可变更',
                    '特殊情况，可依职权变更']
        },
    '计算方式':[
            '以时、日、月、年计算',
            '期间开始的时和日，不计算在内',
            '期限届满最后一日是法定节假日的，以节假日后的第一个工作日为期限届满的日期',
            '在途期间不包括在内，诉讼文书在期满前交邮的，不算过期'
            ],
    }
    #'耽误与顺延'
    if ('不可抗拒的事由或其他正当理由耽误期限') and ('需要当事人申请，法院不能主动依职权顺延')and('障碍消除后10日内'):
        do = '是否同意，由法院决定'
        

def Send():  # 送达
    if('直接送达'):
        if(not '离婚诉讼中，既是受送达人同住成年家属，又是另一方当事人的'):
            do='交送'+ ['受送达人'or'受送达人同住成年家属'or'法人，其他组织的法定代表人、主要负责人、负责收件人'or'诉讼代理人，受送达人指定的代收人']
    elif('留置送达'):
        if('拒收'):
            if(not '调解书'):# 调解书需当事人签收，不能留置送达
                do = {
                    '视为送达':[
                    '邀请有关基层组织或者所在单位代表到场，记明事由和日期,由送达人、见证人签名或盖章',
                    '采取拍照、录像等方式记录送达过程'
                ]}
    elif('电子送达'):
        if('受送达人同意'):
            if(not ['判决书'or '裁定书'or'调解书']): # 不能电子送达的几种
                do = '采用传真、电子邮件、移动通信等方式送达诉讼文书'
    elif('委托送达'):
        do = '委托其他法院代为送达'
    elif('转交送达'):
        do = {
            '受送达人为军人的':'通过部队团以上政治机关转交',
            '受送达人被监禁的':'通过所在监所转交',
            '受送达人被采取强制性教育措施的':'通过所在强制教育机构转交',
        }
    elif('邮寄送达'):
        do = '邮局挂号信方式'+'以挂号信回执记载日期为送达之日'
    elif('公告送达'):
        if('受送达人下落不明') or ('其他方式均无法送达'):
            if(not '支付令')and (not '简易程序审理的案件'):#不能公告送达的情形
                do = {'视为送达':['国内诉讼公告之日经过60日','涉外诉讼公告之日经过3个月']}

def Mediation():  # 法院调解，公力救济
    r1 = '自愿原则'
    r2 = '合法原则'
    rangeA = [ # 积极范围
            '可能通过调解解决的民事案件,应当调解',
            '离婚案件，应当先行调解',
                {
            '简易程序的下列案件，应当先行调解':[
                '婚姻家庭纠纷和继承纠纷',
                '劳务合同纠纷',
                '交通事故和工伤事故引起的，权利义务关系较为明确的损害赔偿纠纷',
                '宅基地和相邻权纠纷',
                '诉讼标的额较小的纠纷']
                }            
            ]
    rangeB = [ # 消极范围 
            '特别程序、督促程序、公示催告程序',
            '婚姻身份关系确认案件、其他依案件性质不能调解的民事案件'
            ]
    except1 = [
    '无民事行为能力人的离婚案件,法定代理人与对方达成协议要求发给判决书的,可以根据协议内容制作判决书',
    '涉外民事诉讼中,经调解双方达成协议，应当制作调解书；当事人要求发给判决书的，可以依协议内容制作判决书'
    ]
    stage=''
    scope=''
    if( stage in ['一审','二审','再审']):   # 适用阶段，不适用执行程序
        if(scope in rangeA) and (scope not in rangeB):
            if('当事人同意公开'):
                done = '公开调解过程'
            else:
                done = '不公开调解过程'  
            if('为保护国家、社会公共利益、他人合法权益,法院认为确有必要公开的'):
                done = '公开调解协议内容'
            else:
                done = '不公开调解协议内容'    

                special_list = [
                '调解协议超出原告诉讼请求的，可以准许',
                '双方可就不履行调解协议约定民事责任',
                '调解协议约定一方不履行协议，另一方可以请求法院作出判决的条款，不予准许',
                '调解协议具有以下情形的，不予确认:'+
                        [
                        '侵害国家、社会公共利益',
                        '侵害案外人利益',
                        '违背当事人真实意思',
                        '违反法律、行政法规禁止性规定'
                    ]    
                ]

                {
             '调解书':'原则上应当制作调解书，经当事人签收后生效'or'当事人拒不签收调解书的,调解书不生效，法院应当及时判决',
             '以下可以不作调解书的情形，将调解协议加入笔录，由双方当事人、审判人员、书记员签名或盖章后生效':
             [
              '调解和好的离婚案件',
              '调解维持收养关系的案件',
              '能够及时履行的案件',
              '其他不需要制作的情形'   
             ]        
                }

            if(scope not in except1):
                done = '当事人自行达成和解协议或者经调解达成调解协议后，请求法院据此制作判决书的，不予支持'
            if('担保问题'):
                done = ['协议约定一方提供担保或者案外人愿意提供担保的,应当准许',
                '调解书应当列明担保人，调解书应当送达担保人,担保人拒不签收调解书不影响调解书生效',
                '担保在符合担保法规定的条件时生效']
            elif('无独立请求权第三人'):
                done = [
                    '需要确定无独三承担义务的，应当经无独三同意，调解书应当送达无独三'+'其拒不签收的，调解书不生效，法院应当及时判决',
                    '既不享有权利又不承担义务的无独三，不签收调解书的不影响调解书生效'
                ]
    if('诉讼中的和解'): # 在诉讼过程中，当事人自行达成和解协议 
        do = {
        '申请撤诉，撤回起诉':'撤回后，视为没有起诉，当事人可以再次起诉',
        '申请法院依据和解协议制作调解书，结案':'若对方不履行，可以申请强制执行'    
        }


def GetFlowChart():  # 程序类型：普通程序、简易程序、公益诉讼程序、二审程序、审判监督程序、第三人撤销之诉
    pass


def Non_LitigationFlow():  # 非诉程序 = 特别程序 + 督促程序 + 公示催告程序
    pass


def Execution():  # 执行程序
    pass


def Arbitration():  # 仲裁
    pass


def ForeignRelated():  # 涉外民事诉讼程序
    pass


class Litigant():  # 当事人
    pass


class ThirdPerson():  # 第三人 = 有独三 + 无独三 + 撤销之诉第三人
    p1 = ''
    p2 = ''
    p3 = ''


class Agent():  # 代理人 = 法定代理人 + 诉讼代理人
    legal_agent = {  # 法定代理人
        '来源': '法律规定',
        '权限': '全权代理',
    }
    commission_agent = {  # 委托代理人
        '来源': '委托',
        '权限': ['一般授权=(委托书中仅写”全权代理“，视为一般代理)', '特别授权=(承认、放弃、变更诉讼请求、和解、反诉、上诉)'],
    }


class Evidence():  # 证据
    e = ['当事人陈诉', '书证', '物证', '视听资料', '电子证据', '证人证言', '鉴定意见', '勘验笔录']
    e_type1 = {  # 证据分类：证据的来源
        '原始证据': '',
        '传来证据': '',
    }
    e_type2 = {  # 证据分类：证据与待证事实关系
        '直接证据': '',
        '间接证据': '',
    }
    e_type3 = {  # 证据分类:证据与举证责任的关系
        '本证': '',
        '反证': '',
    }


def check_person():  # 检查适格当事人
    person = '?' # 当事人
    right_ability = {'诉讼权利能力':{
                    '自然人':'始于出生，终于死亡',
                    '法人或其他组织':'始于成立，终于终止', # 法人或其他组织注销为终止
                    }
            }
    action_ability = {'诉讼行为能力':{
                    '概念':'亲自参加诉讼行使诉讼权利，承担诉讼义务的资格',
                    '法人或其他组织':'与诉讼权利能力同时产生，同时消灭',
                    '自然人':['无民事行为能力人、限制民事行为能力人 = 无诉讼行为能力','完全民事行为能力人 = 具有诉讼行为能力 '],
                    '当事人资格':{
                            '概念':'本案所争议的 民事实体法律关系的 主体即为本案适格当事人',
                         },
                    }
            }
    in3 = {'有独三':{
            '诉讼地位':'原告',
            '参诉方式':'提起诉讼',
            '参诉时间':'案件受理后，辩论终结前',
            '撤销之诉':['因不能归责于本人的事由，未参加诉讼' and '有证据证明 发送法律效力的判决、裁定、调解书的内容有误 损害其民事权益的'],
            '管辖':'作出该判决、裁判的法院', # 终审法院
            }
    }
    withOut3 = {'无独三':{
                '参诉方式':'申请参加' or '被追加',
                '附条件享有的权利':['被判要承担责任的，有权上诉','被调解要承担义务的，需要签收同意，否则，调解书不生效，法院应当及时判决'],
                '无权享有的权利':['管辖权异议','放弃、变更诉讼请求','撤诉'],
                '撤销之诉':['因不能归责于本人的事由，未参加诉讼' and '有证据证明 发送法律效力的判决、裁定、调解书的内容有误 损害其民事权益的'],
                '管辖':'作出该判决、裁判的法院', # 终审法院
                }
    }
    if('诉讼权利能力') and ('诉讼行为能力'): # 自然人、法人、其他组织
        do = ('判断原告') and ('判断被告') and ('判断诉讼标的1')
        T1 = '诉讼标的1'
        T2 = '诉讼标的2'
        if(person in T1): # 新当事人 与诉讼标的有关
            if ('要钱的'):# 主张权利的
                '共同原告'
            else: # 赔钱的 ，承担责任的
                '共同被告'
        elif(person not in T1) and(person in T2):   #  新当事人 与诉讼标的无关，且基于新的诉讼标的T2(法律关系)参与进来
            if('要钱的'):# 主张权利的
                '有独三'
            else: # 赔钱的，承担责任的
                '无独三'
        else: 
            '证人'

    organization = {  # 其他组织
        '依法登记 + 领取营业执照':'个人独资企业 合伙企业 中外合作经营企业 外资企业 乡镇企业 街道企业',
        '依法设立 + 领取营业执照':'法人分支机构 社会团体的分支机构、代表机构',
        '依法设立 + 领取营业执照':'商业银行 政策性银行 非银行金融机构的分支机构'
    }
    individual = [  # 个体工商户 *
        '以营业执照上登记的经营者为当事人',
        '有字号的，以营业执照上登记的字号为当事人，但应同时注明经营者的基本信息',
        '营业执照上登记的经营者与实际不一致的，列为共同诉讼人'
    ]
    partnership = [  # 个人合伙

    ]
    Non_civil_capacity = [  # 无民事行为能力人、限制民事行为能力

    ]
    village_committee = ''  # 村民委员会、村民小组 *
    call = ''  # 挂靠
    # 法人的工作人员
    # 企业法人解散的 *
    # 提供劳务的
    # 劳务派遣期间
    # 担保法律关系中
    # 死者近亲属等

def check_procedure(): # 确认诉讼程序
    nature ='平等主体对抗，法院居中裁判，解决民事权利义务纠纷'  # 民事诉讼程序的本质
    if('诉讼程序'):
        return ('一审' or '二审' or '再审')
    else:# 非诉程序,不解决民事权利义务纠纷
        return ('特别程序(选民资格除外)' or '督促程序' or'公示催告程序')

def check_target():  # 检查诉讼标的
    nature = '法律关系' # 诉讼标的本质：当事人之间发生争议，并请求法院作出判决的实体法律关系
    request = '特定裁判' # 诉讼请求：当事人基于诉讼标的，请求法院作出的特点裁判
    reason = '事实和法律依据' # 诉讼理由：原告起诉并提出诉讼请求在事实和法律上的依据

def getSueClass():  # 检查诉的类型
    cls1 = {
           '诉讼类型':{ 
               '确认之诉':'请求法院 确认与被告之间是否存在 某种法律关系' + '分为 积极确认之诉 and 消极的确认之诉',
               '给付之诉':'请求法院判被告 履行一定义务' + '给付内容包括财物，行为（作为和不作为）',
               '形成之诉':'请求法院 消灭 or 变更 某种既存的法律关系',
           } 
          }
    # { '一个诉讼标的':'可以对应多个诉讼请求':'每个诉讼请求可以导致诉的性质（类型）不同' }
    cls2 = { # 反诉，是独立的诉！！！
            '反诉':'诉讼进行中，本诉被告对本诉原告 向法院提出的 独立反请求',
            '牵连关系':'本诉之间有牵连关系', # 并不要求基于相同法律关系
            '时间':'一审法庭辩论终结前', # 二审中提出反诉，二审应当调解(不可裁判，否则不能再上诉，除非双方当事人同意由二审法院一并审理，二审法院可以一并裁判);调解不成，告知另行起诉
            '管辖':'应当向受理本诉的法院提出' + '且受理本诉的法院对反诉有管辖权',
            '程序':'本、反诉 应当适用同一程序审理'
    }
    return cls1 or cls2

def CheckSue():  # 判断起诉条件
    Determine_Jurisdiction()    # 确认管辖
    check_procedure()           # 确认诉讼程序
    getSueClass()				# 确认诉的类型
    check_target()				# 确认诉讼标的
    check_person()				# 确认当事人
    
    


def Go1st_Adjudgment(): # 一审
    time = ''
    if('证据保全'):
        Preservation_1()
    elif('保全'):
        Preservation_2()
    if('需要强制措施'):
        MandatoryAction()  # 
	Prov()		# 举证、证明	
	Proof_procedure()	# 证明程序

    if('需要先予执行'):
        ExecuteFirst() 
    
    if(time in TheTerm()):# 期限内
        Send()      # 送达

def Go2nd_Adjudgment():
    body = {  # 主体
            '本案当事人':[  
                        '原告',
                        '被告',
                        '有独三',
                        '判决承担义务的无独三'
                        ]
    }
    obj = '一审判决' +'三类裁定: 不予受理 + 驳回起诉 + 管辖权异议' # 对象
    black_obj = [ # 不能上诉的裁判
                '最高人民法院的一审判决、裁定',
                '调解书一审终审',
                '裁定书(以上三类除外)一审终审',
                '特别程序、督促程序、公示催告程序一审终审',
                '小额诉讼程序(包括实体判决和管辖权异议、驳回起诉裁定)一审终审',
                '根据《婚姻法解释一》,有关婚姻效力的判决'
    ]
    Time = '判决15天，裁定10天，自送达之日起计算'
    style = '提交书面上诉状（口头上诉无效）'
    do={
        '审判组织':'由审判员组成合议庭审理',
        '审理范围':'围绕当事人上诉请求进行审理' + '当事人没有提出请求的，不予审理,但一审判决违法、损害国家、社会公共利益、他人合法权益的除外',
        '审理形式':'开庭审理为原则' + '合议庭经过阅卷和调查，询问当事人，对没有提出新的事实、证据或理由的，合议庭任务不需要开庭的' + '可以不开庭'
        }
    output = {
        '裁判':{
                    '原判决、裁定 +  事实清楚 + 适用法律正确' + '用判决、裁定方式 驳回上诉、维持原判',
                    '原判决、裁定 +  事实或者适用法律错误'    + '用判决、裁定方式 改判、撤销、变更',
                    '原判决、裁定 +  基本事实不清'           + ['裁定撤销原判、发回重审' ,'查清事实后依法改判'],
                    '原判决、裁定 +  严重违反法定程序(遗漏当事人、违法缺席判决等)'     +  '撤销原判，发回重审',
                    '若发回重审'+'原审法院适用一审程序审理，判决为一审判决，当事人可以上诉' ,
                    '原审法院对发回重审案件作出判决后' + '当事人上诉的' + '二审法院不得再次发回重审'
            },
        '调解':[
                    '可以调解' + '达成调解协议，应当制作调解书' + '调解书送达后，原判决视为撤销',
                    '一审中达成调解协议的' + '原则上制作调解书' + '符合法定情形也可以不制作调解书，而通过调解协议结案',
                    '二审、再审中达成调解协议的' + '必须制作调解书' + '调解书送达后，原判决视为撤销'
        ],
        '撤回起诉':[
                    '二审程序中' + '原审原告申请撤回起诉' + '经其他当事人同意' + '且不损害国家、社会公共、他人合法权益的' + '法院可以准许',
                    '准许撤诉的' + '应当一并裁定撤销一审裁判'    
        ],
        '撤回上诉':[
                    '二审判决宣告前' + '当事人可以申请撤回上诉' + '是否准许由二审法院裁定',
                    '二审法院经审查认为一审判决确有错误的' + '或 双方当事人串通损害国家、集体、社会公共利益及他人合法权益的' + '不应准许',
                    '撤回上诉的法律效果' + '自裁定准许撤回上诉之日起，一审判决生效'

        ],
    }
    # 两审终审的贯彻
    if ('当事人在一审中已提出诉讼请求，原审法院未作审理、判决') or ('必须参加诉讼的当事人或者有独三在一审中没有参加诉讼'):
        '调解不成、发回重审'

    if ('一审判决不准离婚，二审法院认为应对判决离婚的，对财产分割和子女抚养问题'):
        '调解不成、发回重审'
        if('当事人同意二审法院一并审理的'):
            '可以由二审法院一并审理'
            
    if ('原告新增独立诉讼请求') or ('被告提出反诉的'):
        '调解不成、告知另诉'
        if('当事人同意二审法院一并审理的'):
            '可以由二审法院一并审理'

def GoBack():
    pass
#==============================================================================#


# 打官司
#
# 起诉--------审判--------判决结果--------不服，上诉--------二审--------二审结束
#									|_____服从判决
def main():
    if (True == CheckSue()):  # 判断起诉条件

        result = Go1st_Adjudgment()			# 一审

        if(result == '不服,上诉'):
            Go2nd_Adjudgment()  # 二审
        else:
            GoBack()
    else:
        GoBack()
