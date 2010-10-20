#require "mg"
#MG.new("jellylorum.gemspec")

require 'fileutils'
require 'rake/testtask'

task :default => :test

Rake::TestTask.new("test") do |t|
	t.pattern = 'tests/*.rb'
end

task :startdb do
	sh %{mongod --dbpath /data/db > /dev/null &}
end

task :seeddb do
	require 'models/a-p'
	require 'models/anidb'
	require 'models/anime'
	require 'models/ann'
	require 'models/layout'
	
	knt = Anime.new
	knt.anidb = AniDB::Anime.new(6466, 'tests/knt.xml')
end
