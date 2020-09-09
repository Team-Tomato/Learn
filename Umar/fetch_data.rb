

require 'net/http'
require 'json'
require 'csv'

url = 'https://teamtomato.herokuapp.com/api/v1/question'
uri = URI(url)
response = Net::HTTP.get(uri)
data=JSON.parse(response)

#puts response
#hashes = [{'a' => 'aaaa', 'b' => 'bbbb'}]
column_names = data.first.keys
s=CSV.generate do |csv|
  csv << column_names
  data.each do |x|
    csv << x.values
  end
end
File.write('the_file.csv', s)

CSV.foreach ('the_file.csv') do |row|
  puts row.inspect
end