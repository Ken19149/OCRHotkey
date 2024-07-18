fetch("./output/result.json").then(result => result.json()).then(result => display(result))

function display(result) {
    console.log(result)
}