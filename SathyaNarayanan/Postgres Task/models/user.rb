class User < ApplicationRecord
	validates :name,:phone,:email,:city,:pin , presence:true
	validates :email, format: {with: /.*@.*/ }
	validates :state , length: { minimum: 2}
	validates :phone,:pin , numericality: {only_integer:true, message:"letters not allowed "}
end
