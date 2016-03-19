var ferrocarriles = 
{
	"data1" : {
		"CBR" : "l1",
		"Espesor" : "400",
		"DMax" : "l150",
		"Geotexan": {"RT" : "16", "ELONG" : "50", "RCBR" : "2600", "KVERT": ">25"},
		"Geotextil" : {"RT" : "16", "ELONG" : "55.76", "RCBR" : "2700", "KVERT": "76.68"},
		"GEOTESAN" : "NT-23"
	},
	"data2" : {
		"CBR" : "l1",
		"Espesor" : "400",
		"DMax" : "ge150-l300",
		"Geotexan": {"RT" : "20", "ELONG" : "50", "RCBR" : "3300", "KVERT": ">25"},
		"Geotextil" : {"RT" : "20", "ELONG" : "57.64", "RCBR" : "3310", "KVERT": "69.55"},
		"GEOTESAN" : "NT-30"
	},
	"data3" : {
		"CBR" : "l1",
		"Espesor" : "ge200-l400",
		"DMax" : "l150",
		"Geotexan": {"RT" : "17", "ELONG" : "50", "RCBR" : "3000", "KVERT": ">25"},
		"Geotextil" : {"RT" : "17.7", "ELONG" : "58.92", "RCBR" :  "3020", "KVERT": "74.16"},
		"GEOTESAN" : "NT-25"
	},
	"data4" : {
		"CBR" : "ge1",
		"Espesor" : "400",
		"DMax" : "l150",
		"Geotexan": {"RT" : "16", "ELONG" : "50", "RCBR" : "2600", "KVERT": ">25"},
		"Geotextil" : {"RT" : "16", "ELONG" : "55.76", "RCBR" : "2700", "KVERT": "78.68"},
		"GEOTESAN" : "NT-23"
	},
	"data5" : {
		"CBR" : "ge1",
		"Espesor" : "400",
		"DMax" : "ge150-l300",
		"Geotexan": {"RT" : "16", "ELONG" : "50", "RCBR" : "2600", "KVERT": ">25"},
		"Geotextil" : {"RT" : "16", "ELONG" : "55.76", "RCBR" : "2700", "KVERT": "78.68"},
		"GEOTESAN" : "NT-23"
	},
	"data6" : {
		"CBR" : "ge1",
		"Espesor" : "ge200-l400",
		"DMax" : "l150",
		"Geotexan": {"RT" : "16", "ELONG" : "50", "RCBR" : "2600", "KVERT": ">25"},
		"Geotextil" : {"RT" : "16", "ELONG" : "55.76", "RCBR" : "2700", "KVERT": "78.68"},
		"GEOTESAN" : "NT-23"
	},
	"data7" : {
		"CBR" : "ge1",
		"Espesor" : "ge200-l400",
		"DMax" : "ge150-l300",
		"Geotexan": {"RT" : "19", "ELONG" : "50", "RCBR" : "3000", "KVERT": ">25"},
		"Geotextil" : {"RT" : "20", "ELONG" : "57.64", "RCBR" : "3310", "KVERT": "69.55"},
		"GEOTESAN" : "NT-25"
	},
	"data8" : {
		"CBR" : "ge1",
		"Espesor" : "ge450-l600",
		"DMax" : "ge300-l400",
		"Geotexan": {"RT" : "21", "ELONG" : "50", "RCBR" : "3800", "KVERT": ">25"},
		"Geotextil" : {"RT" : "21.13", "ELONG" : "57.91", "RCBR" :  "3930", "KVERT": "63.28"},
		"GEOTESAN" : "NT-35"
	},
	"data9" : {
		"CBR" : "ge1",
		"Espesor" : "ge600-l750",
		"DMax" : "ge400-l500",
		"Geotexan": {"RT" : "24", "ELONG" : "50", "RCBR" : "4400", "KVERT": ">15"},
		"Geotextil" : {"RT" : "25.2", "ELONG" : "58.17", "RCBR" : "4490", "KVERT": "49.96"},
		"GEOTESAN" : "NT-40"
	},
	"data10" : {
		"CBR" : "ge1",
		"Espesor" : "ge750-l900",
		"DMax" : "ge500-l600",
		"Geotexan": {"RT" : "27", "ELONG" : "50", "RCBR" : "5100", "KVERT": ">15"},
		"Geotextil" : {"RT" : "27.92", "ELONG" : "57.82", "RCBR" : "5260", "KVERT": "43.38"},
		"GEOTESAN" : "NT-46"
	},
	"data10" : {
		"CBR" : "ge1",
		"Espesor" : "ge900",
		"DMax" : "ge600",
		"Geotexan": {"RT" : "30", "ELONG" : "50", "RCBR" : "6000", "KVERT": ">15"},
		"Geotextil" : {"RT" : "31.52", "ELONG" : "63.11", "RCBR" :  "6490", "KVERT": "40.84"},
		"GEOTESAN" : "NT-58"
	}
};


function calcula() {
	var icbr = $('#i-cbr').val();
	var ie = $('#i-e').val();
	var id = $('#i-d').val();

	//Storage interval from the input
	var cbr;
	var e;
	var d;

	if (icbr < 1) {
		cbr = "l1";
	} else if (icbr >= 1) {
		cbr = "ge1";
	}

	if (ie < 200) {
		alert("E debe ser mayor o igual a 200");
		return false;
	} else if (ie >=200 && ie < 400) {
		e = "ge200-l400";
	} else if (ie = 400) {
		e = "400";
	} else {
		alert('No hay información para este valor de E');
		return false;
	}

	if (id < 150) {
		d = "l150";
	} else if (id >= 150 && id < 300) {
		d = "ge150-l300";
	} else if (id >= 300) {
		alert("D debe ser menor que 300");
		return false;
	}

	$.each(ferrocarriles, function(i, item) {
		if (ferrocarriles[i]['CBR'] == cbr ) {
			if (ferrocarriles[i]['Espesor'] == e) {
				if (ferrocarriles[i]['DMax'] == d) {
					//Relleno valores del formulario y salgo de la iteración
					$('#rt-geotexan-value').val(ferrocarriles[i]['Geotexan']['RT']);
					$('#elong-geotexan-value').val(ferrocarriles[i]['Geotexan']['ELONG']);
					$('#cbr-geotexan-value').val(ferrocarriles[i]['Geotexan']['RCBR']);
					$('#kvert-geotexan-value').val(ferrocarriles[i]['Geotexan']['KVERT']);
					$('#rt-geotextil-value').val(ferrocarriles[i]['Geotextil']['RT']);
					$('#elong-geotextil-value').val(ferrocarriles[i]['Geotextil']['ELONG']);
					$('#cbr-geotextil-value').val(ferrocarriles[i]['Geotextil']['RCBR']);
					$('#kvert-geotextil-value').val(ferrocarriles[i]['Geotextil']['KVERT']);
					$('#product').val(ferrocarriles[i]['GEOTESAN']);
					return true;
				}
			}
		}
	});
}