var dbSchema = {
  "Player": {"name": "string", "DOB": "date", "currentStatus": "string"},
  "Stats": {"team": "string", "year": "int", "gamesPlayed": "int"},
  "Receiving": {"team": "string", "year": "int", "receptions": "int", "receivingTDs": "int", "fumbles": "int"},
  "Defensive": {"team": "string", "year": "int", "sacks": "int", "interceptions": "int", "longestIntReturned": "int"},
  "Rushing": {"team": "string", "year": "int", "rushingYards": "int", "fumbles": "int", "rushingTDs": "int"},
  "Passing": {"team": "string", "year": "int", "passingTDs": "int", "interceptions": "int", "longestPass": "int", "sacks": "int"},
  "FieldGoalKicking": {"team": "string", "year": "int", "longestFG": "int", "percentageFG": "int", "percentagePAT": "int"}
};

$(document).ready(function(){
   // $('#table-select').change(function(){
   //     $('#dbFields').empty();
   //     $('#table-name').empty();
   //     var value = $('#table-select').val();
   //     var options = dbSchema[value];
   //     for (var key in options){
   //          $('#table-name').for = 'dbFields';
   //          $('#table-name').innerHTML = value;
   //          switch (options[key]){
   //              case 'int':
   //                  var newLabel = document.createElement('label');
   //                  newLabel.for = key;
   //                  newLabel.innerHTML = key + ": ";
   //                  var newField = document.createElement('input');
   //                  newField.type = 'number';
   //                  newField.id = key;
   //                  break;
   //              case 'string':
   //                  var newLabel = document.createElement('label');
   //                  newLabel.for = key;
   //                  newLabel.innerHTML = key + ": ";
   //                  var newField = document.createElement('input');
   //                  newField.type = 'text';
   //                  newField.id = key;
   //                  break;
   //              case 'date':
   //                  var newLabel = document.createElement('label');
   //                  newLabel.for = key;
   //                  newLabel.innerHTML = key + ": ";
   //                  var newField = document.createElement('input');
   //                  newField.type = 'date';
   //                  newField.id = key;
   //              default:
   //                  var newLabel = document.createElement('label');
   //                  newLabel.for = key;
   //                  newLabel.innerHTML = key + ": ";
   //                  var newField = document.createElement('input');
   //                  newField.type = 'text';
   //                  newField.id = key;
   //                  break;
   //              $('#dbFields').append(newLabel);
   //              $('#dbFields').append(newField);
   //              $('#dbFields').append('<br>');
   //          }
   //     }
   // });


});