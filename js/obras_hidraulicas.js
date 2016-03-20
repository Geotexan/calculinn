var obras = 
{
	"data1" : {
		"CBR" : "test",
		"Espesor" : "test",
		"Tam_Esc" : "test",
		"Caida_esc" : "test",
		"Geotexan" : { "RT" : "VALUE", "ELONG" : "VALUE", "RCBR" : "VALUE", "PERF_CONO" : "VALUE", "AB_CONO" : "VALUE", "KVERT" : "VALUE"},
		"Geotextil" : { "RT" : "VALUE", "ELONG" : "VALUE", "RCBR" : "VALUE", "PERF_CONO" : "VALUE", "AB_CONO" : "VALUE", "KVERT" : "VALUE"},
		"GEOTESAN" : "NT-VALUE"
	}
};

function calcula() {
	var icbr = $('#i-cbr').val();
	var ie = $('#i-e').val();
	var itam_esc = $('#i-tam-esc').val();
	var icaida_esc = $('#i-caida-esc').val();

	$.each(obras, function(i, item) {
		if (obras[i]['CBR'] == icbr ) {
			if (obras[i]['Espesor'] == ie) {
				if (obras[i]['Tam_Esc'] == itam_esc) {
					if (obras[i]['Caida_esc'] == icaida_esc) {
						//Relleno valores del formulario y salgo de la iteración
						$('#rt-geotexan-value').val(obras[i]['Geotexan']['RT']);
						$('#elong-geotexan-value').val(obras[i]['Geotexan']['ELONG']);
						$('#cbr-geotexan-value').val(obras[i]['Geotexan']['RCBR']);
						$('#perfcono-geotexan-value').val(obras[i]['Geotexan']['PERF_CONO']);
						$('#abcono-geotexan-value').val(obras[i]['Geotexan']['AB_CONO']);
						$('#kvert-geotexan-value').val(obras[i]['Geotexan']['KVERT']);
						$('#rt-geotextil-value').val(obras[i]['Geotextil']['RT']);
						$('#elong-geotextil-value').val(obras[i]['Geotextil']['ELONG']);
						$('#cbr-geotextil-value').val(obras[i]['Geotextil']['RCBR']);
						$('#perfcono-geotextil-value').val(obras[i]['Geotextil']['PERF_CONO']);
						$('#abcono-geotextil-value').val(obras[i]['Geotextil']['AB_CONO']);
						$('#kvert-geotextil-value').val(obras[i]['Geotextil']['KVERT']);
						$('#product').val(obras[i]['GEOTESAN']);
						return true;
					}
				}
			}
		}
	});
}