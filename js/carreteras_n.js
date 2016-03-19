var carreteras = 
{
	"data1" : {
		"Trafico": "T0",
		"Funcion" : "SEPARACION", 
		"PG3" : { "ELONG": "6.4", "RT" : "16", "PERF_CONO" : "20", "AB_PORO": "0.05-0.2"},
		"Geotexan" : { "ELONG": "8.92", "RT" : "16", "PERF_CONO" : "18.65", "AB_PORO": "0.06"},
		"GEOTESAN" : "NT-21"
		},
	"data2" : {
		"Trafico": "T0",
		"Funcion" : "FILTRACION", 
		"PG3" : { "ELONG": "2.7", "RT" : "9", "PERF_CONO" : "30", "AB_PORO": "0.05-0.2"},
		"Geotexan" : { "ELONG": "5.2", "RT" : "9.16", "PERF_CONO" : "25.28", "AB_PORO": "0.061"},
		"GEOTESAN" : "NT-17"
		},
	"data3" : {
		"Trafico": "T1",
		"Funcion" : "SEPARACION", 
		"PG3" : { "ELONG": "4.8", "RT" : "12", "PERF_CONO" : "25", "AB_PORO": "0.05-0.2"},
		"Geotexan" : { "ELONG": "6.44", "RT" : "12", "PERF_CONO" : "21.93", "AB_PORO": "0.061"},
		"GEOTESAN" : "NT-18"
		},
	"data4" : {
		"Trafico": "T1",
		"Funcion" : "FILTRACION", 
		"PG3" : { "ELONG": "2.1", "RT" : "7", "PERF_CONO" : "35", "AB_PORO": "0.05-0.2"},
		"Geotexan" : { "ELONG": "3.98", "RT" : "7.12", "PERF_CONO" : "34.04", "AB_PORO": "0.068"},
		"GEOTESAN" : "NT-12"
		},
	"data5" : {
		"Trafico": "T2",
		"Funcion" : "SEPARACION", 
		"PG3" : { "ELONG": "3.2", "RT" : "8", "PERF_CONO" : "30", "AB_PORO": "0.05-0.2"},
		"Geotexan" : { "ELONG": "4.58", "RT" : "8", "PERF_CONO" : "28.66", "AB_PORO": "0.061"},
		"GEOTESAN" : "NT-15"
		},
	"data6" : {
		"Trafico": "T2",
		"Funcion" : "FILTRACION", 
		"PG3" : { "ELONG": "1.5", "RT" : "5", "PERF_CONO" : "40", "AB_PORO": "0.05-0.2"},
		"Geotexan" : { "ELONG": "2.96", "RT" : "5.36", "PERF_CONO" : "39", "AB_PORO": "0.075"},
		"GEOTESAN" : "NT-10"
		},
	"data7" : {
		"Trafico": "T3",
		"Funcion" : "SEPARACION", 
		"PG3" : { "ELONG": "2.4", "RT" : "6", "PERF_CONO" : "35", "AB_PORO": "0.05-0.2"},
		"Geotexan" : { "ELONG": "3.98", "RT" : "7.12", "PERF_CONO" : "34.04", "AB_PORO": "0.068"},
		"GEOTESAN" : "NT-12"
		},
	"data8" : {
		"Trafico": "T3",
		"Funcion" : "FILTRACION", 
		"PG3" : { "ELONG": "1.2", "RT" : "4", "PERF_CONO" : "45", "AB_PORO": "0.05-0.2"},
		"Geotexan" : { "ELONG": "2.96", "RT" : "5.36", "PERF_CONO" : "39", "AB_PORO": "0.075"},
		"GEOTESAN" : "NT-10"
		}
};

function calcula() {
	var trafico = $('#trafico').val();
	var filtracion = $('#filtracion').val();
	$.each(carreteras, function(i, item) {
		if (carreteras[i]['Trafico'] == trafico ) {
			if (carreteras[i]['Funcion'] == filtracion) {
				//Relleno valores del formulario y salgo de la iteración
				$('#e-calculo-value').val(carreteras[i]['PG3']['RT']);
				$('#rt-calculo-value').val(carreteras[i]['PG3']['ELONG']);
				$('#rperf-calculo-value').val(carreteras[i]['PG3']['PERF_CONO']);
				$('#abertura-poro-calculo-value').val(carreteras[i]['PG3']['AB_PORO']);
				$('#e-geotextil-value').val(carreteras[i]['Geotexan']['RT']);
				$('#rt-geotextil-value').val(carreteras[i]['Geotexan']['ELONG']);
				$('#rperf-geotextil-value').val(carreteras[i]['Geotexan']['PERF_CONO']);
				$('#abertura-poro-geotextil-value').val(carreteras[i]['Geotexan']['AB_PORO']);
				$('#product').val(carreteras[i]['GEOTESAN']);
				return true;
			}
		}
	});
}