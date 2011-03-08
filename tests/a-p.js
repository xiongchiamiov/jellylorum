describe('APAnime', function() {
	//var knt;

	beforeEach(function() {
		//knt = new APAnime('kimi-ni-todoke');
		//knt.update();
	});
	
	it('should have the correct type', function() {
		expect(knt.type).toEqual('TV');
	});
	
	it('should have the correct number of episodes', function() {
		expect(knt.episodeCount).toEqual(25);
	});
	
	it('should have the correct year started', function() {
		expect(knt.startDate).toEqual(2009);
	});
	
	it('should have the correct year ended', function() {
		expect(knt.endDate).toEqual(2010);
	});
	
	it('should have the correct description', function() {
		expect(knt.description).toEqual("Sawako Kuronuma is just like any other high school girl who wants to make friends and be useful. The only problem is she bears a worrying resemblance to Sadako from 'The Ring!' Because of her reputation, people are not only terrified of her, but small dogs even bark in fear at her presence; in fact, the only person in school who will talk to her is the lively class hottie, Kazehara. As the pair spends more time together, Kazehara slowly begins to bring Sawako out of her shell and soon their feelings for each other develop further. Though with her crippling insecurities, lack of social skills, and a series of cruel rumors and misunderstandings, it seems that Sawako's dream of a normal life won’t be quite so easy to obtain.");
	});
});

