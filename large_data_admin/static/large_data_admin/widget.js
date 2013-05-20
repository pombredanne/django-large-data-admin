function select_input(id, url, min_length, callback){
    $("#"+id).keyup(function() {
        if ($("#"+id).val().length > min_length - 1){
            $.get(url+"?q="+$("#"+id).val(), function (d){
                d = JSON.parse(d);
                $("#"+id+"_list").empty();
                d.forEach(function (i) {
                    $("#"+id+"_list").append("<li><a href=\"#\" id=\""+id+i[0]+"\">"+i[1]+"</a></li>");
                    $("#"+id+i[0]).click(function(){
                        $("#"+id+"_list").empty();
                        $("#"+id).val("");
                        callback(i);
                    })
                })
            })
        }
    })
}

function check_input(id, url, min_length, callback){
    $("#"+id).keyup(function() {
        if ($("#"+id).val().length > min_length - 1){
            $.get(url+"?q="+$("#"+id).val(), function (d){
                d = JSON.parse(d);
                $("#"+id+"_out").removeClass("color-red");
                $("#"+id+"_out").removeClass("color-green");
                $("#"+id+"_out").removeClass("color-orange");
                if (d.length == 0){
                    $("#"+id+"_out").addClass("color-red");
                }
                else if (d.length == 1){
                    $("#"+id+"_out").addClass("color-green");
                }
                else if (d.length > 1){
                    $("#"+id+"_out").addClass("color-orange");
                }
                $("#"+id+"_list").empty();
                d.forEach(function (i) {
                    $("#"+id+"_list").append("<li>"+i[1]+"</li>");
                })
            })
        }
    })
}


function num_selected(id, url, callback){
    $.get(url, function (d){
        d = JSON.parse(d);
        $("#"+id).val(d);
    })
}