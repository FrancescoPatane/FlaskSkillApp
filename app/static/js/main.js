$(document).ready(function() {
  employees = fetchEmployeesData()
});


function fetchEmployeesData() {
  fetch('/employees')
    .then(response => response.json()
      .then(result => setEmplTableHtml(result)))
    .then(data => console.log(data))
}

function setEmplTableHtml(employees) {
  let tableHtml = ""
  employees.map(e => tableHtml += "<tr><td><i class='fa fa-search fa-2'></i></td><td>" + e.name + "</td><td>" + e.surname + "</td><td>" + e.email + "</td><td>" + e.role + "</td></tr>")
  $('#employee-table-body').append(tableHtml)
  $('#employee-table').DataTable()
}
