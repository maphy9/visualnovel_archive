const url = 'http://127.0.0.1:8000/create_publisher/';
const method = 'POST';
const headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
};
const names = ["Leaf", "  Key      ", "Sekai Games", "key", "NITRO PLUS"];

const main = async () => {
    for (const name of names) {
        console.log(`Name: ${name}`);
        const body = JSON.stringify({ name });
        const res = await fetch(url, { method, headers, body });
        if (res.status != 200) {
            console.log(`Status code ${res.status}`);
            continue;
        }
        console.log('Successfully created');
    }
};

main();