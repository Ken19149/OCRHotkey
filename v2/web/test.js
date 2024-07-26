function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

pixel = []
text = ""
async function demo() {
    await sleep(250)
    let elements = document.getElementById("text")
    let p = elements.querySelectorAll("p")
    for (i=0; i < p.length; i++) {
        pixel.push(p[i].getBoundingClientRect().height)
        console.log(i, p[i].getBoundingClientRect().height)
    }
    console.log(pixel)
    for (i=0; i < pixel.length; i++) {
        text += `(${i},${pixel[i]}),`
    }
    console.log(text)
}

demo();

