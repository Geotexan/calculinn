var tuneles = [
  {
    "ESPESOR":"1.2",
    "TAM_ARIDO":"0-4",
    "Geotexan" : {"RT":25, "ELONG":50, "RCBR":4000, "KPLANO":7},
    "Geotextil" : {"RT":"25.6", "ELONG":50, "RCBR":4490, "KPLANO":7},
    "GEOTESAN": "NT-40"
  },
  {
    "ESPESOR":"1.2",
    "TAM_ARIDO":"4-8",
    "Geotexan" : {"RT":25, "ELONG":50, "RCBR":5000, "KPLANO":8},
    "Geotextil" : {"RT":"31.6", "ELONG":50, "RCBR":5260, "KPLANO":8},
    "GEOTESAN": "NT-46"
  },
  {
    "ESPESOR":"1.2",
    "TAM_ARIDO":"8-12",
    "Geotexan" : {"RT":30, "ELONG":50, "RCBR":6000, "KPLANO":12},
    "Geotextil" : {"RT":"36.8", "ELONG":50, "RCBR":6490, "KPLANO":9},
    "GEOTESAN": "NT-58"
  },
  {
    "ESPESOR":"1.2",
    "TAM_ARIDO":"0-4",
    "Geotexan" : {"RT":18, "ELONG":50, "RCBR":3000, "KPLANO":7},
    "Geotextil": {"RT":"19.55", "ELONG":50, "RCBR":3310, "KPLANO":6},
    "GEOTESAN": "NT-30"
  },
  {
    "ESPESOR":"1.2",
    "TAM_ARIDO":"4-8",
    "Geotexan" : {"RT":20, "ELONG":50, "RCBR":3500, "KPLANO":7},
    "Geotextil" : {"RT":"22", "ELONG":50, "RCBR":3930, "KPLANO":6},
    "GEOTESAN": "NT-35"
  },
  {
    "ESPESOR":"1.2",
    "TAM_ARIDO":"8-12",
    "Geotexan" : {"RT":25, "ELONG":50, "RCBR":4000, "KPLANO":7},
    "Geotextil" : {"RT":"25.6", "ELONG":50, "RCBR":4490, "KPLANO":7},
    "GEOTESAN": "NT-40"
  },
  {
    "ESPESOR":"2",
    "TAM_ARIDO":"0-4",
    "Geotexan" : {"RT":14, "ELONG":50, "RCBR":2500, "KPLANO":6},
    "Geotextil" : {"RT":"15", "ELONG":50, "RCBR":2570, "KPLANO":5},
    "GEOTESAN": "NT-23"
  },
  {
    "ESPESOR":"2",
    "TAM_ARIDO":"4-8",
    "Geotexan" : {"RT":16, "ELONG":50, "RCBR":3000, "KPLANO":7},
    "Geotextil" : {"RT":"18,5", "ELONG":50, "RCBR":3020, "KPLANO":5},
    "GEOTESAN": "NT-25"
  },
  {
    "ESPESOR":"2",
    "TAM_ARIDO":"8-12",
    "Geotexan" : {"RT":18, "ELONG":50, "RCBR":3000, "KPLANO":7},
    "Geotextil" : {"RT":"19.55", "ELONG":50, "RCBR":3310, "KPLANO":6},
    "GEOTESAN": "NT-30"
  }
];

function calcula() {
    var ia = $('#i-a').val();
    var ie = $('#i-e').val();

    $.each(tuneles, function(i, item) {
        if (tuneles[i]['ESPESOR'] == ie ) {
            if (tuneles[i]['TAM_ARIDO'] == ia) {
                //Relleno valores del formulario y salgo de la iteración
                $('#rt-geotexan-value').val(tuneles[i]['Geotexan']['RT']);
                $('#elong-geotexan-value').val(tuneles[i]['Geotexan']['ELONG']);
                $('#cbr-geotexan-value').val(tuneles[i]['Geotexan']['RCBR']);
                $('#kplano-geotexan-value').val(tuneles[i]['Geotexan']['KPLANO']);
                $('#rt-geotextil-value').val(tuneles[i]['Geotextil']['RT']);
                $('#elong-geotextil-value').val(tuneles[i]['Geotextil']['ELONG']);
                $('#cbr-geotextil-value').val(tuneles[i]['Geotextil']['RCBR']);
                $('#kplano-geotextil-value').val(tuneles[i]['Geotextil']['KPLANO']);
                $('#product').val(tuneles[i]['GEOTESAN']);
                return true;
            }
        }
    });
}