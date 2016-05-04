/*
* Determina el cálculo solicitado y abre el HTML de justificación del cálculo
* con los valores obtenidos y el producto recomendado.
*/
$(document).ready(function() {
    $('#just').click(function() {
        var url = window.location.href;
        var basename = url.split("/").pop();
        var desturl = url.replace(basename, basename.replace("#", "")).replace("/calculos/", "/just/");
        console.log(desturl);
    });
});
