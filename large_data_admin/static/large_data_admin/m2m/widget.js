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
