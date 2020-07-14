class OperationController < ApplicationController
   before_action :validation,only: [:addition, :subraction, :multiplication, :division]
   before_action :div_zero,only: :division

    def welcomepage
      render json: "welcome to the calculator\nhere you can perform arithmetic operation
      \n1.addition-/api/v1/arithmetic/add?num1=&num2=\n2.subraction-/api/v1/arithmetic/sub?"\
      "num1=&num2=\n3.multiplication-/api/v1/arithmetic/mul?num1=&num2=\n4.division-"\
      "/api/v1/arithmetic/div?num1=&num2="
    end

    def addition
      @num1=params[:num1].to_i
      @num2=params[:num2].to_i
      @sum=@num1+@num2
      render json: {status: :ok,message: "the sum of #{@num1} and #{@num2} is #{@sum}"}
    end

    def subraction
      @num1=params[:num1].to_i
      @num2=params[:num2].to_i
      @diff=@num1-@num2
      render json: {status: :ok,message: "the difference of #{@num1} and #{@num2} is #{@diff}"}
    end

    def multiplication
      @num1=params[:num1].to_i
      @num2=params[:num2].to_i
      @mul=@num1*@num2
      render json: {status: :ok,message: "the product of #{@num1} and #{@num2} is #{@mul}"}
    end

    def division
      @num1=params[:num1].to_f
      @num2=params[:num2].to_f
      @div=(@num1/@num2)
      render json: {status: :ok,message: "the division of #{@num1.to_i} and #{@num2.to_i} is #{@div}"}
    end

private
    def validation
      if (params[:num1].blank?||params[:num2].blank?)
        render json: {status:404,message:"input must be filled!"}
      end
    end
    def div_zero
      if (params[:num2].to_i==0)
        render json: {status:404,message:"mathematical error"}
      end
     end
end
