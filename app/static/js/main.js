$(document).ready(function() {
  employees = fetchEmployeesData()
})


function fetchEmployeesData() {
  fetch('/employees')
    .then(response => response.json()
      .then(result => setEmplTableHtml(result)))
    .then(data => console.log(data))
}

function setEmplTableHtml(employees) {
  let tableHtml = ""
  employees.map(e => tableHtml += "<tr><td><button type='button' class='btn btn-light' onclick=\"selectEmployee('" + e.email + "')\"><i class='fa fa-search fa-2' ></i></button></td><td>" + e.name + "</td><td>" + e.surname + "</td><td>" + e.email + "</td><td>" + e.role + "</td></tr>")
  $('#employee-table-body').append(tableHtml)
  $('#employee-table').DataTable()
}

function selectEmployee(email){
  fetch('/employees/'+email)
    .then(
      response => response.json()
      .then(result => populateEmployeeCard(result))
    )
    .then(
      data => console.log(data)
    )
}

function populateEmployeeCard(employee){
  document.getElementById('empl-name').innerHTML = employee.name + " " + employee.surname
  document.getElementById('empl-data').innerHTML = employee.email + " - " + employee.role
  let skillsHtml = ""
  employee.skills.map(e => skillsHtml += "<li class='list-group-item'>" + e.skill_name + "</li>")
  document.getElementById('empl-skills').innerHTML = skillsHtml
}
