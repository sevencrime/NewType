CRM登录:
	Test_Login.py

CRM开户表单(addApply):
	(常规输入, 不触发隐藏框)
	1, 个人账户,填写所有必填参数, 校验是否可以创建成功 >> test_addApplyAllNotEmpty.py::Test_addApplyAllNotEmpty::test_apply_IndividualNotEmpty
	2, 联名账户, 填写所有必填参数, 校验是否可以创建成功 >> test_addApplyAllNotEmpty.py::Test_addApplyAllNotEmpty::test_apply_JointNotEmpty
	3, 个人账户, 填写全部字段,校验是否可以创建成功 >> test_addApplyAllNotEmpty.py::Test_addApplyAllNotEmpty::test_apply_IndividualAll
	4, 联名账户, 填写全部字段, 校验是否可以创建成功 >> test_addApplyAllNotEmpty.py::Test_addApplyAllNotEmpty::test_apply_JointNotEmpty

	校验衍生产品隐藏框:
		(优先校验衍生产品是否必填)
		1, 账户类别选择香港及环球证券账户(现金),衍生产品选择"否", 校验是否可以创建成功 >> test_addApplyDerivativeProduct.py::Test_addApplyDerivativeProduct::test_apply_CashNotDerivativeProduct
		2, 账户类别选择香港及环球证券账户(现金),衍生产品选择"是", 风险声明披露不填, 校验风险声明披露是否必填 >> test_addApplyDerivativeProduct.py::Test_addApplyDerivativeProduct::test_apply_CashisDerivativeProductNone
		3, 账户类别选择香港及环球证券账户(现金),衍生产品选择"是", 风险声明披露选 "是", 校验是否创建成功 >> test_addApplyDerivativeProduct.py::Test_addApplyDerivativeProduct::test_apply_CashisDerivativeProductyes
		4, 账户类别选择香港及环球证券账户(现金),衍生产品选择"是", 风险声明披露选 "否", 校验是否会弹出提示框, 校验创建成功 >> test_addApplyDerivativeProduct.py::Test_addApplyDerivativeProduct::test_apply_CashisDerivativeProductNo
		5, 账户类别选择香港及环球证券账户(现金),衍生产品选择"否", 校验是否可以创建成功 >> test_addApplyDerivativeProduct.py::Test_addApplyDerivativeProduct::test_apply_MarginNotDerivativeProduct
		6, 账户类别选择香港及环球证券账户(现金),衍生产品选择"是", 风险声明披露不填, 校验风险声明披露是否必填 >> test_addApplyDerivativeProduct.py::Test_addApplyDerivativeProduct::test_apply_MarginisDerivativeProductNone
		7, 账户类别选择香港及环球证券账户(现金),衍生产品选择"是", 风险声明披露选 "是", 校验是否创建成功 >> test_addApplyDerivativeProduct.py::Test_addApplyDerivativeProduct::test_apply_MarginisDerivativeProductyes
		8, 账户类别选择香港及环球证券账户(现金),衍生产品选择"是", 风险声明披露选 "否", 校验是否会弹出提示框, 校验创建成功 >> test_addApplyDerivativeProduct.py::Test_addApplyDerivativeProduct::test_apply_MarginisDerivativeProductNo
		9, 账户类别选择非外汇, 黄金, ,证券, 校验是否会触发衍生产品隐藏框 >> test_addApplyDerivativeProduct.py::Test_addApplyDerivativeProduct::test_apply_PassDerivativeProduct
		10, 个人账户衍生产品选择"是", 风险声明披露选择"是", 联名账户衍生产品选择"是", 风险声明披露选择"是", 校验是否可以创建成功 >> test_addApplyDerivativeProduct.py::Test_addApplyDerivativeProduct::test_apply_jointDerivativeProductsameyes
		11, 个人账户衍生产品选择"是", 风险声明披露选择"是", 联名账户衍生产品选择"否", 校验是否会弹出提示 >> test_addApplyDerivativeProduct.py::Test_addApplyDerivativeProduct::test_apply_jointDerivativeProductDiffyes
		12, 个人账户衍生产品选择"否", 联名账户衍生产品选择"否", 校验是否可以创建成功 >> test_addApplyDerivativeProduct.py::Test_addApplyDerivativeProduct::test_apply_jointDerivativeProductsameno
		13, 个人账户衍生产品选择"否", 联名账户衍生产品选择"是", 校验是否会弹出提示 >> test_addApplyDerivativeProduct.py::Test_addApplyDerivativeProduct::test_apply_jointDerivativeProductDiffno

	选择杠杆式外汇, 黄金, 结构性衍生产品后, 投资目标不能单独选利息/股息收入:
		1, 账户类别选择金业账户, 投资目标单独选择利息/股息收入, 校验是否会弹出提示 >> test_addApplyInvestmentTarget.py::Test_addApplyInvestmentTarget::test_apply_BullionInvestmentTarget
		2, 账户类别选择杠杆式外汇账户, 投资目标单独选择利息/股息收入, 校验是否会弹出提示 >> test_addApplyInvestmentTarget.py::Test_addApplyInvestmentTarget::test_apply_LeveragedInvestmentTarget
		3, 衍生产品选择"是", 风险声明披露选择"是", 投资目标单独选择利息/股息收入, 校验是否会弹出提示 >> test_addApplyInvestmentTarget.py::Test_addApplyInvestmentTarget::test_apply_BuyProductInvestmentTarget

	校验开户方式隐藏框是否必填	:
		1, 开户方式选择手机应用程式身份认证--校验银行名称和银行账户号码是否必填 >> test_addApplyRequired.py::Test_addApplyRequired::test_apply_MobileAuthentication
		2, 开户方式选择电子签名认证--校验电子签名证书栏位是否必填 >> test_addApplyRequired.py::Test_addApplyRequired::test_apply_certificateNb

	选择开通黄金账户,杠杆式外汇账户,结构性衍生产品, 风险承受能力必须为高:
		1, 账户类别选择黄金账户,风险承受能力选择为"低", 校验是否会弹出提示 >> test_addApplyRiskTolerance.py::Test_addApplyRiskTolerance::test_apply_BullionRiskToleranceLow
		2, 账户类别选择黄金账户,风险承受能力选择为"中", 校验是否会弹出提示 >> test_addApplyRiskTolerance.py::Test_addApplyRiskTolerance::test_apply_BullionRiskToleranceMiddle
		3, 账户类别选择黄金账户,风险承受能力选择为"高", 校验是否可以创建成功 >> test_addApplyRiskTolerance.py::Test_addApplyRiskTolerance::test_apply_BullionRiskToleranceHigh
		4, 账户类别选择杠杆式外汇账户,风险承受能力选择为"低", 校验是否会弹出提示 >> test_addApplyRiskTolerance.py::Test_addApplyRiskTolerance::test_apply_LeveragedRiskToleranceLow
		5, 账户类别选择杠杆式外汇账户,风险承受能力选择为"中", 校验是否会弹出提示 >> test_addApplyRiskTolerance.py::Test_addApplyRiskTolerance::test_apply_LeveragedRiskToleranceMiddle
		6, 账户类别选择杠杆式外汇账户,风险承受能力选择为"高", 校验是否可以创建成功 >> test_addApplyRiskTolerance.py::Test_addApplyRiskTolerance::test_apply_LeveragedRiskToleranceHigh
		7, 衍生成功选择为"是",风险承受能力选择为"低", 校验是否会弹出提示 >> test_addApplyRiskTolerance.py::Test_addApplyRiskTolerance::test_apply_BuyProductRiskToleranceLow
		8, 衍生成功选择为"是",风险承受能力选择为"中", 校验是否会弹出提示 >> test_addApplyRiskTolerance.py::Test_addApplyRiskTolerance::test_apply_BuyProductRiskToleranceMiddle
		9, 衍生成功选择为"是",风险承受能力选择为"高", 校验是否可以创建成功 >> test_addApplyRiskTolerance.py::Test_addApplyRiskTolerance::test_apply_BuyProductRiskToleranceHigh

	从潜在客户获取:


			
	勾选证券账户后,配偶信息为必填:
		勾选证券,校验
		勾选非证券, 校验
		勾选证券, 填写
		勾选证券, 填一半


