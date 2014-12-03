function formSubmit(text){
	var textValue = text.replace(/(^\s*)|(\s*$)/g, "");
	if(textValue==null || textValue=="") {
		var infoBlock = document.getElementById("info");
		alert('输入不能为空！');
        return false;  
    }
	return true;
}