class User < ApplicationRecord

  validates :name, :email, :state, :city, :pincode, presence: true
  validates :phone_no, presence: true, numericality: { only_integer: true }, length: { in: 10..15 }
  validates :pincode, presence: true, numericality: { only_integer: true }
  validates :email, format: { with: /(\A([a-z]*\s*)*\<*([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]{2,})\>*\Z)/i }, uniqueness: true

end
