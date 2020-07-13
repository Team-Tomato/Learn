Rails.application.routes.draw do
	
  get 'cal/add' ,to:"cal#add"
  get 'cal/sub' ,to:"cal#sub"
  get 'cal/mul' ,to:"cal#mul"
  get 'cal/div' ,to:"cal#div"
  
end
