var importJs=document.createElement('script');  
	importJs.setAttribute("type","text/javascript"); 
	importJs.setAttribute("src", "https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"); 
	document.getElementsByTagName("head")[0].appendChild(importJs);
setTimeout(fuck,1000);
function fuck(){
	$.get('https://raw.githubusercontent.com/ghosx/git/master/json.json', function(data) {
		console.log("get data success");
		var s = JSON.parse(data);
		$('table[id$=DataGridA] tbody tr').each(function(index, el) {
			var question = $(this).find('td tbody tr:nth(0) td span').text().replace(/\d+ 、/g,"");
			console.log(question);
			if(s[question]){
				console.log(s[question]);
				var fuck1 = $(this).find('table[id$=RBLAData] tr td:nth(0) label');
				var fuck2 = $(this).find('table[id$=RBLAData] tr td:nth(1) label');
				var fuck3 = $(this).find('table[id$=RBLAData] tr td:nth(2) label');
				var fuck4 = $(this).find('table[id$=RBLAData] tr td:nth(3) label');
				if(fuck1.text().indexOf(s[question])!=-1){
					$(this).find('table[id$=RBLAData] tbody tr input:radio').eq(0).attr('checked', 'checked');	
				}else if(fuck2.text().indexOf(s[question])!=-1){
					$(this).find('table[id$=RBLAData] tbody tr input:radio').eq(1).attr('checked', 'checked');	
				}else if(fuck3.text().indexOf(s[question])!=-1){
					$(this).find('table[id$=RBLAData] tbody tr input:radio').eq(2).attr('checked', 'checked');	
				}else if(fuck4.text().indexOf(s[question])!=-1){
					$(this).find('table[id$=RBLAData] tbody tr input:radio').eq(3).attr('checked', 'checked');	
				}
			}
		 });
		$('table[id$=DataGridC] tbody tr').each(function(index, el) {
			var que = $(this).find('span[id$=labCDataTitle]').text().replace(/\d+ 、/g,"");;
			console.log(que);
			if(s[que]){
				console.log(s[que]);
				if(s[que]=="正确"){
					$(this).find('table[id$=RBLCData] tr td:nth(0) input:radio').attr('checked', 'checked');
				}else if(s[que]=="错误"){
					$(this).find('table[id$=RBLCData] tr td:nth(1) input:radio').attr('checked', 'checked');
				}
			}
		});
	});
	alert("别呼吸~点击确定后倒数5秒奇迹将会发生")
}
