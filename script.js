function iniciarJuego() {
    // Obtener los valores del formulario
    const nombreJugador = document.getElementById('nombre').value;
    const dificultadJuego = document.getElementById('dificultad').value;
    const colorPielJugador = document.getElementById('color_piel').value;
    const colorPeloJugador = document.getElementById('color_pelo').value;
    const nombreMundo = document.getElementById('nombre_mundo').value;

    // Aquí puedes almacenar la información en algún lugar o procesarla según sea necesario

    // Abrir la nueva ventana con el menú de inicio
    abrirMenuInicio();
}

function abrirMenuInicio() {
    document.body.innerHTML = '';  // Limpiar el contenido de la página actual

    // Crear el menú de inicio
    const menuVentana = document.createElement('div');
    menuVentana.className = 'ventana';

    const titulo = document.createElement('h2');
    titulo.textContent = 'Menú de Inicio';
    menuVentana.appendChild(titulo);

    const opciones = ['Jugar', 'Configuraciones', 'Salir'];
    opciones.forEach(opcion => {
        const boton = document.createElement('button');
        boton.textContent = opcion;
        boton.onclick = () => alert(`Seleccionaste: ${opcion}`);
        menuVentana.appendChild(boton);
        menuVentana.appendChild(document.createElement('br'));
    });

    document.body.appendChild(menuVentana);
}