CRM审核流程(ReviewProves):
	1, CRM或apply_from来源数据, 审核步骤为:未处理--待cs2--待RO--待ops--success >> test_reviewProcess01.py::Test_reviewProcess1
	2, App来源数据, 审核步骤为: 待cs1--待cs2--待RO--待ops--success` >> test_reviewProcess02.py::Test_reviewProcess2
	3, App来源数据, 驳回操作, 步骤为: 待cs1--拒绝--CS1修改后重新提交给CS2--CS2拒绝 >> test_reviewProcess03.py::Test_reviewProcess3
	4, CRM来源数据, 驳回操作, 步骤为: 未处理---待cs2--拒绝--sales修改给CS2 >> test_reviewProcess04.py::Test_reviewProcess4
	5, 多角色RO, 全部RO一次性审核通过	>> test_reviewProcess14.py::Test_reviewProcess14
	6, 多角色RO, 审核其中的一个或多个 >> test_reviewProcess05.py::Test_reviewProcess5
	7, 证券RO拒绝, CS2驳回给证券RO >> test_reviewProcess06.py::Test_reviewProcess6
	8, 证券RO拒绝, CS2确定拒绝 >> test_reviewProcess07.py::Test_reviewProcess7
	9, 期货RO拒绝, CS2驳回给证券RO >> test_reviewProcess08.py::Test_reviewProcess8
	10, 期货RO拒绝, CS2确定拒绝 >> test_reviewProcess09.py::Test_reviewProcess9
	11, 外汇RO拒绝, CS2驳回给证券RO >> test_reviewProcess10.py::Test_reviewProcess10
	12, 外汇RO拒绝, CS2确定拒绝 >> test_reviewProcess11.py::Test_reviewProcess11
	13, 黄金RO拒绝, CS2驳回给证券RO >> test_reviewProcess12.py::Test_reviewProcess12
	14, 黄金RO拒绝, CS2确定拒绝 >> test_reviewProcess13.py::Test_reviewProcess13


修改数据
	1, sales修改, 修改全部
	2, CS1修改, 修改图片
	3, CS2修改, 修改图片, 推荐人-推广编号
	4, OPS修改, 图片


CRM创建活动:
	1, 创建活动,全字段 >> test_createActivity.py::Test_createActivity::test_AllCreateActivity
	2, 创建活动,必要字段 >> test_createActivity.py::Test_createActivity::test_RequiredCreate
	3, 非空校验 >> test_createActivity.py::Test_createActivity::test_NonCreateActivity

登記講座:
	1, 不勾选讲座
	2, 不填资料
	3, 填写错误邮箱
	4, 不选择来源
	5, 不勾选
	5, 选择人数

