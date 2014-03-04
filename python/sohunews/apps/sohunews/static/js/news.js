// render news

var news = function (array) {
	var html = "";

	for (var i = 0; i < array.length; i++) {
		var tmp = array[i];
		html += '<div class="panel panel-info">';
		var link = tmp.link.slice(7, -1)
		html += '<div class="panel-heading"><a href="/articles?' + link + '">' + tmp.title + '</a></div>';
		html += '<div class="panel-body">';
		html += '<div id="content">'
		html += '<span>' + tmp.description + '</span>';
		if (tmp.pics !== undefined) {
			html += '<span><img src="' + tmp.pics[0] + '" style="height: 150px; width: 200px;"></span>';
		}
		html += '</div></div></div>';
	}

	$("#news").html(html);
};


var get_specific_news = function (url) {
	$.ajax({
		url: url,
		dataType: "json",
		success: function (data, textStatus, jqXHR) {
			news(data);
		},
		error: function (jqXHR, textStatus, errorThrown) {
			console.log(errorThrown);
		}
	});
	return;
}