// x/web/app.js

// Function to initialize the WebSocket connection
function initWebSocket() {
    // Create a new WebSocket connection
    const socket = new WebSocket("ws://localhost:6789");

    // Event handler for when the connection is opened
    socket.onopen = () => {
        console.log("WebSocket connection opened");
    };

    // Event handler for when a message is received from the server
    socket.onmessage = (event) => {
        const dataDisplay = document.getElementById("dataDisplay");
        // Display the received message in the HTML element
        dataDisplay.innerText = event.data;
    };

    // Event handler for when the connection is closed
    socket.onclose = () => {
        console.log("WebSocket connection closed");
    };

    // Event handler for when an error occurs
    socket.onerror = (error) => {
        console.error("WebSocket error:", error);
    };
}

// Initialize the WebSocket connection when the page loads
window.onload = initWebSocket;
