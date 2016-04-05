var ferrocarriles = 
{
	"ADIF" : { "RT" : "8 – 10,1", "ELONG" : "50 – 55", "CBR": "1,56", "KVERT" : "4,9" },
	"Geotextil" : {"RT" : "20", "ELONG" : "60", "CBR": "3,25", "KVERT" : "74"},
	"GEOTESAN" : "NT-25"
};
var inputs = 
{
	"Funcion" : "Separación",
	"Aplicacion": "Ferrocarriles en Plataforma"
};

$(document).ready(function() {
	$('#funcion').val(inputs['Funcion']);
	$('#aplicacion').val(inputs['Aplicacion']);
	$('#rt-adif-value').val(ferrocarriles['ADIF']['RT']);
	$('#elong-adif-value').val(ferrocarriles['ADIF']['ELONG']);
	$('#cbr-adif-value').val(ferrocarriles['ADIF']['CBR']);
	$('#kvert-adif-value').val(ferrocarriles['ADIF']['KVERT']);
	$('#rt-geotextil-value').val(ferrocarriles['Geotextil']['RT']);
	$('#elong-geotextil-value').val(ferrocarriles['Geotextil']['ELONG']);
	$('#cbr-geotextil-value').val(ferrocarriles['Geotextil']['CBR']);
	$('#kvert-geotextil-value').val(ferrocarriles['Geotextil']['KVERT']);
	$('#product').val(ferrocarriles['GEOTESAN']);
});