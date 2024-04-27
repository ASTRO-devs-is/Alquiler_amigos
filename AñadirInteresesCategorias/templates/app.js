function mostrarSeleccion() {
    const selectedInterests = Array.from(document.querySelectorAll('input[type="checkbox"]:checked'))
        .map(input => input.nextElementSibling.textContent);
    const selectedCategories = Array.from(document.querySelectorAll('input[type="checkbox"]:checked'))
        .map(input => input.nextElementSibling.textContent);
    const message = `Intereses seleccionados: ${selectedInterests.join(', ')}\nCategorías seleccionadas: ${selectedCategories.join(', ')}`;
    alert(message);
}