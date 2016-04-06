var tuneles_norma = 
{
	"RT":7,
	"ELONG":"80/40",
	"RCBR":"1,5",
	"KPLANO":"0,1",
	"GEOTESAN":"NT-15"
};

var tuneles_gtxtl = 
{
	"RT":"9,5",
	"ELONG":"57,23",
	"RCBR":"1,56",
	"KPLANO":"0,1",
	"GEOTESAN":"NT-15"
};


$(document).ready(function() {
	$('#rt-geotexan-value').val(tuneles_norma['RT']);
	$('#elong-geotexan-value').val(tuneles_norma['ELONG']);
	$('#cbr-geotexan-value').val(tuneles_norma['RCBR']);
	$('#kplano-geotexan-value').val(tuneles_norma['KPLANO']);
	$('#rt-geotextil-value').val(tuneles_gtxtl['RT']);
	$('#elong-geotextil-value').val(tuneles_gtxtl['ELONG']);
	$('#cbr-geotextil-value').val(tuneles_norma['RCBR']);
	$('#kplano-geotextil-value').val(tuneles_gtxtl['KPLANO']);
	$('#product').val(tuneles_gtxtl['GEOTESAN']);
});