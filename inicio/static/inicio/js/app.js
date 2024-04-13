const dropArea = document.querySelector(".drag-area");
const dragText = dropArea.querySelector("header");
const button = dropArea.querySelector("button");
const input = dropArea.querySelector("input");
const previewContainer = document.getElementById('preview-container');
const cargarBtn = document.querySelector('.cargar-button');
const cancelarBtn = document.querySelector('.cancel-button');
const uploadForm = document.getElementById('upload-form');
const MAX_IMAGENES = 5;
let selectedFiles = [];
    
// Agregar la funcionalidad para arrastrar y soltar archivos
dropArea.addEventListener("dragover", (event) => {
    event.preventDefault();
    dropArea.classList.add("drag-over");
    dragText.textContent = "Suelta para cargar";
});
    
dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("drag-over");
    dragText.textContent = "Arrastra las fotos aquí";
});
    
dropArea.addEventListener("drop", (event) => {
    event.preventDefault();
    dropArea.classList.remove("drag-over");
    dragText.textContent = "Arrastra las fotos aquí";
    const files = event.dataTransfer.files;
    console.log("Archivos recibidos");
    handleFiles(files);
});
    
// Agregar la funcionalidad al botón de buscar fotos
    button.onclick = () => {
    input.click();
}
    
// Manejar los archivos seleccionados
input.addEventListener("change", (event) => {
            const files = event.target.files;
            handleFiles(files);
        });
    
        // Función para manejar los archivos
        function handleFiles(files) {
            const validFiles = Array.from(files).filter(isValidFile);
        
            // Verificar duplicados en la lista actual de archivos seleccionados
            const duplicatesInSelected = validFiles.filter(file =>
                selectedFiles.some(f => f.name === file.name && f.size === file.size)
            );
        
            // Verificar duplicados en la lista de archivos a agregar
            const duplicatesToAdd = validFiles.filter((file, index) =>
                validFiles.some((f, i) => i !== index && f.name === file.name && f.size === file.size)
            );
        
            if (duplicatesInSelected.length > 0 || duplicatesToAdd.length > 0) {
                showMessage("Solo se permite subir una vez la misma imagen.", "error");
                return;
            }
        
            if (validFiles.length + previewContainer.children.length > MAX_IMAGENES) {
                showMessage(`Solo se permiten seleccionar hasta ${MAX_IMAGENES} imágenes.`, "error");
                return;
            }
        
            validFiles.forEach(file => {
                selectedFiles.push(file);
                const reader = new FileReader();
                reader.onload = () => {
                    const imgContainer = document.createElement("div"); // Crear un contenedor para la imagen y el botón de eliminar
                    imgContainer.classList.add("img-container"); // Agregar una clase CSS para estilos
        
                    const img = document.createElement("img");
                    img.src = reader.result;
                    img.classList.add('img-preview');
        
                    const removeBtn = document.createElement("span");
                    removeBtn.textContent = "X";
                    removeBtn.classList.add("remove-btn");
                    removeBtn.addEventListener("click", () => {
                        imgContainer.remove(); // Eliminar el contenedor completo
                        selectedFiles = selectedFiles.filter(f => f !== file);
                        updateFilesAndPreview();
                    });
        
                    imgContainer.appendChild(img); // Agregar la imagen al contenedor
                    imgContainer.appendChild(removeBtn); // Agregar el botón de eliminar al contenedor
                    previewContainer.appendChild(imgContainer); // Agregar el contenedor al contenedor de previsualización
                };
                reader.readAsDataURL(file);
                });        
                updateFilesAndPreview();
            }
            function showMessage(message, type) {
                const messageContainer = document.getElementById("message-container");
                messageContainer.innerHTML = `<div class="${type}-message">${message}</div>`;
                // Limpia el mensaje después de unos segundos
                setTimeout(() => {
                    messageContainer.innerHTML = "";
                }, 5000); // 5000 milisegundos = 5 segundos
            }
            // Función para validar archivos
            function isValidFile(file) {
                const validExtensions = ['jpg', 'png','jpeg'];
                const invalidExtensions = ['docx', 'pptx', 'xlsx','pdf'];
                const fileExtension = file.name.split('.').pop().toLowerCase();
                const isValidFormat = validExtensions.includes(fileExtension);
                const isInvalidFormat = invalidExtensions.includes(fileExtension);
                const isValidSize = file.size <= 3000000; // 3MB
                
                if (isInvalidFormat) {
                    alert("Solo se permiten imágenes en formato JPG y PNG.");
                    return false;
                }

                if (!isValidSize) {
                    alert(`Solo se permite imágenes de peso de 3 MB.`);
                }

                return isValidFormat && isValidSize;
            }
    
            // Función para actualizar archivos y previsualización
            function updateFilesAndPreview() {
                cargarBtn.disabled = selectedFiles.length === 0;
                // Agregar los archivos seleccionados al formulario
                const formData = new FormData(uploadForm);
                selectedFiles.forEach(file => {
                    formData.append('file-input', file);
                });
            }
    
            cargarBtn.addEventListener('click', () => {

                if (selectedFiles.length === 0) {
                    alert('No se han seleccionado archivos para cargar.');
                    return;
                }
    
                confirmAction('¿Está seguro de cargar las imágenes?', () => {
                    const formData = new FormData(uploadForm);
                    selectedFiles.forEach(file =>{
                        formData.append('file-input', file);
                    });
                    fetch("{% url 'cargar_fotos_perfil' %}", {
                        method: 'POST',
                        body: formData
                    })
                    .then(response => {
                        if (response.ok) {
                            return response.json();
                        } else {
                            throw new Error('Error al cargar las imágenes');
                        }
                    })
                    .then(data => {
                        if (data.success) {
                            alert('Las imágenes se han cargado correctamente.');
                            window.location.href = "{% url 'exito' %}";
                        } else {
                            alert('Error al cargar las imágenes');
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        alert('Error al cargar las imágenes');
                    });
                });

            });
        
            cancelarBtn.addEventListener('click', () => {
                confirmAction('¿Está seguro de cancelar?', () => {
                    uploadForm.reset();
                    previewContainer.innerHTML = '';
                    selectedFiles = [];
                    updateFilesAndPreview();
                });
            });
    
            // Función de confirmación para eventos click
            function confirmAction(message, action) {
                return new Promise((resolve, reject) => {
                    const dialog = document.createElement('dialog');
                    dialog.innerHTML = `
                        <div class="dialog-container">
                            <p>${message}</p>
                            <div class="buttons">
                                <button class="button-primary" id="confirm-button">Sí</button>
                                <button class="button-secondary" id="cancel-button">No</button>
                            </div>
                        </div>
                    `;

                    document.body.appendChild(dialog);
        
                    const confirmButton = dialog.querySelector('#confirm-button');
                const cancelButton = dialog.querySelector('#cancel-button');
        
            confirmButton.addEventListener('click', () => {
                dialog.close();
                resolve(true);
                action();
            });
        
            cancelButton.addEventListener('click', () => {
                dialog.close();
                resolve(false);
            });
            dialog.showModal();
        });
    }