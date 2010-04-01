# -*- coding: UTF-8 -*-
require 'light_mongo'

# LightMongo throws a RuntimeError if we don't have a default database set when
# we define a class that includes LightMongo::Document. Doing this in the test
# means that we have to require light_mongo explicitly, and then set the
# database inbetween that and requiring this file.  Eck.
begin
	LightMongo.database
rescue RuntimeError
	LightMongo.database = 'layout_test'
end

class Layout
	include LightMongo::Document
	
	index :user_id
	attr_accessor :user_id, :columns
end
