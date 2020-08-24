class UsersController < ApplicationController
  def index
  @users = User.all
  render json: @users, status: :ok
  end
  
  def create
  	@user = User.new(user_params)

  	if @user.save
  		render json: @user, status: :created 
  	else
  	  render json: { errors: @user.errors.full_messages, status: 404, message:"Not Created" } 
    end 
    
   end 

  private
  def user_params
    params.permit(:name,:phone,:email,:city,:state,:pin)
  end
end
