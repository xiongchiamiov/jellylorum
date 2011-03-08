var APAnime = new Class({
	initialize: function(slug) {
		this.slug = slug;
		this.type =
		this.episodeCount =
		this.startDate =
		this.endDate =
		this.description = null;
	},
	
	update: function() {
		var anime = this;
		new Request.JSONP({
			url: 'http://fileserverness.ath.cx/jsonp.php?url=http://www.anime-planet.com/anime/'+this.slug,
			async: false, // this doesn't seem to actually work
			method: 'get',
			timeout: 3000,
			onSuccess: function(responseText){
				console.log('success!');
				var element, text, matches;

				element = new Element('div');
				element.set('html', responseText);

				text = element.getElement('.tabPanelLeft .type').get('text');
				matches = text.match(/^(\w+) \((\d+\+?)/);
				[, anime.type, anime.episodeCount] = matches;
				anime.episodeCount = parseInt(anime.episodeCount);
				
				anime.description = element.getElement('.entryContent .synopsis p').get('text');
				
				text = element.getElement('.tabPanelLeft .year').get('text');
				matches = text.match(/(\d+|\?) - (\d+|\?)/);
				[, anime.startDate, anime.endDate] = matches;
				anime.startDate = parseInt(anime.startDate);
				anime.endDate = parseInt(anime.endDate);
			},
			onFailure: function(xhr) {
				console.log('failure!');
				console.log(xhr);
			},
			onRequest: function() {
				console.log('request...');
			}
		}).send();
	}
});

