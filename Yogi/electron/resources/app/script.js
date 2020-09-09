function input( val ) {
    var x = document.getElementById("result") ;
    var y = document.getElementById("myPara") ;
    x.value += val ;
    y.innerHTML += val ;
}

function factorial( num ) {
    if (Number.isInteger(num)) {
        if (num < 2) return 1 ;
        return num * factorial(num - 1) ;
    }
}

function sqrt() {
    var x = document.getElementById("result") ;
    var y = document.getElementById("myPara") ;
    x.value += "sqrt(" ;
    y.innerHTML += (/[\d)IE]/.test(y.innerHTML.slice(-1))) ? 
    " * Math.sqrt(" : "Math.sqrt(" ;
}

function leftParen() {
    var x = document.getElementById("result") ;
    var y = document.getElementById("myPara") ;
    x.value += "(" ;
    y.innerHTML += (/[\d)IE]/.test(y.innerHTML.slice(-1))) ? 
    " * (" : "(" ;
}

function pi() {
    var x = document.getElementById("result") ;
    var y = document.getElementById("myPara") ;
        x.value += "\u03C0" ;
        y.innerHTML += (/[\d)IE]/.test(y.innerHTML.slice(-1))) ? 
        " * Math.PI" : "Math.PI" ;
    } 

function e()
{
    var x = document.getElementById("result") ;
    var y = document.getElementById("myPara") ;
    x.value += "\u0065" ;
    y.innerHTML += (/[\d)IE]/.test(y.innerHTML.slice(-1))) ? 
    " * Math.E" : "Math.E" ;
}

function expon(){
    var x = document.getElementById("result") ;
    var y = document.getElementById("myPara") ;
    x.value += 'E' ;
    y.innerHTML += (/[\d)IE]/.test(y.innerHTML.slice(-1))) ?
    " * Math.pow(10," : "Math.pow(10," ;

}
function log() {
    var x = document.getElementById("result") ;
    var y = document.getElementById("myPara") ;
        x.value += "log(" ;
        y.innerHTML += (/[\d)IE]/.test(y.innerHTML.slice(-1))) ? 
        " * Math.log10(" : "Math.log10(" ;
    }

function ln(){
    var x = document.getElementById("result") ;
    var y = document.getElementById("myPara") ;
        x.value += "ln(" ;
        y.innerHTML += (/[\d)IE]/.test(y.innerHTML.slice(-1))) ? 
        " * Math.log(" : "Math.log(" ;
    }

function trigo(trig_value) {
    var x = document.getElementById("result") ;
    var y = document.getElementById("myPara") ;
    x.value += trig_value + "(" ;
    y.innerHTML += (/[\d)IE]/.test(y.innerHTML.slice(-1))) ? 
    " * Math." + trig_value + "(Math.PI / 180 * " : "Math." + trig_value + "(Math.PI / 180 * " ;
}

function multOrDiv(opr) {
    var x = document.getElementById("result") ;
    var y = document.getElementById("myPara") ;
    if (opr == "mult") {
        x.value += "\u00D7" ;
        y.innerHTML += "*" ;
    } else {
        x.value += "\u00F7" ;
        y.innerHTML += "/"
    }
}

function percent(){
    var x = document.getElementById("result") ;
    var y = document.getElementById("myPara") ;
    x.value += "\u2052";
    y.innerHTML += "%"
}

function del() {
    var x = document.getElementById("result") ;
    var y = document.getElementById("myPara") ;
    var z = document.getElementById("myAns") ;
    if (x.value.slice(-3) == "Ans") {
        y.innerHTML = (/[\d)IE]/.test(x.value.slice(-4, -3))) ? 
        y.innerHTML.slice(0, -(z.innerHTML.length + 3)) : y.innerHTML.slice(0, -(z.innerHTML.length)) ;
        x.value = x.value.slice(0, -3) ;
    } else if (x.value == "Error!") {
        ac() ;
    } else {
        switch (y.innerHTML.slice(-2)) {
            case "* ": // sin cos tan
            y.innerHTML = (/[\d)IE]/.test(x.value.slice(-5, -4))) ? 
            y.innerHTML.slice(0, -28) : y.innerHTML.slice(0, -25) ;
            x.value = x.value.slice(0, -4) ;
            break ;
            case "n(":
            case "s(": // asin acos atan
            y.innerHTML = (/[\d)IE]/.test(x.value.slice(-7, -6))) ? 
            y.innerHTML.slice(0, -29) : y.innerHTML.slice(0, -26) ;
            x.value = x.value.slice(0, -6) ;
            break ;
            case "0(": // log
            y.innerHTML = (/[\d)IE]/.test(x.value.slice(-5, -4))) ? 
            y.innerHTML.slice(0, -14) : y.innerHTML.slice(0, -11) ;
            x.value = x.value.slice(0, -4) ;
            break ;
            case "g(": // ln
            y.innerHTML = (/[\d)IE]/.test(x.value.slice(-4, -3))) ? 
            y.innerHTML.slice(0, -12) : y.innerHTML.slice(0, -9) ;
            x.value = x.value.slice(0, -3) ;
            break ;
            case "t(": // sqrt
            y.innerHTML = (/[\d)IE]/.test(x.value.slice(-6, -5))) ? 
            y.innerHTML.slice(0, -13) : y.innerHTML.slice(0, -10) ;
            x.value = x.value.slice(0, -5) ;
            break ;
            case "PI": // pi
            y.innerHTML = (/[\d)IE]/.test(x.value.slice(-2, -1))) ? 
            y.innerHTML.slice(0, -10) : y.innerHTML.slice(0, -7) ;
            x.value = x.value.slice(0, -1) ;
            break ;
            case ".E": // e
            y.innerHTML = (/[\d)IE]/.test(x.value.slice(-2, -1))) ? 
            y.innerHTML.slice(0, -9) : y.innerHTML.slice(0, -6) ;
            x.value = x.value.slice(0, -1) ;
            break ;
            default:
            y.innerHTML = y.innerHTML.slice(0, -1) ;
            x.value = x.value.slice(0, -1) ;
        } ;
    }
}

function c() {
    var x = document.getElementById("result") ;
    var y = document.getElementById("myPara") ;
    var z = document.getElementById("myAns") ;
    x.value = y.innerHTML = z.innerHTML= "" ;
}
function ce() {
    var x = document.getElementById("result") ;
    var y = document.getElementById("myPara") ;
    x.value = y.innerHTML = "" ;
}

function ans() {
    var x = document.getElementById("result") ;
    var y = document.getElementById("myPara") ;
    var z = document.getElementById("myAns") ;
    x.value += "Ans" ;
    y.innerHTML += (/[\d)IE]/.test(y.innerHTML.slice(-1))) ? 
    " * " + z.innerHTML : z.innerHTML ;
}

function equal() {
    var x = document.getElementById("result") ;
    var y = document.getElementById("myPara") ;
    var z = document.getElementById("myAns") ;
    for (var i = 0; i < x.value.split("(").length - x.value.split(")").length; i++) {
        y.innerHTML += ")" ;
    }
    if (y.innerHTML != "") {
        x.value = y.innerHTML = z.innerHTML = eval(y.innerHTML
        .replace(/(\d+\.?\d*)\!/g, "factorial($1)")
        .replace(/(\(?[^(]*\)?)\^(\(?.*\)?)/, "Math.pow($1, $2)")
        ) ;
    }
    if (!isFinite(x.value)) x.value = "Error!" ;
}