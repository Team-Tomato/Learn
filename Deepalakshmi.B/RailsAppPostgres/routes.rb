Rails.application.routes.draw do
  resources :users, only: [:index, :create]
  get 'users/index', to:'users#index'
  get 'users/create',to:'users#create'
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
end
