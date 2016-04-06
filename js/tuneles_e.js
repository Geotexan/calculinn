var tuneles_gtx = [
  {
    "Espesor":"[1,2..1,5)",
    "Dmax":"[0..4)",
    "RT":25,
    "ELONG":50,
    "RCBR":4000,
    "KPLANO":7,
    "GEOTESAN":"NT-40"
  },
  {
    "Espesor":"[1,2..1,5)",
    "Dmax":"[4..8)",
    "RT":25,
    "ELONG":50,
    "RCBR":5000,
    "KPLANO":8,
    "GEOTESAN":"NT-46"
  },
  {
    "Espesor":"[1,2..1,5)",
    "Dmax":"[8..12]",
    "RT":30,
    "ELONG":50,
    "RCBR":6000,
    "KPLANO":12,
    "GEOTESAN":"NT-58"
  },
  {
    "Espesor":"[1,5..2)",
    "Dmax":"[0..4)",
    "RT":18,
    "ELONG":50,
    "RCBR":3000,
    "KPLANO":7,
    "GEOTESAN":"NT-30"
  },
  {
    "Espesor":"[1,5..2)",
    "Dmax":"[4..8)",
    "RT":20,
    "ELONG":50,
    "RCBR":3500,
    "KPLANO":7,
    "GEOTESAN":"NT-35"
  },
  {
    "Espesor":"[1,5..2)",
    "Dmax":"[8..12]",
    "RT":25,
    "ELONG":50,
    "RCBR":4000,
    "KPLANO":7,
    "GEOTESAN":"NT-40"
  },
  {
    "Espesor":"[2..∞)",
    "Dmax":"[0..4)",
    "RT":14,
    "ELONG":50,
    "RCBR":2500,
    "KPLANO":6,
    "GEOTESAN":"NT-23"
  },
  {
    "Espesor":"[2..∞)",
    "Dmax":"[4..8)",
    "RT":16,
    "ELONG":50,
    "RCBR":3000,
    "KPLANO":7,
    "GEOTESAN":"NT-25"
  },
  {
    "Espesor":"[2..∞)",
    "Dmax":"[8..12]",
    "RT":18,
    "ELONG":50,
    "RCBR":3000,
    "KPLANO":7,
    "GEOTESAN":"NT-30"
  }
];

var tuneles_gtxtl = [
  {
    "Espesor":"[1,2..1,5)",
    "Dmax":"[0..4)",
    "RT":"25,6",
    "ELONG":50,
    "RCBR":4490,
    "KPLANO":7,
    "GEOTESAN":"NT-40"
  },
  {
    "Espesor":"[1,2..1,5)",
    "Dmax":"[4..8)",
    "RT":"31,6",
    "ELONG":50,
    "RCBR":5260,
    "KPLANO":8,
    "GEOTESAN":"NT-46"
  },
  {
    "Espesor":"[1,2..1,5)",
    "Dmax":"[8..12]",
    "RT":"36,8",
    "ELONG":50,
    "RCBR":6490,
    "KPLANO":9,
    "GEOTESAN":"NT-58"
  },
  {
    "Espesor":"[1,5..2)",
    "Dmax":"[0..4)",
    "RT":"19,55",
    "ELONG":50,
    "RCBR":3310,
    "KPLANO":6,
    "GEOTESAN":"NT-30"
  },
  {
    "Espesor":"[1,5..2)",
    "Dmax":"[4..8)",
    "RT":"22",
    "ELONG":50,
    "RCBR":3930,
    "KPLANO":6,
    "GEOTESAN":"NT-35"
  },
  {
    "Espesor":"[1,5..2)",
    "Dmax":"[8..12]",
    "RT":"25,6",
    "ELONG":50,
    "RCBR":4490,
    "KPLANO":7,
    "GEOTESAN":"NT-40"
  },
  {
    "Espesor":"[2..∞)",
    "Dmax":"[0..4)",
    "RT":"15",
    "ELONG":50,
    "RCBR":2570,
    "KPLANO":5,
    "GEOTESAN":"NT-23"
  },
  {
    "Espesor":"[2..∞)",
    "Dmax":"[4..8)",
    "RT":"18,5",
    "ELONG":50,
    "RCBR":3020,
    "KPLANO":5,
    "GEOTESAN":"NT-25"
  },
  {
    "Espesor":"[2..∞)",
    "Dmax":"[8..12]",
    "RT":"19,55",
    "ELONG":50,
    "RCBR":3310,
    "KPLANO":6,
    "GEOTESAN":"NT-30"
  }
];

function calcula() {
    var id = $('#i-d').val();
    var ie = $('#i-e').val();

    if (id.length === 0 && ie === 0) {
      alert("Debe introducir todos los valores del formulario");
      return false;
    }

    if (isNaN(id) || isNaN(ie)) {
      alert("Los valores deben ser numéricos");
      return false;
    }

    if (id < 0) {
      alert('El valor de D debe ser mayor que 0');
      return false;
    } else if (id >= 0 && id < 4 ) {
      var d = '[0..4)';
    } else if (id >= 4 && id < 8) {
      var d = '[4..8)';
    } else if (id >= 8 && id <=12) {
      var d = '[8..12]'
    } else {
      alert('El valor de D debe ser menor o igual a 12');
      return false;
    }

    if (ie < 1.2) {
      alert('El valor de E debe ser mayor que 1.2');
      return false;
    } else if (ie >= 1.2 && ie < 1.5 ) {
      var e = '[1,2..1,5)';
    } else if (ie >= 1.5 && ie < 2) {
      var e = '[1,2..1,5)';
    } else if (ie >= 2) {
      var e = '[2..∞)'
    }

    var result = false;
    $.each(tuneles_gtx, function(i, item) {
        if (tuneles_gtx[i]['Espesor'] == e ) {
            if (tuneles_gtx[i]['Dmax'] == d) {
                //Relleno valores del formulario y salgo de la iteración
                $('#rt-geotexan-value').val(tuneles_gtx[i]['RT']);
                $('#elong-geotexan-value').val(tuneles_gtx[i]['ELONG']);
                $('#cbr-geotexan-value').val(tuneles_gtx[i]['RCBR']);
                $('#kplano-geotexan-value').val(tuneles_gtx[i]['KPLANO']);
                $('#rt-geotextil-value').val(tuneles_gtxtl[i]['RT']);
                $('#elong-geotextil-value').val(tuneles_gtxtl[i]['ELONG']);
                $('#cbr-geotextil-value').val(tuneles_gtxtl[i]['RCBR']);
                $('#kplano-geotextil-value').val(tuneles_gtxtl[i]['KPLANO']);
                $('#product').val(tuneles_gtxtl[i]['GEOTESAN']);
                result = true;
                return true;
            }
        }
    });
    if (!result) {
      alert('No se han encontrado resultados');
    }
}