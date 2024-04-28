$(document).ready(function () {
    var selectedInterests = [];
    var selectedCategories = [];
    var messageTimer;

    // Lista de intereses
    var interests = [
        'Artes', 'Música', 'Deportes', 'Karaoke', 'Moda', 'Fotografía', 'Maquillaje', 'Escribir',
        'Dibujar', 'Pintar', 'Anime', 'Baile', 'Comida y bebida', 'Bienestar y fitness', 'Coches', 'Videojuegos',
        'Leer', 'Películas', 'Boxeo', 'K-pop', 'Manualidades', 'Fútbol', 'Acuario', 'Baloncesto', 'Negocios',
        'Jardinería', 'Poesía', 'Redes Sociales', 'Viajar', 'Caminar', 'Intercambio de idiomas', 'E-Sports',
        'Cosplay', 'Motociclismo', 'Carreras de bicicleta', 'Astrología', 'Tatuajes', 'Repostería', 'Inversiones',
        'Automovilismo', 'Creación de contenido', 'Actividades al aire libre', 'Acampar', 'Artes Marciales',
        'Ballet', 'Skateboarding', 'Programar', 'Senderismo', 'Voleibol', 'Blogger'
    ];

    var categorias = ['Casual', 'Viajes', 'Experiencias extremas', 'Videojuegos', 'Cosplay', 'Turismo', 'Actividades al aire libre', 'Bienestar y fitnnes', 'Deporte', 'Eventos sociales', 'Gastronomia', 'Voluntariados', 'Arte y cultura', 'Aventuras', 'Aprendizaje', 'Formal'];

    function showMessage(message) {
        $('#messageBox').text(message).show();
        messageTimer = setTimeout(function () {
            hideMessage();
        }, 3000);
    }

    function hideMessage() {
        $('#messageBox').hide();
    }
    // Función para generar la lista de intereses
    function generateInterestsList() {
        var interestsList = $('#interestsList');
        interestsList.empty();
        var row;
        var colCount = 0;
        interests.slice(0, 16).forEach(function (interest, index) {
            if (index % 4 === 0) {
                row = $('<div class="row"></div>');
                interestsList.append(row);
            }
            var isChecked = selectedInterests.includes(interest) ? 'checked' : '';
            row.append('<div class="col-md-3"><div class="form-check"><input type="checkbox" class="form-check-input interest-checkbox" value="' + interest + '" ' + isChecked + '> <label class="form-check-label">' + interest + '</label></div></div>');
            colCount++;
            if (colCount === 4) {
                colCount = 0;
            }
        });
    }

    // Función para generar la lista de categorías
    function generateCategoriesList() {
        var categoriesList = $('#categoriesList');
        categoriesList.empty();
        var row;
        var colCount = 0;
        categorias.forEach(function (category, index) {
            if (index % 4 === 0) {
                row = $('<div class="row"></div>');
                categoriesList.append(row);
            }
            var isChecked = selectedCategories.includes(category) ? 'checked' : '';
            row.append('<div class="col-md-3"><div class="form-check"><input type="checkbox" class="form-check-input category-checkbox" value="' + category + '" ' + isChecked + '> <label class="form-check-label">' + category + '</label></div></div>');
            colCount++;
            if (colCount === 4) {
                colCount = 0;
            }
        });
    }

    // Generar la lista de intereses y categorías al cargar la página
    generateInterestsList();
    generateCategoriesList();

    // Función para contar los checkboxes seleccionados
    function countChecked() {
        var checked = $('.interest-checkbox:checked').length;
        return checked;
    }

    // Función para actualizar los intereses seleccionados
    function updateSelectedInterests(interest, checked) {
        if (checked) {
            if (selectedInterests.length < 5) {
                selectedInterests.push(interest);
            } else {
                showMessage("¡Ya has seleccionado 5 intereses!");
                $('.interest-checkbox[value="' + interest + '"]').prop('checked', false);
            }
        } else {
            var index = selectedInterests.indexOf(interest);
            if (index !== -1) {
                selectedInterests.splice(index, 1);
            }
        }
        displaySelectedInterests();
    }

    // Función para actualizar las categorías seleccionadas
    function updateSelectedCategories(category, checked) {
        if (checked) {
            if (selectedCategories.length < 5) {
                selectedCategories.push(category);
            } else {
                showMessage("¡Ya has seleccionado 5 categorías!");
                $('.category-checkbox[value="' + category + '"]').prop('checked', false);
            }
        } else {
            var index = selectedCategories.indexOf(category);
            if (index !== -1) {
                selectedCategories.splice(index, 1);
            }
        }
    }

    // Función para mostrar los intereses seleccionados
    function displaySelectedInterests() {
        var selectedInterestsDiv = $('#selectedInterests');
        selectedInterestsDiv.empty();
        selectedInterests.forEach(function (interest) {
            selectedInterestsDiv.append('<span style="padding-top:5px;" class="badge badge-primary mr-2 mb-2">' + interest + '<button type="button" class="close" data-interest="' + interest + '" style="color: white; margin-top: -8px;"><span aria-hidden="true">&times;</span></button></span>');
        });
        // Evento de clic en el botón "x" para quitar el interés seleccionado
        selectedInterestsDiv.find('.close').click(function () {
            var interestToRemove = $(this).data('interest');
            var index = selectedInterests.indexOf(interestToRemove);
            if (index !== -1) {
                selectedInterests.splice(index, 1);
                displaySelectedInterests();
                // Desmarcar el checkbox correspondiente
                $('.interest-checkbox[value="' + interestToRemove + '"]').prop('checked', false);
            }
        });
    }

    // Función para filtrar los intereses al buscar
    function filterInterestsList(query) {
        var filteredInterests = interests.filter(function (interest) {
            return interest.toLowerCase().indexOf(query.toLowerCase()) !== -1;
        });
        generateInterestsListFromData(filteredInterests);
    }

    // Función para generar la lista de intereses a partir de los datos filtrados
    function generateInterestsListFromData(data) {
        var interestsList = $('#interestsList');
        interestsList.empty();
        var row;
        var colCount = 0;
        data.forEach(function (interest, index) {
            if (index % 4 === 0) {
                row = $('<div class="row"></div>');
                interestsList.append(row);
            }
            var isChecked = selectedInterests.includes(interest) ? 'checked' : '';
            row.append('<div class="col-md-3"><div class="form-check"><input type="checkbox" class="form-check-input interest-checkbox" value="' + interest + '" ' + isChecked + '> <label class="form-check-label">' + interest + '</label></div></div>');
            colCount++;
            if (colCount === 4) {
                colCount = 0;
            }
        });
    }

    // Función para filtrar los intereses al buscar
    $('#searchInput').on('keyup', function () {
        var query = $(this).val();
        if (query === '') {
            generateInterestsList();
        } else {
            filterInterestsList(query);
        }
    });

    // Evento de cambio en los checkboxes de intereses
    $(document).on('change', '.interest-checkbox', function () {
        var interest = $(this).val();
        var checked = $(this).is(':checked');
        updateSelectedInterests(interest, checked);
    });

    // Evento de cambio en los checkboxes de categorías
    $(document).on('change', '.category-checkbox', function () {
        var category = $(this).val();
        var checked = $(this).is(':checked');
        updateSelectedCategories(category, checked);
    });

    function hideMessage() {
        $('#messageBox').hide();
        clearTimeout(messageTimer); // Cancelar el temporizador
    }
    // Evento de clic en el botón Continuar
    $('#continueBtn').click(function () {
        if (selectedInterests.length === 0) {
            showMessage("Por favor, selecciona al menos 1 interés");
        }
        if (selectedCategories.length === 0) {
            showMessage("Por favor, selecciona al menos 1 categoría.");
        }
        else {
            console.log("Intereses seleccionados:", selectedInterests);
            console.log("Categorías seleccionadas:", selectedCategories);
            // Aquí puedes agregar cualquier otra acción que desees realizar cuando el usuario continúe
        }
    });
});
