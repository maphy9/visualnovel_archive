const user_id_array = [1, 2];

for (const user_id of user_id_array) {
    const body = { user_id, };
    const res = await fetch(
        'http://127.0.0.1:8000/get_user_info/',
        {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify(body),
        }
    );

    if (res.status == 200) {
        const data = await res.json();
        console.dir(data);
    } else {
        console.log(`Not found (user_id=${user_id})`)
    }
}