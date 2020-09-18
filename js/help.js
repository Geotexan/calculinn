/*
 * http://www.w3schools.com/howto/howto_css_modals.asp
 */

function set_real_width_from_img(element, img_element) {
    /* http://stackoverflow.com/questions/318630/get-real-image-width-and-height-with-javascript-in-safari-chrome */
    var pic_real_width, pic_real_height;
    $("<img/>") // Make in memory copy of image to avoid css issues
        .attr("src", $(img_element).attr("src"))
        .load(function() {
            pic_real_width = this.width;   // Note: $(this).width() will not
            pic_real_height = this.height; // work for in memory images.
            // Ver calculinn.css. Se le agrega 16 de padding.
            var ancho = pic_real_width + 16*2;
            element.style.width = ancho + "px";
    });
}

function ver_imagen_ayuda(){
    /*
     * Busca el diagrama (fichero .png) de ayuda correspondiente al
     * cálculo actual y lo muestra en una ventana emergente.
     * También hace visibles los rangos permitidos.
     */
    var elementos = document.getElementsByClassName("rango");
    for (var i = 0; i < elementos.length; i++) {
        elementos[i].style.visibility = "visible";
    }

    var url = window.location.href;
    var filename = url.split('/').pop();
    var imgsrc = "../images/calculos/" + filename.replace(".html", ".png");
    var img = document.createElement("img");
    img.setAttribute("src", imgsrc);
    img.setAttribute("alt", "Diagrama de ayuda de parámetros.");
    img.setAttribute("id", "diagrama");
    var modal_body = document.getElementById("modal-body");
    // Solo lo agrego una vez:
    var diagrama = document.getElementById("diagrama");
    if (!diagrama){
        modal_body.appendChild(img);
    }
    // Ajusto el modal-content al ancho de la imagen:
    var modal_content = document.getElementById("modal-content");
    set_real_width_from_img(modal_content, img);

    // Get the modal
    var modal = document.getElementById('myModal');

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks on the button, open the modal
    modal.style.display = "block";

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    };

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
}
