// Obtener referencias a los elementos relevantes
const estilosClaros = document.getElementById('estilos-claros');
const estilosOscuros = document.getElementById('estilos-oscuros');
const botonModoDark = document.getElementById('modo-dark');
const botonModoLight = document.getElementById('modo-light');

// Función para cambiar al modo oscuro
function activarModoOscuro() {
    estilosClaros.disabled = true;
    estilosOscuros.disabled = false;
    // Agregar clases de estilo para modo oscuro si es necesario
    document.body.classList.add('modo-oscuro');

    // Aplicar estilos oscuros a la navbar y el footer
    document.querySelector('.navbar').classList.add('modo-oscuro');
    document.querySelector('.footer').classList.add('modo-oscuro');
    document.querySelector('.navbar-toggler-icon').classList.add('modo-oscuro');
}

// Función para cambiar al modo claro
function activarModoClaro() {
    estilosClaros.disabled = false;
    estilosOscuros.disabled = true;
    // Eliminar clases de estilo para modo oscuro si es necesario
    document.body.classList.remove('modo-oscuro');

     // Aplicar estilos claros a la navbar y el footer
     document.querySelector('.navbar').classList.remove('modo-oscuro');
     document.querySelector('.footer').classList.remove('modo-oscuro');
     document.querySelector('.navbar-toggler-icon').classList.remove('modo-oscuro');
}

// Agregar manejadores de clic a los botones
botonModoDark.addEventListener('click', activarModoOscuro);
botonModoLight.addEventListener('click', activarModoClaro);

