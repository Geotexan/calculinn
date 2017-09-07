/*
 * "Parsea" los parámetros de la url y sistutuye los `span` que se llamen 
 * igual por el valor de cada parámetro.
 */

var DEBUG=false;

// "Parser" de parámetros. Los guarda en una `hashmap` o como se llamen en JS.
var params={};location.search.replace(/[?&]+([^=&]+)=([^&]*)/gi,function(s,k,v){params[k]=v})

// Cuando se acaba de cargar la página, hago la sustitución.
$(document).ready(function() {
    for (var param  in params) {
    	var valor=decodeURIComponent(params[param]);
        $("#"+param).text(valor);
        if (DEBUG){
        	console.log(param);
        	console.log(valor);
        }
    }
});
