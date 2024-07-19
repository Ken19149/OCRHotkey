fetch("./output/result.json").then(result => result.json()).then(result => display(result))

function display(results) {
    text = ""
    for (i in results[0]) {
        content = results[0][i][1][0]
        left = results[0][i][0][3][0]
        top = results[0][i][0][3][1]
        text += `<p style=\"position:absolute;left:${left};top:${top};\">${content}</p>`
    }
    console.log(results)
    document.getElementById("text").innerHTML = text
    
}