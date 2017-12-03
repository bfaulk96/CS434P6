var dbSchema = {
    "Player": {"name": "string", "DOB": "date", "currentStatus": "string"},
    "Stats": {"team": "string", "year": "int", "gamesPlayed": "int"},
    "Receiving": {"team": "string", "year": "int", "receptions": "int", "receivingTDs": "int", "fumbles": "int"},
    "Defensive": {"team": "string", "year": "int", "sacks": "int", "interceptions": "int", "longestIntReturned": "int"},
    "Rushing": {"team": "string", "year": "int", "rushingYards": "int", "fumbles": "int", "rushingTDs": "int"},
    "Passing": {
        "team": "string",
        "year": "int",
        "passingTDs": "int",
        "interceptions": "int",
        "longestPass": "int",
        "sacks": "int"
    },
    "FieldGoalKicking": {
        "team": "string",
        "year": "int",
        "longestFG": "int",
        "percentageFG": "int",
        "percentagePAT": "int"
    }
};

$(document).ready(function () {
    $('#Player').DataTable();


    //triggered when modal is about to be shown
    $('#editModal').on('show.bs.modal', function (e) {
        //get data-id attribute of the clicked element
        var id = $(e.relatedTarget).data('id');
        var name = $(e.relatedTarget).data('name');
        var currentStatus = $(e.relatedTarget).data('currentstatus');
        var year = $(e.relatedTarget).data('year');
        var rushingYards = $(e.relatedTarget).data('rushingyards');
        var rushingTDs = $(e.relatedTarget).data('rushingtds');
        var fumbles = $(e.relatedTarget).data('fumbles');
        $(e.currentTarget).find('#id').val(id);
        $(e.currentTarget).find('#name').val(name);
        $(e.currentTarget).find('#currentStatus').val(currentStatus);
        $(e.currentTarget).find('#year').val(year);
        $(e.currentTarget).find('#rushingYards').val(rushingYards);
        $(e.currentTarget).find('#rushingTDs').val(rushingTDs);
        $(e.currentTarget).find('#fumbles').val(fumbles);
    });
});