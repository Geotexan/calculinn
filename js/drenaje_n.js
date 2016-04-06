var drenajes_n = [
  {
    "Trafico":"T0",
    "E":"2,7",
    "RT":9,
    "RPERF_CONO":30,
    "AB_PORO":"0,05 – 0,2",
    "GEOTESAN":"NT-15"
  },
  {
    "Trafico":"T1",
    "E":"2,1",
    "RT":7,
    "RPERF_CONO":35,
    "AB_PORO":"0,05 – 0,2",
    "GEOTESAN":"NT-12"
  },
  {
    "Trafico":"T2",
    "E":"1,5",
    "RT":5,
    "RPERF_CONO":40,
    "AB_PORO":"0,05 – 0,2",
    "GEOTESAN":"NT-10"
  },
  {
    "Trafico":"T3",
    "E":"1,2",
    "RT":4,
    "RPERF_CONO":45,
    "AB_PORO":"0,05 – 0,2",
    "GEOTESAN":"NT-10"
  }
];

var drenajes_g  = [
  {
    "Trafico":"T0",
    "E":"57,23",
    "RT":"9,5",
    "RPERF_CONO":"28,66",
    "AB_PORO":"0,061",
    "GEOTESAN":"NT-15"
  },
  {
    "Trafico":"T1",
    "E":"55,87",
    "RT":"8",
    "RPERF_CONO":"34,04",
    "AB_PORO":"0,068",
    "GEOTESAN":"NT-12"
  },
  {
    "Trafico":"T2",
    "E":"55,19",
    "RT":"6",
    "RPERF_CONO":"39",
    "AB_PORO":"0,075",
    "GEOTESAN":"NT-10"
  },
  {
    "Trafico":"T3",
    "E":"55,19",
    "RT":"6",
    "RPERF_CONO":"39",
    "AB_PORO":"0,075",
    "GEOTESAN":"NT-10"
  }
];

var inputs = 
{
	"Filtracion" : "Filtracion",
};

$(document).ready(function() {
	$('#funcion').val(inputs['Filtracion']);
});

function calcula() {
	var trafico = $('#trafico').val();
	$.each(drenajes_n, function(i, item) {
		if (drenajes_n[i]['Trafico'] == trafico ) {
			//Relleno valores del formulario y salgo de la iteración
			$('#e-normativa-value').val(drenajes_n[i]['E']);
			$('#rt-normativa-value').val(drenajes_n[i]['RT']);
			$('#rperf-normativa-value').val(drenajes_n[i]['RPERF_CONO']);
			$('#abertura-poro-normativa-value').val(drenajes_n[i]['AB_PORO']);
			$('#e-geotexan-value').val(drenajes_g[i]['E']);
			$('#rt-geotexan-value').val(drenajes_g[i]['RT']);
			$('#rperf-geotexan-value').val(drenajes_g[i]['RPERF_CONO']);
			$('#abertura-poro-geotexan-value').val(drenajes_g[i]['AB_PORO']);
			$('#product').val(drenajes_g[i]['GEOTESAN']);
			return true;
		}
	});
}