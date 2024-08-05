setInterval(start, 300)

// start()

function display(results) {
    text = ""
    // results = 100
    for (i in results[0]) {
    // for (let i=0;i<=100;i++) {

        content = results[0][i][1][0]

        // Pixel Position - old
        /* 
        x = (results[0][i][0][3][0]/results[1][0]) * window.outerWidth
        y = (results[0][i][0][0][1]/results[1][1]) * window.outerHeight
        text += `<p style=\"position:absolute;left:${x}px;top:${y}px;\">${content}</p>`
        */
        
        // Percentage Position  -> get exact position; only works on original screen - current
        
        x = (results[0][i][0][3][0]/results[1][0]) * 100
        y = (results[0][i][0][0][1]/results[1][1]) * 100

        text_height = results[0][i][0][3][1] - results[0][i][0][0][1]   // yBottom - yTop
        font_size = text_height/1.25 // 1.22 = constant
        text += `<p style=\"position:absolute;left:${x}%;top:${y}%;font-size:${font_size}px;\">${content}</p>`

        // test
        /*
        content = "test1234ABC@!#テスト嗚呼啊啊"
        font_size = i
        text += `<p style=\"font-size:${font_size}px;\">${content} - ${i}</p>`
        */

    }
    document.getElementById("text").innerHTML = text    
}

function start() {
    fetch("./output/result.json").then(result => result.json()).then(result => display(result))
}
