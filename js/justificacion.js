/*
 * Determina el cálculo solicitado y abre el HTML de justificación del cálculo
 * con los valores obtenidos y el producto recomendado.
 */
$(document).ready(function() {
    $('#just').click(function() {
        var url = window.location.href;
        var basename = url.split("/").pop();
        var desturl = url.replace(basename, basename.replace("#", "")).replace("/calculos/", "/just/");
        // Selector múltiple por expresión regular. Lista de ids a pasar.
        var selectors = $("div[id^='ref_'],div[id^='gtx_'],div[id='product'],input[id^='in'],select[id^='in']");
        var params = selectors.map(function() {
        	return this.id;
		}).get();
		// Lista de "valores" de esos ids.
		var params_values = [];
		for (var param in params){
			var selector = '#'.concat(params[param]);
			// Primero lo intento como si fuera un desplegable:
        	var valor = $(selector.concat(" option:selected")).text();
        	// Porque en un desplegable el valor .text() da cosas raras.
        	// Después ya lo intento como campo de texto normal y como numérico.
        	if (! valor){
        		valor = $(selector).text();
        		//console.log(valor);
        	}
        	if (! valor){
        		valor = $(selector).val();
        		//console.log(valor);
        	}
        	params_values.push(params[param] + "=" + valor);
        }
        desturl += "?" + params_values.join("&");
        //console.log(desturl);
        window.location.href = desturl;
    });
});
