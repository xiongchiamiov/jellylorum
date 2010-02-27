# -*- coding: UTF-8 -*-
require 'dm-core'
require 'open-uri'
require 'nokogiri'

module AP
	class Anime
		include DataMapper::Resource
		
		property :slug,         String, :key => true
		property :type,         String
		property :episodeCount, Integer
		property :startDate,    Date
		property :endDate,      Date
		property :description,  Text
		
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
