Rails.application.routes.draw do
  get 'add', to: "arithmetics#add"
  get 'sub', to: "arithmetics#sub"
  get 'mul', to: "arithmetics#mul"
  get 'div', to: "arithmetics#div"
end
