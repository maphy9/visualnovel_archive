const titles = ['Clannad', 'Saya no Uta', 'K-On'];

async function main() {
    for (const title of titles) {
        let body = { title, };
        let res = await fetch(
            'http://127.0.0.1:8000/get_visualnovel/',
            {
                method: "POST",
                headers: {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(body),
            }
        );
        if (res.status == 406) {
            console.log(`Error: Not found ("${title}")`);
            continue;
        }
        const data = await res.json();
        console.dir(data);
    }
}

main();