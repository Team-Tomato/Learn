require 'open-uri'
require 'json'
url='https://newsapi.org/v2/everything?q=bitcoin&apiKey=686c3ccc5253489b872d84a96db5e5d4'
req=open(url)
response=req.read
data_hash=JSON.parse(response)
result=data_hash["articles"]
result.each do |post|
	puts "Author: #{post['author']},\nTitle: #{post['title']},\nDescription: #{post['descripition']},\nUrl: #{post['url']}"
	puts "___________________________________________________________________________________________________________________________"
end
