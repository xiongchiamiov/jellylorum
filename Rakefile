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
