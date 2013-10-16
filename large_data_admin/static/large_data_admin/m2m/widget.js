Array.prototype.remove = function(from, to) {
  var rest = this.slice((to || from) + 1 || this.length);
  this.length = from < 0 ? this.length + from : from;
  return this.push.apply(this, rest);
};

function str2list(s){
    if (s) {
        a = s.split(",");
        for (i = 0; i < a.length ; i++) { if (! a[i]) { a.pop(i); } }
        return a;   
    }
    else return []
}

function str2intList(s){
    a = str2list(s);
    for (i = 0; i < a.length ; i++) a[i] = parseInt(a[i]);
    return a;
}

function list2str(l){
    return l.toString();
}

function select_input(id, selected_id, url, min_length, callback){
    $("#"+id).keyup(function() {
        if ($("#"+id).val().length > min_length - 1){
            $.get(url+"?q="+$("#"+id).val()+"&s="+$("#"+selected_id).val(), function (d){
                d = JSON.parse(d);
                $("#"+id+"_list").empty();
                d.forEach(function (i) {
                    $("#"+id+"_list").append("<li><a id=\""+id+i[0]+"\">"+i[1]+"</a></li>");
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

function check_input(id, selected_id, url, min_length, callback){
    $("#"+id).keyup(function() {
        if ($("#"+id).val().length > min_length - 1){
            $.get(url+"?q="+$("#"+id).val()+"&s="+$("#"+selected_id).val(), function (d){
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
