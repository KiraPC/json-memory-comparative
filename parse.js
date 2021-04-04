const fs = require('fs');

function printMemory() {
    const used = process.memoryUsage().heapUsed / 1024 / 1024;
    console.log(`${Math.round(used * 100) / 100} MB`);
}

printMemory() // 2.47 MB
file = fs.readFileSync('huge.json')
printMemory() // 2.82 MB

json = JSON.parse(file)

console.log(json['type']) // FeatureCollection
printMemory() // 47.92 MB
