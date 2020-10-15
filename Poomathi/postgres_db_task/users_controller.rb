class Api::V1::UsersController < ApplicationController

  def create
    @user = User.new(user_params)
    if @user.save
      render json: @user, status: :created
    else
      render json: { errors: @user.errors.full_messages },
              status: :unprocessable_entity
    end
  end

  def index
    @users = User.all
    render json: @users, status: :ok
  end
  
  def user_params
    params.permit(
       :name, :email, :state, :city, :pincode, :phone_no
    )
  end
end
