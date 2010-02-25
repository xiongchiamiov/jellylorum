#require "mg"
#MG.new("jellylorum.gemspec")

require 'rake/testtask'

task :default => :test

Rake::TestTask.new("test") do |t|
	t.pattern = 'tests/*.rb'
end
