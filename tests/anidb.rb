# -*- coding: UTF-8 -*-
require 'shoulda'
$LOAD_PATH.unshift File.dirname(__FILE__) + '/..'

require 'models/anidb'

class AniDBTest < Test::Unit::TestCase
	context "An AniDB model" do
		setup do
			@knt = AniDB::Anime.new(6466, 'tests/knt.xml')
			@ktm = AniDB::Anime.new(6468, 'tests/ktm.xml')
			@knt.update!
			@ktm.update!
		end
		
		context 'updated from the web' do
			should 'have the correct type' do
				assert_equal "TV Series", @knt.type
				assert_equal "OVA", @ktm.type
			end
			
			should 'have the correct number of episodes' do
				assert_equal 24, @knt.episodeCount
				assert_equal 1, @ktm.episodeCount
			end
			
			should 'have the correct year started' do
				assert_equal "07.10.2009", @knt.startDate.strftime("%d.%m.%Y")
				assert_equal 1987, @ktm.startDate.year
			end
			
			should 'have the correct year ended' do
				assert_equal nil, @knt.endDate
				assert_equal 1987, @ktm.endDate.year
			end
			
			should 'have the correct description' do
				description = <<EOS.strip
* Based on a shoujo manga by Shiina Karuho, serialised in Bessatsu Margaret.
Kuronuma Sawako is the perfect heroine... for a horror movie. With her jet-black hair, sinister smile and silent demeanor, she`s often mistaken for the haunting movie character Sadako. But behind her scary facade is a very misunderstood teenager. Too shy to fit in, all she wants to do is make some friends. But when a popular boy in class befriends her, she`s sure to make more than just that--she`s about to make some enemies too! 
Source: Manga-Updates
EOS
				assert_equal description, @knt.description
				assert_equal 'An erotic version of the classical Japanese folktale "The Tale of the Bamboo Cutter", produced by Tokyo Studio.', @ktm.description
			end
		end
	end
end
