//FAMILY FILE
//Get the button:
mybutton = document.getElementById("myBtn");

// When the user clicks on the button, scroll to the top of the document
function bottomFunction() {
  //document.body.scrollDown = 1; // For Safari
  //document.documentElement.scrollDown = 1; // For Chrome, Firefox, IE and Opera
  window.scrollBy(0, 680);
}

selectButton = document.getElementById("selectedPat");
function pat_selectedBtn() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
//auto change the pat status
function patient_status() {
  if ( document.getElementById("option2").checked == true ) {
      document.getElementById('status').innerHTML = "Inactive";
  }
  if ( document.getElementById("option1").checked == true ) {
      document.getElementById('status').innerHTML = "Active";
  }
  if ( document.getElementById("option3").checked == true ) {
      document.getElementById('status').innerHTML = "Archived";
  }
}
auto_click_radio();
function auto_click_radio(){
    pat_status = document.getElementById('status').innerText;
    console.log(pat_status);
    if (pat_status == "Active"){
         document.getElementById('option1').click();
    }
    if ( pat_status == "Inactive"){
         document.getElementById('option2').click();
    }
    if ( pat_status == "Archived") {
         document.getElementById('option3').click();
    }
}
//change photo from file will auto change the current img
/*
function Change_Image() {
    document.getElementById('prof_img').src = window.URL.createObjectURL(this.files[0])
}
*/
function Msg_Update(){
    alert('Successfully Updated Profile!');
}
function Msg_Success(){
    alert('Successfully Saved Profile!');
}

function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2)
        month = '0' + month;
    if (day.length < 2)
        day = '0' + day;

    document.getElementById('bformat').value = [year, month, day].join('-');

}
