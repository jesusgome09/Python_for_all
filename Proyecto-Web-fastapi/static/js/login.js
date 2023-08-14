document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".form")

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Evita el envío del formulario normal

        const username = form.querySelector('input[name="username"]').value;
        const password = form.querySelector('input[name="password"]').value;

        const data = {
            username: username,
            password: password
        };

        fetch("/alogin", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(result => {
                // Aquí puedes manejar la respuesta de la API
                console.log(result);
            })
            .catch(error => {
                console.error("Error:", error);
            });
    });
});
