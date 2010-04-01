# -*- coding: UTF-8 -*-
require 'shoulda'
$LOAD_PATH.unshift File.dirname(__FILE__) + '/..'

require 'models/a-p'

class APTest < Test::Unit::TestCase
	context 'An A-P model' do
		setup do
			@knt = AP::Anime.new('kimi-ni-todoke')
			@knt.update!
		end
		
		context 'updated from the web' do
			should 'have the correct type' do
				assert_equal 'TV', @knt.type
			end
			
			should 'have the correct number of episodes' do
				assert_equal '25', @knt.episodeCount
			end
			
			should 'have the correct year started' do
				assert_equal 2009, @knt.startDate.year
			end
			
			should 'have the correct year ended' do
				assert_equal 2010, @knt.endDate.year
			end
			
			should 'have the correct description' do
				assert_equal "Sawako Kuronuma is just like any other high school girl who wants to make friends and be useful. The only problem is she bears a worrying resemblance to Sadako from 'The Ring!' Because of her reputation, people are not only terrified of her, but small dogs even bark in fear at her presence; in fact, the only person in school who will talk to her is the lively class hottie, Kazehara. As the pair spends more time together, Kazehara slowly begins to bring Sawako out of her shell and soon their feelings for each other develop further. Though with her crippling insecurities, lack of social skills, and a series of cruel rumors and misunderstandings, it seems that Sawako's dream of a normal life won’t be quite so easy to obtain.", @knt.description
			end
		end
		
		teardown do
			LightMongo.connection.drop_database(LightMongo.database.name)
		end
	end
end
