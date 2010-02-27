require 'date'
require 'dm-core'
require 'open-uri'
require 'xmlsimple'
require 'zlib'

module AniDB
	class Anime
		include DataMapper::Resource
		
		property :id,           Integer, :key => true
		property :type,         String
		property :episodeCount, Integer
		property :startDate,    Date
		property :endDate,      Date
		property :description,  Text
		
		def initialize(id, file=nil)
			@id = id
			@file = file
		end
		
		def update!
			# load up from a file, if we have one
			uncompressed = @file \
						|| Zlib::GzipReader.new(open("http://api.anidb.net:9001/httpapi?request=anime&client=jellylorum&clientver=1&protover=1&aid=#{@id}")).read()
			# automagic hash!
			xml = XmlSimple.xml_in uncompressed
			xml.default = []
			# sanity check
			fail if @id != xml['id'].to_i
			
			@type = xml['type'][0]
			@episodeCount = xml['episodecount'][0].to_i
			parse = lambda do |date|
				begin
					return Date.parse(date)
				# sometimes, all we can get is the year
				rescue ArgumentError
					return Date.strptime(date, '%Y')
				# and if it's still airing, the year is nil
				rescue TypeError
					return nil
				end
			end
			@startDate = parse.call xml['startdate'][0]
			@endDate = parse.call xml['enddate'][0]
			@description = xml['description'][0]
		end
	end
end
