class CalController < ApplicationController
      before_action :validation
      before_action :div_by_zero,only:  :div
def add
  @num1=params[:n1].to_i
  @num2=params[:n2].to_i
  @add=@num1 + @num2
  render json: {message: "sum of #{@num1} and #{@num2} is #{@add}"}
end

def sub
  @num1=params[:n1].to_i
  @num2=params[:n2].to_i
  @sub=@num1 - @num2
  render json: {message: "Difference between #{@num1} and #{@num2} is #{@sub}"}
end

def mul
   @num1=params[:n1].to_i
   @num2=params[:n2].to_i
   @mul=@num1 * @num2
   render json: {message: "product of #{@num1} and #{@num2} is #{@mul}"}
 end

 def div
   @num1=params[:n1].to_i
   @num2=params[:n2].to_i
   @div=@num1 / @num2
   render json: {message: "The remainder of #{@num1} by #{@num2} is #{@div}"}
 end

 private
  def validation
    if !(params[:n1].present? && params[:n2].present?)
   render json: {message: "verify your inputs"}
end

end

def div_by_zero
    if params[:n2].to_i==0
      render json: { message: "denominato can't be zero"}
    end
  end
end
