Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  get 'cal/add' ,to:"cal#add"
  get 'cal/sub' ,to:"cal#sub"
  get 'cal/mul' ,to:"cal#mul"
  get 'cal/div' ,to:"cal#div"
end
