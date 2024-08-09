function display(results) {
    results = JSON.parse(results)
    text = ""
    for (i in results[0]) {

        content = results[0][i][1][0]

        x = (results[0][i][0][3][0]/results[1][0]) * 100
        y = (results[0][i][0][0][1]/results[1][1]) * 100

        text_height = results[0][i][0][3][1] - results[0][i][0][0][1]   // yBottom - yTop
        font_size = text_height/1.22 // 1.22 = approximate constant
        text += `<p style=\"position:absolute;left:${x}%;top:${y}%;font-size:${font_size}px;\">${content}</p>`

    }
    document.getElementById("text").innerHTML = text    
}


function initWebSocket() {
    const socket = new WebSocket("ws://localhost:6789");

    socket.onopen = () => {
        console.log("WebSocket connection opened");
    };

    socket.onmessage = (event) => {
        // console.log(event.data)
        display(event.data)
    };

    socket.onclose = () => {
        console.log("WebSocket connection closed");
    };

    socket.onerror = (error) => {
        console.error("WebSocket error:", error);
    };
}

// Initialize the WebSocket connection when the page loads
window.onload = initWebSocket;
