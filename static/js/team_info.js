$(document).ready(function () {
    $('#roster').hide();


            // player_table.append(first_row);
});

$(document).on('change',"#country_list",function (e) {
    $target = $(e.target);
    var country = $("#country_list option:selected").text();
   name_info={team_name:country};
    $.ajax({
        url: '/team_info',
        data: name_info,
        type: 'POST',
        success: function (response) {
           var r = JSON.parse(response);
            $('#roster tbody').remove();
            var table = $("#roster");
            var tbody = $("<tbody>")

            for (var z = 0; z < Object.keys(r["Caps"]).length-1; z++) {
            row = $('<tr>')
            for (var x in r) {
                var col = $("<td>");
                col.text(r[x][z])
                row.append(col);
            }
            tbody.append(row);
        }
            table.append(tbody);
            table.show();
        },

        error: function (error) {
            console.log(error);
        }
    });
    });


