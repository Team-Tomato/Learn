Rails.application.routes.draw do
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
    root "operation#welcomepage"
    get 'api/v1/arithmetic/add', to: "operation#addition"
    get 'api/v1/arithmetic/sub', to: "operation#subraction"
    get 'api/v1/arithmetic/mul', to: "operation#multiplication"
    get 'api/v1/arithmetic/div', to: "operation#division"
  end
