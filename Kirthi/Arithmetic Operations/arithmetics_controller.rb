class ArithmeticsController < ApplicationController
  before_action :check_validation
  before_action :check_divisible, only: :div

  def add
    @num1 = params[:num1].to_i
    @num2 = params[:num2].to_i
    @sum = @num1 + @num2
    render json: {message: "Addition: #{@sum}", status: :ok}
  end

  def sub
    @num1 = params[:num1].to_i
    @num2 = params[:num2].to_i
    @sub = @num1 - @num2
    render json: {message: "Subtraction: #{@sub}", status: :ok}
  end

  def mul
    @num1 = params[:num1].to_i
    @num2 = params[:num2].to_i
    @mul =  @num1 * @num2
    render json: {message: "Multiplication: #{@mul}", status: :ok}
  end

  def div
    @num1 = params[:num1].to_i
    @num2 = params[:num2].to_i
    @div = @num1 / @num2
    render json: {message: "Division: #{@div}", status: :ok}
  end

  private
  def check_validation
      render json: { status: 404, message: "Invalid Input" } unless params[:num1].present? && params[:num2].present?
  end

  def check_divisible
    render json: {status: 404, message: "Invalid Input"} unless params[:num2].present? && params[:num2].to_i != 0
  end
end
