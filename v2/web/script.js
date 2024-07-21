setInterval(start, 2000)

function display(results) {
    text = ""
    for (i in results[0]) {
        content = results[0][i][1][0]

        // Pixel Position
        /* 
        x = (results[0][i][0][3][0]/results[1][0]) * window.outerWidth
        y = (results[0][i][0][0][1]/results[1][1]) * window.outerHeight
        text += `<p style=\"position:absolute;left:${x}px;top:${y}px;\">${content}</p>`
        */
        
        // Percentage Position  -> get exact position; only works on original screen
        x = (results[0][i][0][3][0]/results[1][0]) * 100
        y = (results[0][i][0][0][1]/results[1][1]) * 100
        text += `<p style=\"position:absolute;left:${x}%;top:${y}%;\">${content}</p>`
    }
    document.getElementById("text").innerHTML = text    
}

function start() {
    fetch("./output/result.json").then(result => result.json()).then(result => display(result))
}
