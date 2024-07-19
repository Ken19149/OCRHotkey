fetch("./output/result.json").then(result => result.json()).then(result => display(result))

function display(results) {
    for (i in results[0]) {
        console.log(results[0][i][1][0])
    }
    
}