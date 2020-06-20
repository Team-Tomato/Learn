require 'net/http'
require 'json'
url = 'https://teamtomato.herokuapp.com/api/v1/question'
req = URI(url)
response = Net::HTTP.get(req)
result=JSON.parse(response)
=begin
result.each do |data|
	puts "id:#{data['id']}, shortForm:#{data['shortForm']}, staffname:#{data['staff']}, subjectname:#{data['subjectName']}, Url:#{data['url']}, year:#{data['year']}\n"
end
=end
=begin
puts "enter the id :"
ins_id=gets.chomp().to_i
result.each do |data|
	if ins_id == data['id']
		puts "id:#{data['id']}, shortForm:#{data['shortForm']}, staffname:#{data['staff']}, subjectname:#{data['subjectName']}, Url:#{data['url']}, year:#{data['year']}\n"
	end
end
=end
puts "enter the shortform :"
ins_form=gets.chomp()
result.each do |data|
	if ins_form == data['shortForm']
		puts "id:#{data['id']}, shortForm:#{data['shortForm']}, staffname:#{data['staff']}, subjectname:#{data['subjectName']}, Url:#{data['url']}, year:#{data['year']}\n"
	end
end
