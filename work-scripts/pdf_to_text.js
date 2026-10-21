ObjC.import('PDFKit');
function run(argv) {
  var url = $.NSURL.fileURLWithPath(argv[0]);
  var doc = $.PDFDocument.alloc.initWithURL(url);
  var n = doc.pageCount;
  var out = [];
  for (var i = 0; i < n; i++) {
    out.push("=== PAGE " + (i+1) + " ===\n" + ObjC.unwrap(doc.pageAtIndex(i).string));
  }
  return out.join("\n");
}
