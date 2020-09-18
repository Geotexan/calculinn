/*
 * Determina el cálculo solicitado y abre el HTML del pliego de condiciones
 * con los valores obtenidos y el producto recomendado.
 */
$(document).ready(function() {
    $('#conds').click(function() {
        var url = window.location.href;
        var basename = url.split("/").pop();
        var desturl = url.replace(basename, basename.replace("#", "")).replace("/calculos/", "/conds/");
        // Selector múltiple por expresión regular. Lista de ids a pasar.
        var selectors = $("div[id^='gtx_']");
        var params = selectors.map(function() {
        return this.id;
		}).get();
		// Lista de "valores" de esos ids.
		var params_values = [];
		for (var param in params){
			var selector = '#'.concat(params[param]);
      		var valor = $(selector).text();
        	//console.log(valor);
        	params_values.push(params[param] + "=" + valor);
        }
        desturl += "?" + params_values.join("&");
        //console.log(desturl);
        window.location.href = desturl;
    });
});
