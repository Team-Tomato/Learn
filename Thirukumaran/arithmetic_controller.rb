class ArithmeticController < ApplicationController
def message
	render json: {message: "hello,there"}
	
end
def add
	@num1=23
	@num2=43
	render json: {message:"the sum is #{@num1+@num2}"}	
end
def sub
	@num1=23
	@num2=43
	render json: {message:"the sum is #{@num1-@num2}"}	
end
def mul
	@num1=23
	@num2=43
	render json: {message:"the sum is #{@num1*@num2}"}	
end	
def div
	@num1=23
	@num2=43
	render json: {message:"the sum is #{@num1/@num2}"}	
end
end

