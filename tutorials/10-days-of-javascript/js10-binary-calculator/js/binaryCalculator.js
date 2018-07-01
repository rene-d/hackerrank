btnClr.onclick = function() {
    res.innerHTML = "";
}

btnEql.onclick = function() {
    let s = res.innerHTML;
    s = Math.floor(eval(s.replace(/([01]+)/g, '0b$1'))).toString(2);
    res.innerHTML = s;
}

btn0.onclick = function() {
    res.innerHTML += "0";
}
btn1.onclick = function() {
    res.innerHTML += "1";
}
btnSum.onclick = function() {
    res.innerHTML += "+";
}
btnSub.onclick = function() {
    res.innerHTML += "-";
}
btnMul.onclick = function() {
    res.innerHTML += "*";
}
btnDiv.onclick = function() {
    res.innerHTML += "/";
}
