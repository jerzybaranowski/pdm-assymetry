ObjC.import('PDFKit');
ObjC.import('AppKit');
// Usage: osascript -l JavaScript pdf_pages_to_png.js input.pdf out_dir [width_px]
function run(argv) {
  var doc = $.PDFDocument.alloc.initWithURL($.NSURL.fileURLWithPath(argv[0]));
  var width = argv.length > 2 ? parseInt(argv[2]) : 1600;
  var n = doc.pageCount;
  for (var i = 0; i < n; i++) {
    var page = doc.pageAtIndex(i);
    var b = page.boundsForBox($.kPDFDisplayBoxMediaBox);
    var h = Math.round(width * b.size.height / b.size.width);
    var img = page.thumbnailOfSizeForBox($.NSMakeSize(width, h), $.kPDFDisplayBoxMediaBox);
    var rep = $.NSBitmapImageRep.imageRepWithData(img.TIFFRepresentation);
    var png = rep.representationUsingTypeProperties($.NSBitmapImageFileTypePNG, $());
    var num = ("0" + (i + 1)).slice(-2);
    png.writeToFileAtomically(argv[1] + "/page-" + num + ".png", true);
  }
  return n + " pages";
}
