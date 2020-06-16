require 'rubygems'
require 'httparty'
require 'csv'

class Staff
	include HTTParty
	base_uri "teamtomato.herokuapp.com"

	def posts
		self.class.get('/api/v1/question')
	end
end

staff_data = Staff.new()
staffs = staff_data.posts
CSV.open("staffData.csv", "wb") do |csv| 
	csv << ["id", "shortForm", "staff", "subjectName", "url", "year"]
	for staf in staffs
		id = staf['id']
		shortForm = staf['shortForm']
		staff = staf['staff']
		subjectName = staf['subjectName']
		url = staf['url']
		year = staf['year']
		csv << [id, shortForm, staff, subjectName, url, year]
	end
end

puts "csv uploading is completed"