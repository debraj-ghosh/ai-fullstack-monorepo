const BASE_URL = import.meta.env.VITE_API_URL;

export async function getHello() {
    const response = await fetch(`${BASE_URL}/api/hello`);

    if (!response.ok) {
        throw new Error("Failed to fetch");
    }

    return response.json();
}

export async function saveUser(userData = { name: "Debraj" }) {
    const response = await fetch(`${BASE_URL}/api/user`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(userData)
    });

    if (!response.ok) {
        throw new Error("Failed to save user");
    }

    return response.json();
}