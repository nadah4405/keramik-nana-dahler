
function adjustSidebar() {
    let sidebar = document.getElementById("sidebar");
    let w = sidebar.clientWidth;
    let show = w > 100;
    var subs = document.getElementsByClassName("sidebar-sub-buttons");
    for (var i = 0; i < subs.length; i++) {
        var item = subs.item(i);
        if(show) {
            item.setAttribute("style", "display: inline-block;");
        } else {
            item.setAttribute("style", "display: none;");
        }
    }
}

window.onload = function() {
    let sidebar = document.getElementById("sidebar");
    window.onresize = function(){adjustSidebar();};
    adjustSidebar()
};