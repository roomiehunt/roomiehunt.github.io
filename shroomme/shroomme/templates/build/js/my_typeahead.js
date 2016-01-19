	var universities = new Bloodhound({
		datumTokenizer: Bloodhound.tokenizers.whitespace,
		queryTokenizer: Bloodhound.tokenizers.whitespace,
	  // url points to a json file that contains an array of country names, see
	  // https://github.com/twitter/typeahead.js/blob/gh-pages/data/countries.json
	 	prefetch: "{% static "data/data_universities.json" %}",

		remote: {
			url: "../search_name/",
			prepare: function (query, settings) {
				data_sent = {query:query,csrfmiddlewaretoken: '{{ csrf_token }}'}
				settings.type = "post";
/*						settings.contentType = "application/json; charset=UTF-8";
*/						settings.data = data_sent;
				return settings;
				}
			},
		rateLimitWait : 1000

	});

	// passing in `null` for the `options` arguments will result in the default
	// options being used
	$('.typeahead').typeahead(null, {
	  name: 'universities',
	  source: universities
	});			
