Rails.application.routes.draw do
	resources :users, only: [:index, :create]
  get 'users/index', to:'users#index'
  get 'users/create',to:'users#create'
 end