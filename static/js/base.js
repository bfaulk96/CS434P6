$(document).ready(function () {
    $('#MostTDs').DataTable({'order':[[1, 'desc']], 'bLengthChange':false});
    $('#sacksAndReceivingTDs').DataTable({'order':[[1, 'desc']], 'bLengthChange':false});
    $('#longerThanZuerleinTable').DataTable({'order':[[1, 'desc']], 'bLengthChange':false});

    val = $('#kickerSelect').val();
    if (val === 'Greg Zuerlein'){
        $('#longestFG').html('61');
    }else if (val === 'Matt Prater'){
        $('#longestFG').html('64');
    }else if (val === 'Mason Crosby'){
        $('#longestFG').html('58');
    }else if (val === 'Dan Carpenter'){
        $('#longestFG').html('60');
    }

    $('#kickerSelect').change(function(){
        val = $(this).val();
        if (val === 'Greg Zuerlein'){
            $('#longestFG').html('61');
        }else if (val === 'Matt Prater'){
            $('#longestFG').html('64');
        }else if (val === 'Mason Crosby'){
            $('#longestFG').html('58');
        }else if (val === 'Dan Carpenter'){
            $('#longestFG').html('60');
        }
    });

    var table = $('#Player').DataTable();
    table.$('[data-toggle="popover"]').popover();
    //triggered when modal is about to be shown
    $('#editModal').on('show.bs.modal', function (e) {
        //get data-id attribute of the clicked element
        var id = $(e.relatedTarget).data('id');
        var name = $(e.relatedTarget).data('name');
        var currentStatus = $(e.relatedTarget).data('currentstatus');
        var team = $(e.relatedTarget).data('team');
        var year = $(e.relatedTarget).data('year');
        var rushingYards = $(e.relatedTarget).data('rushingyards');
        var rushingTDs = $(e.relatedTarget).data('rushingtds');
        var fumbles = $(e.relatedTarget).data('fumbles');
        $(e.currentTarget).find('#id1').val(id);
        $(e.currentTarget).find('#id').val(id);
        $(e.currentTarget).find('#name1').val(name);
        $(e.currentTarget).find('#name').val(name);
        $(e.currentTarget).find('#currentStatus1').val(currentStatus);
        $(e.currentTarget).find('#currentStatus').val(currentStatus);
        $(e.currentTarget).find('#year1').val(year);
        $(e.currentTarget).find('#year').val(year);
        $(e.currentTarget).find('#team1').val(team);
        $(e.currentTarget).find('#team').val(team);
        $(e.currentTarget).find('#rushingYards').val(rushingYards);
        $(e.currentTarget).find('#rushingTDs').val(rushingTDs);
        $(e.currentTarget).find('#fumbles').val(fumbles);
    });
});

$('table').ready(function () {
    $(function () {
        // Enables popover
        $("[data-toggle=popover]").popover();
    });
});