require 'rubygems'
require 'sinatra'
require 'liquid'

$file_system = Liquid::LocalFileSystem.new("views")
$templates = {}
$templates['index'] = $file_system.read_template_file("index")

get '/' do
	Liquid::Template.parse($templates['index']).render
end
