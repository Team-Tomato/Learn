require 'net/http'
require 'json'
require 'csv'
url = 'https://teamtomato.herokuapp.com/api/v1/question'
uri = URI(url)
response = Net::HTTP.get(uri)
csv_string = CSV.generate do |csv|
  JSON.parse(response).each do |hash|
    csv << hash.values
  end
end

File.write("data.csv", csv_string)