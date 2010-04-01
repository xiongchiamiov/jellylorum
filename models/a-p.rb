# -*- coding: UTF-8 -*-
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
	LightMongo.database = 'a-p_test'
end

module AP
	class Anime
		include LightMongo::Document
		
		index :slug
		
		attr_accessor :slug         # string (key)
		attr_accessor :type         # string
		attr_accessor :episodeCount # integer
		attr_accessor :startDate    # date
		attr_accessor :endDate      # date
		attr_accessor :description  # text
		
		def initialize(slug)
			@slug = slug
		end
		
		def update!
			doc = Nokogiri::HTML(open("http://www.anime-planet.com/anime/#{@slug}"))
			
			doc.at_css('.tabPanelLeft .type').content =~ /^(\w+) \((\d+\+?)/
			@type = $1
			@episodeCount = $2
			
			@description = doc.at_css('.entryContent .synopsis p').content
			
			doc.at_css('.tabPanelLeft .year').content =~ /(\d+|\?) - (\d+|\?)/
			# assign nil if the date is unknown
			@startDate = $1 == '?' ? nil : Date.strptime($1, '%Y')
			@endDate = $2 == '?' ? nil : Date.strptime($2, '%Y')
		end
	end
end
