# -*- coding: UTF-8 -*-
require 'date'
require 'light_mongo'
require 'open-uri'
require 'nokogiri'

# LightMongo throws a RuntimeError if we don't have a default database set when
# we define a class that includes LightMongo::Document. Doing this in the test
# means that we have to require light_mongo explicitly, and then set the
# database inbetween that and requiring this file.  Eck.
begin
	LightMongo.database
rescue RuntimeError
	LightMongo.database = 'ann_test'
end

module ANN
	class Anime
		include LightMongo::Document
		
		index :id
		
		attr_accessor :id           # integer (key)
		attr_accessor :episodeCount # integer
		attr_accessor :startDate    # date
		attr_accessor :description  # text
		
		def initialize(id)
			@id = id
		end
		
		def update!
			# we have to force the encoding to utf-8,
			# because nokogiri doesn't auto-figure it out right :/
			doc = Nokogiri::HTML(open("http://www.animenewsnetwork.com/encyclopedia/anime.php?id=#{@id}"), nil, 'utf-8')
			
			# get all sorts of useful information, and some
			infos = doc.css('.encyc-info-type')
			
			infos.each do |info|
				case info.content.strip
				when /Number of episodes: \n\t(\d+)/
					@episodeCount = $1.to_i
				when /Vintage: \n\t([\d-]+)/
					@startDate = Date.parse($1)
				when /Plot Summary: \n\t(.*)/m
					#@description = $1.encode('iso-8859-1', 'utf-8')
					@description = $1
				end
			end
		end
	end
end
