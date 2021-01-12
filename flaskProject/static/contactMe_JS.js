
function backgroundchang(bg){
    document.body.style.background= bg;
}

function updateDate(){
    var d = new Date();
    var months = ["January", "February","March","April","May","June","July","August","September","October","November","December"]
     document.getElementById("imgdate").innerHTML= months[d.getMonth()] + "," + d.getFullYear();


}
