/*
* Determina el cálculo solicitado y abre el HTML de justificación del cálculo
* con los valores obtenidos y el producto recomendado.
*/
$(document).ready(function() {
    $('#just').click(function() {
        var url = window.location.href;
        var basename = url.split("/").pop();
        var desturl = url.replace(basename, basename.replace("#", "")).replace("/calculos/", "/just/");
        var params = ["pg3_elon", "gtx_elon", "pg3_trac", "gtx_trac", "pg3_cono", "gtx_cono", "pg3_poro", "gtx_poro", "gtx_nt"];
        var params_values = [];
        for (var param in params){
        	params_values.push(params[param] + "=" + param);
        }
        desturl += "?" + params_values.join("&");
        //console.log(desturl);
        window.location.href = desturl;
    });
});
