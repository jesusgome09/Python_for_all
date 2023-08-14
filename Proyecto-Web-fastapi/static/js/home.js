fetch('/ahome')
    .then(response => {
        if (!response.ok) {
            throw new Error(`Error al realizar la solicitud: ${response.status} ${response.statusText}`);
        }
        return response.json();
    })

    .then(data => {
        // Aquí puedes utilizar los datos obtenidos de la API
        console.log("Datos obtenidos:", data);

        document.querySelector('.title').textContent = data.titulo;

        document.querySelector('.mensaje').textContent = data.mensaje;

        document.querySelector('.creator').textContent = data.creador;

    })
    .catch(error => {
        console.error("Error:", error);
        console.log("No se encuentra la API")
    });
