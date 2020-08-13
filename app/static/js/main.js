
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
