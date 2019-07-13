CRM开户表单:
	(常规输入, 不触发隐藏框)
	1, 个人账户,填写所有必填参数, 校验是否可以创建成功 >> test_addApplyAllNotEmpty.py::Test_addApplyAllNotEmpty::test_apply_IndividualNotEmpty
	2, 联名账户, 填写所有必填参数, 校验是否可以创建成功 >> test_addApplyAllNotEmpty.py::Test_addApplyAllNotEmpty::test_apply_JointNotEmpty
	3, 个人账户, 填写全部字段,校验是否可以创建成功
	4, 联名账户, 填写全部字段, 校验是否可以创建成功

	校验衍生产品隐藏框:
		(优先校验衍生产品是否必填)
		1, 账户类别选择香港及环球证券账户(现金),衍生产品选择"否", 校验是否可以创建成功 >> test_addApplyDerivativeProduct::Test_addApplyDerivativeProduct::test_apply_CashNotDerivativeProduct
		2, 账户类别选择香港及环球证券账户(现金),衍生产品选择"是", 风险声明披露不填, 校验风险声明披露是否必填 >> test_addApplyDerivativeProduct::Test_addApplyDerivativeProduct::test_apply_CashisDerivativeProductNone
		3, 账户类别选择香港及环球证券账户(现金),衍生产品选择"是", 风险声明披露选 "是", 校验是否创建成功 >> test_addApplyDerivativeProduct::Test_addApplyDerivativeProduct::test_apply_CashisDerivativeProductyes
		4, 账户类别选择香港及环球证券账户(现金),衍生产品选择"是", 风险声明披露选 "否", 校验是否会弹出提示框, 校验创建成功 >> test_addApplyDerivativeProduct::Test_addApplyDerivativeProduct::test_apply_CashisDerivativeProductNo
		5, 账户类别选择香港及环球证券账户(现金),衍生产品选择"否", 校验是否可以创建成功 >> test_addApplyDerivativeProduct::Test_addApplyDerivativeProduct::test_apply_MarginNotDerivativeProduct
		6, 账户类别选择香港及环球证券账户(现金),衍生产品选择"是", 风险声明披露不填, 校验风险声明披露是否必填 >> test_addApplyDerivativeProduct::Test_addApplyDerivativeProduct::test_apply_MarginisDerivativeProductNone
		7, 账户类别选择香港及环球证券账户(现金),衍生产品选择"是", 风险声明披露选 "是", 校验是否创建成功 >> test_addApplyDerivativeProduct::Test_addApplyDerivativeProduct::test_apply_MarginisDerivativeProductyes
		8, 账户类别选择香港及环球证券账户(现金),衍生产品选择"是", 风险声明披露选 "否", 校验是否会弹出提示框, 校验创建成功 >> test_addApplyDerivativeProduct::Test_addApplyDerivativeProduct::test_apply_MarginisDerivativeProductNo
		9, 账户类别选择非外汇, 黄金, ,证券, 校验是否会触发衍生产品隐藏框 >> test_addApplyDerivativeProduct::Test_addApplyDerivativeProduct::test_apply_PassDerivativeProduct
		10, 个人账户衍生产品选择"是", 风险声明披露选择"是", 联名账户衍生产品选择"是", 风险声明披露选择"是", 校验是否可以创建成功 >> test_addApplyDerivativeProduct::Test_addApplyDerivativeProduct::test_apply_jointDerivativeProductsameyes
		11, 个人账户衍生产品选择"是", 风险声明披露选择"是", 联名账户衍生产品选择"否", 校验是否会弹出提示 >> test_addApplyDerivativeProduct::Test_addApplyDerivativeProduct::test_apply_jointDerivativeProductDiffyes
		12, 个人账户衍生产品选择"否", 联名账户衍生产品选择"否", 校验是否可以创建成功 >> test_addApplyDerivativeProduct::Test_addApplyDerivativeProduct::test_apply_jointDerivativeProductsameno
		13, 个人账户衍生产品选择"否", 联名账户衍生产品选择"是", 校验是否会弹出提示 >> test_addApplyDerivativeProduct::Test_addApplyDerivativeProduct::test_apply_jointDerivativeProductDiffno
