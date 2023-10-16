from functools import total_ordering
import fitz
import os
 


def covert2pic(zoom):
    if os.path.exists('.pdf'):
        os.removedirs('.pdf')
    os.mkdir('.pdf')
    for pg in range(totaling):
        page = doc[pg]
        zoom = int(zoom)
        rotate = int(0)
        print(page)
        trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)
        pm = page.getPixmap(matrix=trans, alpha=False)

        lurl='.pdf/%s.jpg' % str(pg+1)
        pm.writePNG(lurl)
    doc.close()

def pic2pdf(obj):
    doc = fitz.open()
    for pg in range(totaling):
        img = '.pdf/%s.jpg' % str(pg+1)
        imgdoc = fitz.open(img)
        pdfbytes = imgdoc.convertToPDF()
        os.remove(img)
        imgpdf = fitz.open("pdf",pdfbytes)
        doc.insertPDF(imgpdf)
    if os.path.exists(obj):
        os.remove(obj)
    doc.save(obj)
    doc.close()

def pdfz(sor, obj, zoom):
    covert2pic(zoom)
    pic2pdf(obj)

if __name__ == "__main__":
    sor="source.pdf"
    obj="new" + sor
    doc = fitz.open(sor)
    totaling = doc.pageCount

    zoom = 200
    pdfz(sor, obj, zoom)
    os.removedirs('.pdf')