var fichas =
{
	"NT-10" : "1-1-01_geotesan_nt10.pdf",
	"NT-11" : "1-1-02_geotesan_nt11.pdf",
	"NT-12" : "1-1-03_geotesan_nt12.pdf",
	"NT-13" : "1-1-04_geotesan_nt13.pdf",
	"NT-14" : "1-1-05_geotesan_nt14.pdf",
	"NT-15" : "1-1-06_geotesan_nt15.pdf",
	"NT-17" : "1-1-07_geotesan_nt17.pdf",
	"NT-175" : "1-1-08_geotesan_nt175.pdf",
	"NT-18" : "1-1-09_geotesan_nt18.pdf",
	"NT-21" : "1-1-10_geotesan_nt21.pdf",
	"NT-23" : "1-1-11_geotesan_nt23.pdf",
	"NT-25" : "1-1-12_geotesan_nt25.pdf",
	"NT-30" : "1-1-13_geotesan_nt30.pdf",
	"NT-35" : "1-1-14_geotesan_nt35.pdf",
	"NT-40" : "1-1-15_geotesan_nt40.pdf",
	"NT-46" : "1-1-16_geotesan_nt46.pdf",
	"NT-58" : "1-1-17_geotesan_nt58.pdf",
    "GEOTEXGRID 20/20": "1-4-12_geotexgrid-2020_3030_4020_4040_5020.pdf",
    "GEOTEXGRID 30/30": "1-4-12_geotexgrid-2020_3030_4020_4040_5020.pdf",
    "GEOTEXGRID 40/20": "1-4-12_geotexgrid-2020_3030_4020_4040_5020.pdf",
    "GEOTEXGRID 40/40": "1-4-12_geotexgrid-2020_3030_4020_4040_5020.pdf",
    "GEOTEXGRID 50/20": "1-4-12_geotexgrid-2020_3030_4020_4040_5020.pdf",
    "GEOTEXGRID 50/60": "1-4-13_geotexgrid-5050_6030_6060_8030_8080.pdf",
    "GEOTEXGRID 60/30": "1-4-13_geotexgrid-5050_6030_6060_8030_8080.pdf",
    "GEOTEXGRID 60/60": "1-4-13_geotexgrid-5050_6030_6060_8030_8080.pdf",
    "GEOTEXGRID 80/30": "1-4-13_geotexgrid-5050_6030_6060_8030_8080.pdf",
    "GEOTEXGRID 80/80": "1-4-13_geotexgrid-5050_6030_6060_8030_8080.pdf",
    "GEOTEXGRID 90/90": "1-4-14_geotexgrid-9090_100100_11030_13030_15030.pdf",
    "GEOTEXGRID 100/100": "1-4-14_geotexgrid-9090_100100_11030_13030_15030.pdf",
    "GEOTEXGRID 110/30": "1-4-14_geotexgrid-9090_100100_11030_13030_15030.pdf",
    "GEOTEXGRID 130/30": "1-4-14_geotexgrid-9090_100100_11030_13030_15030.pdf",
    "GEOTEXGRID 150/30": "1-4-14_geotexgrid-9090_100100_11030_13030_15030.pdf"
};

/*
* Asociar la apertura de una nueva pestaña al click sobre
* el enlace situado en el footer
*/
$(document).ready(function() {
	$('#pdf').click(function() {
        var flag_version = 1;   // No se me ocurre otra manera más rápida.
		var nt = $('#product').val();
        if ( nt == ''){
            // No es un input, viene del template. Es un span.
            nt = $('#product').text();
            // console.log("nt");
            // console.log(nt);
            /* TODO: Tal y como está ahora, solo mostrará la ficha técnica
             * del primero de los productos recomendados. Todos los demás
             * que se agreguen a la tabla llevan el mismo id.
             */
            flag_version = 2;
        }
		if (typeof fichas[nt] !== 'undefined') {
    		var file = 'pdf/' + fichas[nt];
            if (flag_version >= 2){
                file = '../pdf/' + fichas[nt];
            }
			var win = window.open(file, '_blank');
			if(win){
			    //Browser has allowed it to be opened
			    win.focus();
			}else{
			    //Broswer has blocked it
			    alert('Please allow popups for this site');
			}
		}
		else {
			return false;
		}
	});

});
