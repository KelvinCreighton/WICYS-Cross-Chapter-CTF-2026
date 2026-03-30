function openTab(tabName, elmnt, color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
    }
    document.getElementById(tabName).style.display = "block";
    if (elmnt.style != null) {
        elmnt.style.backgroundColor = color;
    }
}

window.onload = function() {
    var defaultBtn = document.getElementById("defaultOpen");
    if (defaultBtn) {
        openTab('tabintro', defaultBtn, '#222');
    }
}

/* Heap MacCipher won't make it easy. 3/3 of the key: s1ght} */