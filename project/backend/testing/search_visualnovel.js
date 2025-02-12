const phrases = ["clan", "saYa", "Soro", "clAnNaD", "a", ""];

async function main() {
    for (const phrase of phrases) {
        const body = { phrase, };
        const res = await fetch(
            'http://127.0.0.1:8000/search_visualnovel/',
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
            console.log(`\n\nError: Not found ("${phrase}")\n\n`);
            continue;
        }
        const data_set = await res.json();
        for (const data of data_set) {
            console.dir(data);
        }
    }
}

main();