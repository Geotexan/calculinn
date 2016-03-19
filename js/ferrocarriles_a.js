var ferrocarriles = 
{
	"ADIF" : { "RT" : "VALUE", "ELONG" : "VALUE", "CBR": "VALUE", "KVERT" : "VALUE" },
	"Geotextil" : {"RT" : "VALUE", "ELONG" : "VALUE", "CBR": "VALUE", "KVERT" : "VALUE"},
	"GEOTESAN" : "NT-VALUE"
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