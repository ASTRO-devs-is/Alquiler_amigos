// Función para alternar la visibilidad de la contraseña
function togglePasswordVisibility() {
  var passwordInput = document.getElementById("contrasena");
  var toggleIcon = document.getElementById("togglePasswordIcon");
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    toggleIcon.classList.remove("fa-eye");
    toggleIcon.classList.add("fa-eye-slash");
  } else {
    passwordInput.type = "password";
    toggleIcon.classList.remove("fa-eye-slash");
    toggleIcon.classList.add("fa-eye");
  }
}

// Función para validar campos antes de enviar el formulario
document.getElementById("registroForm").addEventListener("submit", function (event) {
  var telefonoInput = document.getElementById("telefono").value;
  var emailInput = document.getElementById("email").value;
  var descripcionInput = document.getElementById("descripcion").value;
  var contrasenaInput = document.getElementById("contrasena").value;
  var generoInputs = document.querySelectorAll('input[name="genero"]:checked');
  var ciudadInput = document.getElementById("ciudad").value;
  var paisInput = document.getElementById("pais").value;
  var localidadInput = document.getElementById("localidad").value;
  var nombreInput = document.getElementById("nombre").value;
  var apellidoInput = document.getElementById("apellido").value;

  // Validar que los campos no estén vacíos
  if (!telefonoInput || !emailInput || !descripcionInput || !contrasenaInput || generoInputs.length !== 1 ||
    !ciudadInput || !paisInput || !localidadInput || !nombreInput || !apellidoInput) {
    alert("Todos los campos son obligatorios");
    event.preventDefault(); // Detener el envío del formulario
    return;
  }

  // Validar género (debe haber seleccionado solo uno)
  if (generoInputs.length !== 1) {
    alert("Seleccione un género");
    event.preventDefault();
    return;
  }

  // Ejemplo de validación de longitud de descripción
  if (descripcionInput.length < 50) {
    alert("La descripción debe tener al menos 50 caracteres");
    event.preventDefault();
    return;
  }
});

// Función para redirigir a la página principal
function redirigirPaginaPrincipal() {
  window.location.href = "Inicio"; // Reemplaza "URL_DE_LA_PAGINA_PRINCIPAL" con la URL correcta
}

// Agrega un evento onclick al botón cancelar que llame a la función redirigirPaginaPrincipal
document.querySelector('.cancel-button').addEventListener('click', redirigirPaginaPrincipal);

// Función para validar que el contenido no sea solo números
function validarNoSoloNumeros(input) {
  let contenido = input.value.trim();
  if (/\D/.test(contenido)) {
    // El contenido tiene al menos un carácter que no es un número, no hacemos nada
  } else {
    // Mostrar un mensaje de error o tomar la acción que consideres adecuada
    alert(`El campo ${input.id} no debe contener solo números.`);
    // Puedes también limpiar el contenido del input si lo prefieres
    input.value = '';
  }
}

// Función para validar el nombre
function validarNombre(elemento) {
  const nombreInput = elemento.value.trim();
  const soloLetras = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/; // Expresión regular para letras y espacios
  
  if (!soloLetras.test(nombreInput)) {
    document.getElementById('nombreError').textContent = 'El nombre debe contener solo letras y espacios';
    elemento.classList.add('is-invalid');
  } else {
    document.getElementById('nombreError').textContent = '';
    elemento.classList.remove('is-invalid');
  }
}

// Función para validar el apellido
function validarApellido(elemento) {
  const apellidoInput = elemento.value.trim();
  const soloLetras = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/; // Expresión regular para letras y espacios
  
  if (!soloLetras.test(apellidoInput)) {
    document.getElementById('apellidoError').textContent = 'El apellido debe contener solo letras y espacios';
    elemento.classList.add('is-invalid');
  } else {
    document.getElementById('apellidoError').textContent = '';
    elemento.classList.remove('is-invalid');
  }
}

// Función para validar la ubicación (país, ciudad, localidad)
function validarUbicacion(elemento) {
  const ubicacionInput = elemento.value.trim();
  const soloLetras = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/; // Expresión regular para letras y espacios
  
  if (!soloLetras.test(ubicacionInput)) {
    elemento.nextElementSibling.textContent = 'Este campo debe contener solo letras y espacios';
    elemento.classList.add('is-invalid');
  } else {
    elemento.nextElementSibling.textContent = '';
    elemento.classList.remove('is-invalid');
  }
}
