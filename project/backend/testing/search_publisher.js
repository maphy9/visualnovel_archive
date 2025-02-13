const url = 'http://127.0.0.1:8000/search_publisher/';
const method = 'POST';
const headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
};
const count = 5;
const phrases = ["Leaf", "  Key      ", "Sekai Games", "key", "NITRO PLUS", ""];

const main = async () => {
    for (const phrase of phrases) {
        console.log(`Phrase: ${phrase}`);
        const body = JSON.stringify({ phrase, count });
        const res = await fetch(url, { method, headers, body });
        if (res.status != 200) {
            console.log(`Status code ${res.status}`);
            continue;
        }
        const data = await res.json();
        console.dir(data);
    }
};

main();