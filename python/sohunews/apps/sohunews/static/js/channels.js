// render channel to page

var channels = function (array) {
	var html = "";
	var count = 0;

	html += '<div class="btn-group">';
	for (var i = 0; i < array.length; i++) {
		var tmp = array[i];
		var link = "/news/" + tmp.id + "/1";
		html += '<a href="#" onclick="get_specific_news(\'' + link + '\')" class="btn btn-default">'
		if (tmp.icon) {
			html += '<img src="' + tmp.icon +'" style="height:14px;"/>';	
		} else {
			html += '<span class="glyphicon glyphicon-info-sign"></span>';
		}
		html += tmp.name + '</a>';
		if (count % 10 === 0) {
			html += '</div>';
			html += '<div class="btn-group">';
		}
	}
	html += '</div>';
	$('#channels').html(html);
};
