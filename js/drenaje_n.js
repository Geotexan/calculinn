var drenajes = {
	"data1" : {
		"Trafico" : "T0",
		"Normativa" : { "E" : "2.7", "RT" : "9", "PERF_CONO" : "30", "AB_PORO" : "0.5-0.2"},
		"Geotexan" : { "E" : "2.7", "RT" : "9", "PERF_CONO" : "30", "AB_PORO" : "0.5-0.2"},
		"GEOTESAN" : "NT-15"
	},
	"data2" : {
		"Trafico" : "T1",
		"Normativa" : { "E" : "2.1", "RT" : "7", "PERF_CONO" : "35", "AB_PORO" : "0.5-0.2"},
		"Geotexan" : { "E" : "2.1", "RT" : "7", "PERF_CONO" : "35", "AB_PORO" : "0.5-0.2"},
		"GEOTESAN" : "NT-12"
	},
	"data3" : {
		"Trafico" : "T2",
		"Normativa" : { "E" : "1.5", "RT" : "5", "PERF_CONO" : "40", "AB_PORO" : "0.5-0.2"},
		"Geotexan" : { "E" : "1.5", "RT" : "5", "PERF_CONO" : "40", "AB_PORO" : "0.5-0.2"},
		"GEOTESAN" : "NT-10"
	},
	"data4" : {
		"Trafico" : "T3",
		"Normativa" : { "E" : "1.2", "RT" : "4", "PERF_CONO" : "45", "AB_PORO" : "0.5-0.2"},
		"Geotexan" : { "E" : "1.2", "RT" : "4", "PERF_CONO" : "45", "AB_PORO" : "0.5-0.2"},
		"GEOTESAN" : "NT-10"
	}

};

var inputs = 
{
	"Filtracion" : "Filtracion",
};

$(document).ready(function() {
	$('#funcion').val(inputs['Filtracion']);
});

function calcula() {
	var trafico = $('#trafico').val();
	$.each(drenajes, function(i, item) {
		if (drenajes[i]['Trafico'] == trafico ) {
			//Relleno valores del formulario y salgo de la iteración
			$('#e-normativa-value').val(drenajes[i]['Normativa']['E']);
			$('#rt-normativa-value').val(drenajes[i]['Normativa']['RT']);
			$('#rperf-normativa-value').val(drenajes[i]['Normativa']['PERF_CONO']);
			$('#abertura-poro-normativa-value').val(drenajes[i]['Normativa']['AB_PORO']);
			$('#e-geotextil-value').val(drenajes[i]['Geotexan']['E']);
			$('#rt-geotextil-value').val(drenajes[i]['Geotexan']['RT']);
			$('#rperf-geotextil-value').val(drenajes[i]['Geotexan']['PERF_CONO']);
			$('#abertura-poro-geotextil-value').val(drenajes[i]['Geotexan']['AB_PORO']);
			$('#product').val(drenajes[i]['GEOTESAN']);
			return true;
		}
	});
}