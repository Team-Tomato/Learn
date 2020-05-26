
// Api calls to fetch empolyees
fetch('http://dummy.restapiexample.com/api/v1/employees')
  .then(response => {
    return response.json()
  })
  .then(data => {
    console.log(data)
  })
  .catch(err => {
    console.log(err)
})