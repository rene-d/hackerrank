var btn = document.getElementById('btn');

btn.innerHTML = 0;
btn.onclick = function() { ++btn.innerHTML; }
