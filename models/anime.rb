# -*- coding: UTF-8 -*-
require 'mongo_adapter'

class Anime
	include DataMapper::Mongo::Resource
	
	property :id, Serial
	property :slug, String, :key => true
	property :titles, Array
	
	property :anidb, Integer
	property :ap, Integer
	property :ann, Integer
end
