# -*- coding: UTF-8 -*-
require 'shoulda'
$LOAD_PATH.unshift File.dirname(__FILE__) + '/..'

require 'models/ann'

class ANNTest < Test::Unit::TestCase
	context 'An ANN model' do
		setup do
			@knt = ANN::Anime.new(10625)
			@knt.update!
		end
		
		context 'updated from the web' do
			should 'have the correct number of episodes' do
				assert_equal 25, @knt.episodeCount
			end
			
			should 'have the correct year started' do
				assert_equal 2009, @knt.startDate.year
				assert_equal 10, @knt.startDate.month
				assert_equal 06, @knt.startDate.day
			end
			
			should 'have the correct description' do
				description = <<EOS.strip
Kuronuma Sawako is nicknamed Sadako due to her resemblance to the girl from the Japanese horror movies "The Ring". Shunned by her classmates, her life starts to change as she befriends Shōta Kazehaya, a very popular boy in her class.
	Kuronuma Sawako’s one wish in life is to make friends. That’s a difficult proposition when everyone who meets her cowers in terror. She admires her classmate, Kazehaya-kun, a popular, easygoing and 100% refreshing guy who is nice with everyone, even with her.
EOS
				assert_equal description, @knt.description
			end
		end
		
		teardown do
			LightMongo.connection.drop_database(LightMongo.database.name)
		end
	end
end
