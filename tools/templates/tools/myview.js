function set_validate(){
	document.getElementById('id_validate').value=1

}

function myFunction(){
	form_count = document.getElementById('id_extra_field_count').value;
	
	if (form_count == ''){
		form_count = 0
	}
	//alert(form_count);
	form_count_new = parseInt(form_count) + 1;
	document.getElementById('id_extra_field_count').value=form_count_new;
	document.getElementById('id_validate').value=0;
}
function myFunction_del(){
	form_count = document.getElementById('id_extra_field_count').value;
	//alert(form_count);
	if (form_count == 0){
		form_count=0
		} else {
	      form_count_new = parseInt(form_count) - 1;		
	}
	
	document.getElementById('id_extra_field_count').value=form_count_new;
	document.getElementById('id_validate').value=0;
}

