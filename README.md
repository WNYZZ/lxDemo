# lxDemo


抽查检测小项目


	infoDefault.html       #抽样列表

	new_sampling.html      #新建抽样信息

	update_sampling.html   #修改抽样信息


	ap_add.html #新增顺德区农产品抽样检测记录

	ap_update.html #更新顺德区农产品抽样检测记录

	ap_sampleArea.html #抽样地点

	ap_sampleCompany.html  #受检单位

	ap_sampleMode.html     #处理方式

	ap_sampleName.html     #样品名称

	ap_samplePeople.html   #受检人

	ap_sampleResult.html   #检测结果

	ap_sampleSource.html   #抽样来源

	ap_sampleType.html     #抽样类型

	ap_table.html          #农产品抽样检测记录表





	vfp_area.html          #蔬菜产地

	vfp_operator.html      #生产商/经营商

	vfp_reaction.html      #反应记录

	vfp_table.html         #蔬菜农药残留检测记录表

	vfp_varieties.html     #蔬菜品种












/********************************************表********************************************/

	infoclass 
		id     类型      是否校对      是否删除     升降序     抽样人     校对人        镇街     新增日期      校对日期     合格率
		id     type      is_check 		is_Del 		order 	   sampling	  correcting	town      enw_time		check_time 	percent  	

		ap_list #农产品抽样表
			id      classID      序号      样品名称ID   样品编号      抽样数量      	  抽样基数      抽样地点ID      样品来源ID      样品类型ID      受检单位电话ID      受检人ID     			
			id      classID	    number		ap_name	   sample_name   sampling_number    sampling_base    ap_area         all_source       ap_type        ap_company         ap_people    

			检测结果ID      处理方式ID      备注      是否校对      新增日期      校对日期
			all_result	    ap_mode		  remarks    is_check        new_time     check_time


	ap_area  #抽样地点
		id  title
		
	ap_company  #受检单位
		id  title
		
	ap_mode   #处理方式
		id  title
		
	ap_name  #样品名称
		id  title
		
	ap_people #受检人
		id  title
		
	ap_type   #抽样类型
		id  title
		

		vfp_list   #农药残留表
			id       classID       序号        生产商/经营商ID        蔬菜品种ID        测试反应记录ID        产地ID        样品来源ID        合格判定ID        备注        是否校对  
			id       classID       number       vfp_operator        vfp_varieties        vfp_reaction        vfp_area      	all_source         all_result     remarks       is_check

			新增日期        校对日期						
			new_time       check_time
			

	vfp_area  #蔬菜产地
		id  title
		
	vfp_operator  #生产商经营商
		id  title
		
	vfp_reaction  #反应记录
		id  title
		
	vfp_varieties #蔬菜品种
		id  title





	all_result  #检测结果   
		id  title   类型
		id  title   type


	all_source #抽样来源
		id  title   类型
		id  title   type	




