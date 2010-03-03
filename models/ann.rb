# -*- coding: UTF-8 -*-
require 'date'
require 'dm-core'
require 'open-uri'
require 'nokogiri'

module ANN
	class Anime
		include DataMapper::Resource
		
		property :id,    Integer, :key => true
		property :episodeCount, Integer
		property :startDate, Date
		property :description, Text
		
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
