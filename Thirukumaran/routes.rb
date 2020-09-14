Rails.application.routes.draw do
 
 get 'arithmetic/message', to: "arithmetic#message"
 get 'arithmetic/add', to: "arithmetic#add"
get 'arithmetic/sub', to: "arithmetic#sub"
get 'arithmetic/mul', to: "arithmetic#mul"
get 'arithmetic/div', to: "arithmetic#div"
end
