# -*- coding: UTF-8 -*-
require 'rubygems'
require 'sinatra'
require 'haml'
require 'dm-core'

require 'models/anime'
require 'models/anidb'
require 'models/layout'

# setup stuff
DataMapper::Logger.new($stdout, :debug)
DataMapper::setup(:default, "sqlite3://#{Dir.pwd}/sqlite.db")
DataMapper::setup(:mongodb, :adapter => 'mongo', :database => 'jellylorum')
AniDB::Anime.auto_migrate!

get '/' do
	data = {}
	data['message'] = 'Hihi~'
	
	haml :index, :locals => data
end

post '/anime/' do
	redirect '/anime/kimi-ni-todoke/'
end

get '/anime/*' do
	data = {}
	
	anime = repository(:mongodb) { Anime.create }
	anime.anidb = 6466
	
	data['anime'] = {'anidb' => AniDB::Anime.new(6466, 'tests/knt.xml') }
	data['anime']['anidb'].update!
	
	layout = repository(:mongodb) { Layout.create }
	layout.columns = [[20,
					   [['anidb', 'type'],
						['anidb', 'episodeCount']]],
					  [50,
					   [['anidb', 'description']]],
					  [29,
					   [['anidb', 'startDate'],
						['anidb', 'endDate']]]]
	data['layout'] = layout
	
	haml :anime, :locals => data
end
