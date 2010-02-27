# -*- coding: UTF-8 -*-
require 'rubygems'
require 'sinatra'
require 'liquid'
require 'dm-core'
require 'models/anidb'

# setup stuff
DataMapper::Logger.new($stdout, :debug)
DataMapper::setup(:default, "sqlite3://#{Dir.pwd}/sqlite.db")
DataMapper.auto_migrate!

$file_system = Liquid::LocalFileSystem.new("views")
$templates = {}
['base', 'index'].each {|template| $templates[template] = $file_system.read_template_file(template)}

helpers do
	def render(template, data)
		Liquid::Template.parse($templates['base'])
						.render('content' => Liquid::Template.parse($templates[template])
															.render(data))
	end
end

get '/' do
	data = {}
	data['message'] = 'Hihi~'
	
	render('index', data)
end
