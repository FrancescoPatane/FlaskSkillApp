
function fetchSkillsData() {
  fetch('/skills')
    .then(response => response.json()
      .then(result => setSkillTableHtml(result)))
    .then(data => console.log(data))
}

function setSkillTableHtml(skills) {
  let tableHtml = ""
  skills.map(e => tableHtml += "<tr><td><button type='button' class='btn btn-light' onclick=\"selectSkill('" + e.name + "', '" + e.description + "')\"><i class='fa fa-search fa-2' ></i></button></td><td>" + e.name + "</td></tr>")
  document.getElementById('skill-table-body').innerHTML = tableHtml
  $('#skill-table').DataTable()
}

function selectSkill(name, description){
  fetch('/skills/'+name+"/employees")
    .then(
      response => response.json()
      .then(result => populateSkillCard(name, description, result))
    )
    .then(
      data => console.log(data)
    )
}

function populateSkillCard(skill, description, employees){
  document.getElementById('skill-name').innerHTML = skill
  document.getElementById('skill-descr').innerHTML = description
  let employeesHtml = ""
  employees.map(e => employeesHtml += "<li class='list-group-item'>" + e.name + " " + e.surname + " " + getSkillLevelBadge(e.level) + "</li>")
  document.getElementById('skill-employees').innerHTML = employeesHtml
}

function getSkillLevelBadge(level){
  let style = ""
  switch (level) {
    case 'High':
      style = "style= 'background-color: green;color: white'"
      break
    case 'Medium':
      style = "style= 'background-color: cadetblue;color: white'"
      break
    case 'Low':
      style = "style= 'background-color: orange;color: white'"
      break
  }
  let html = "<span class='badge float-right' " + style + ">" + level + "</span>"
  return html
}


fetchSkillsData()
