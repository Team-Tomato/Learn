require 'open-uri'
require 'json'
url='https://newsapi.org/v2/everything?q=bitcoin&apiKey=13e947e28cfd488cb8064dd30cf81010'
req=open(url)
response=req.read
data_hash=JSON.parse(response)
result=data_hash["articles"]

result.each do |post|
  puts "Source Name:#{post['source']},Title:#{post['title']},Description: #{post['description']},url: #{post['url']}"
  puts "----------"
end
