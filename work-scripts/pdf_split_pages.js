ObjC.import('PDFKit');
// Usage: osascript -l JavaScript pdf_split_pages.js input.pdf out_dir
function run(argv) {
  var doc = $.PDFDocument.alloc.initWithURL($.NSURL.fileURLWithPath(argv[0]));
  var n = doc.pageCount;
  for (var i = 0; i < n; i++) {
    var single = $.PDFDocument.alloc.init;
    single.insertPageAtIndex(doc.pageAtIndex(i).copy, 0);
    var num = ("0" + (i + 1)).slice(-2);
    single.writeToFile(argv[1] + "/page-" + num + ".pdf");
  }
  return n + " pages";
}
