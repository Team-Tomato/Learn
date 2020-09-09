require 'news-api'

newsapi = News.new("0630ee9a73044403bf6d17b49500d47d")             

top_headlines = newsapi.get_top_headlines(language: 'en',country: 'in')

puts (json: top_headlines)