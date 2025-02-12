const genre_names_array = ["horror", "eroge", "fantasy", "nakige"];
const page_size = 4;
const page_number = 1;

async function main() {
    for (const genre_name of genre_names_array) {
        const body = { genre_name, page_size, page_number };
        const res = await fetch(
            'http://127.0.0.1:8000/get_visualnovels_by_genre/',
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
            console.log(`Error: Not found ("${genre_name}")`);
            continue;
        }
        const data = await res.json();
        console.log(data);
    }
}

main();