# -*- coding: UTF-8 -*-
require 'mongo_adapter'

class Layout
	include DataMapper::Mongo::Resource
	
	property :user_id, ObjectID
	property :columns, Array
	
	def self.default_repository_name
		:mongodb
	end
end
