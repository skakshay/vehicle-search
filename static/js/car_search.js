$(function(){

	function getCookie(name){
		var cookieValue = null;
		if (document.cookie && document.cookie !== '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				if (cookie.substring(0, name.length + 1) === (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}

	var input = "";
	function updateSource(){
		var source = $( "#id_search_string" ).autocomplete( "option", "source" );
		var currInput = document.getElementById("id_search_string").value;
		if(source.length<30 && source.length>0 &&  currInput.includes(input)){
			return;
		}

		$.ajax({
			url : searchURL,
			dataType : 'json',
			data : {
				search_string : currInput
			},
			success : function(data, textStatus, jqXHR){
				$( "#id_search_string" ).autocomplete( "option","source", data.model_list);
				input = currInput;
			}

		});
	}

	$("#id_search_string").autocomplete({
		source : [],
		minLength : 2,
		delay: 100, 
		select : function(event, ui){
			var csrftoken = getCookie('csrftoken');
			$.ajax({
				type : 'POST',
				url : selectURL,
				headers : {
					'X-CSRFToken' : csrftoken
				},
				data: {
					search_string: ui.item['label']	
				},
				success : function(data, textStatus, jqXHR){
					console.log(data);
				}
			});
		},
		search : function(event, ui){
			updateSource();
		}
	});
});