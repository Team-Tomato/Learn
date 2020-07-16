Rails.application.routes.draw do
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
  namespace :api do
    namespace :v1 do
      resource :arithmetic do
        get 'add', to: "arithmetic#add"
        get 'sub', to: "arithmetic#sub"
        get 'mul', to: "arithmetic#mul"
        get 'div', to: "arithmetic#div"
      end
    end
  end
end
