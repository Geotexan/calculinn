/*
* Determina el cálculo solicitado y abre el HTML de justificación del cálculo
* con los valores obtenidos y el producto recomendado.
*/
$(document).ready(function() {
    $('#just').click(function() {
        var url = window.location.href;
        var basename = url.split("/").pop();
        var desturl = url.replace(basename, basename.replace("#", "")).replace("/calculos/", "/just/");
        // TODO: En vez de HARDODED, recorrer el DOM y rescatar todo lo que empiece por ref_, gtx_ o prouct.
        var params = ["ref_E", "gtx_E", "ref_Rt", "gtx_Rt", "ref_R_perf__Cono", "gtx_R_perf__Cono", "ref_Abertura_poro", "gtx_Abertura_poro", "product"];
        var params_values = [];
        for (var param in params){
        	// TODO: En lugar del índice numérico param, el valor del span que está contenido en el div.
        	var valor = param;
        	params_values.push(params[param] + "=" + valor);
        }
        desturl += "?" + params_values.join("&");
        //console.log(desturl);
        window.location.href = desturl;
    });
});
