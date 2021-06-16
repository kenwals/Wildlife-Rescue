/**
 * this formats the date passed and returns it as YYYY-MM-DDD
 */
function formatDate(date) {
    var d = new Date(date),
      month = '' + (d.getMonth() + 1),
      day = '' + d.getDate(),
      year = d.getFullYear();
  
    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;
  
    return [year, month, day].join('-');
    // taken from https://stackoverflow.com/questions/23593052/format-javascript-date-as-yyyy-mm-dd
  }
    
  let today = new Date(); // this gets todays date

  // this places a maximum date value on the datepicker field
  // so the date cannot be greater then today's date
  document.getElementById("date").max = formatDate(today); 