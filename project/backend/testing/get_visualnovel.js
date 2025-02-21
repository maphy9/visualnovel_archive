const url = 'http://127.0.0.1:8000/get_visualnovel/';
const method = 'POST';
const headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
};
const titles = ["Clannad", "Saya no Uta", "To Heart", "Sora no Sakura"];

const main = async () => {
    for (const title of titles) {
        console.log(`Title: ${title}`);
        const body = JSON.stringify({ title });
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