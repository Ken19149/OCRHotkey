fetch("./output/result.json").then(result => result.json()).then(result => display(result))

function display(results) {
    text = ""
    for (i in results[0]) {
        content = results[0][i][1][0]
        x = results[0][i][0][3][0]
        y = results[0][i][0][0][1]
        text += `<p style=\"position:absolute;left:${x}px;top:${y}px;\">${content}</p>`
    }

    document.getElementById("text").innerHTML = text
}