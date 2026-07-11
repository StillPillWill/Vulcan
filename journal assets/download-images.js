var imgs = document.querySelectorAll("img");
var found = [];
for (var i = 0; i < imgs.length; i++) {
  var src = imgs[i].src;
  if (src && src.indexOf("blob") > -1 || src && src.indexOf("user-attachments") > -1 || src && src.indexOf("media") > -1) {
    found.push(imgs[i]);
  }
}
if (found.length === 0) {
  found = [];
  for (var i = 0; i < imgs.length; i++) {
    if (imgs[i].width > 100) found.push(imgs[i]);
  }
}
console.log("Found " + found.length + " images");
var idx = 0;
function downloadNext() {
  if (idx >= found.length) { console.log("Done!"); return; }
  idx++;
  var img = found[idx - 1];
  var url = img.src;
  fetch(url, {credentials: "include"}).then(function(r) { return r.blob(); }).then(function(blob) {
    var ext = blob.type.split("/")[1] || "png";
    var name = "img_" + idx + "." + ext;
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = name;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    console.log("Downloaded: " + name);
    setTimeout(downloadNext, 500);
  }).catch(function(e) { console.error("Failed: " + idx, e); setTimeout(downloadNext, 500); });
}
downloadNext();
