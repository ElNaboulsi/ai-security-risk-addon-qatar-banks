// usage: node build_doc.js <content.js> <out.docx>
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  AlignmentType, HeadingLevel, ShadingType, BorderStyle, LevelFormat, Footer, Header, PageNumber, PageBreak,
} = require("docx");

const C = require(path.resolve(process.argv[2]));
const OUT = process.argv[3];
const RTL = !!C.rtl;
const FONT = "Arial";
const MAROON = "8A1538", NAVY = "1E2230", GREY = "6B7280";

const run = (text, o = {}) => new TextRun({
  text, font: FONT, rightToLeft: RTL, size: o.size || 21, sizeComplexScript: o.size || 21,
  bold: !!o.bold, boldComplexScript: !!o.bold, color: o.color, italics: !!o.italic, italicsComplexScript: !!o.italic,
});
// inline **bold** support
const runs = (text, o = {}) => String(text).split(/(\*\*[^*]+\*\*)/).filter(Boolean).map(s =>
  s.startsWith("**") ? run(s.slice(2, -2), { ...o, bold: true }) : run(s, o));
const para = (text, o = {}) => new Paragraph({
  bidirectional: RTL, alignment: o.align || AlignmentType.START, keepNext: !!o.keepNext,
  spacing: { before: o.before || 0, after: o.after ?? 120, line: o.line || 300 },
  heading: o.heading, children: Array.isArray(text) ? text : runs(text, o),
});
const numConfigs = [{ reference: "bul", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.START, style: { paragraph: { indent: { start: 520, hanging: 300 } } } }] }];
let numRef = 0;

const TW = 9026;
const border = { style: BorderStyle.SINGLE, size: 4, color: "C8CED6" };
const borders = { top: border, bottom: border, left: border, right: border };
const table = (head, rows, widths) => {
  const total = widths.reduce((a, b) => a + b, 0);
  widths = widths.map(w => Math.round(w * TW / total));
  const mk = (txt, i, hdr, ri) => new TableCell({
    width: { size: widths[i], type: WidthType.DXA }, borders,
    shading: { type: ShadingType.CLEAR, fill: hdr ? NAVY : (ri % 2 ? "F5F3EF" : "FFFFFF"), color: "auto" },
    margins: { top: 70, bottom: 70, left: 110, right: 110 },
    children: String(txt).split("\n").map(line => para(line, { after: 0, size: 19, bold: hdr || (i === 0 && !hdr), color: hdr ? "FFFFFF" : undefined })),
  });
  return new Table({
    visuallyRightToLeft: RTL, width: { size: TW, type: WidthType.DXA }, columnWidths: widths,
    rows: [new TableRow({ tableHeader: true, children: head.map((h, i) => mk(h, i, true, 0)) }),
      ...rows.map((r, ri) => new TableRow({ cantSplit: true, children: r.map((c, i) => mk(c, i, false, ri)) }))],
  });
};

const children = [];
const sp = () => children.push(para("", { after: 60 }));
for (const b of C.blocks) {
  const [k, a, c, d] = b;
  if (k === "title") children.push(para(a, { size: 44, bold: true, color: NAVY, after: 160, before: 2400, line: 580 }));
  else if (k === "kicker") children.push(para(a, { size: 22, bold: true, color: MAROON, after: 80 }));
  else if (k === "sub") children.push(para(a, { size: 26, color: NAVY, after: 120 }));
  else if (k === "meta") children.push(para(a, { size: 19, color: GREY, italic: true, after: 600 }));
  else if (k === "box") children.push(new Paragraph({ bidirectional: RTL, spacing: { before: 120, after: 200, line: 300 },
      shading: { type: ShadingType.CLEAR, fill: "F7E8EC", color: "auto" },
      border: { left: { style: BorderStyle.SINGLE, size: 18, color: MAROON, space: 8 }, right: { style: BorderStyle.SINGLE, size: 18, color: MAROON, space: 8 } },
      children: runs(a, { size: 20, color: "3A0A18" }) }));
  else if (k === "pb") children.push(new Paragraph({ children: [new PageBreak()] }));
  else if (k === "h1") children.push(para(a, { heading: HeadingLevel.HEADING_1, size: 32, bold: true, color: MAROON, before: 240, after: 160, keepNext: true }));
  else if (k === "h2") children.push(para(a, { heading: HeadingLevel.HEADING_2, size: 25, bold: true, color: NAVY, before: 200, after: 100, keepNext: true }));
  else if (k === "p") children.push(para(a, { keepNext: /:\s*$/.test(a) }));
  else if (k === "b") a.forEach(t => children.push(new Paragraph({ bidirectional: RTL, numbering: { reference: "bul", level: 0 }, spacing: { after: 60, line: 300 }, children: runs(t) })));
  else if (k === "n") {
    const ref = `num${numRef++}`;
    numConfigs.push({ reference: ref, levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.START, style: { paragraph: { indent: { start: 520, hanging: 340 } } } }] });
    a.forEach(t => children.push(new Paragraph({ bidirectional: RTL, numbering: { reference: ref, level: 0 }, spacing: { after: 60, line: 300 }, children: runs(t) })));
  }
  else if (k === "tbl") { children.push(table(a, c, d)); if (b !== C.blocks[C.blocks.length - 1]) sp(); else children.push(para("", { after: 0, size: 2 })); }
  else if (k === "small") children.push(para(a, { size: 18, color: GREY, italic: true }));
}

const doc = new Document({
  creator: C.creator || "", lastModifiedBy: C.creator || "", title: C.title,
  styles: { default: { document: { run: { font: FONT, size: 21, rightToLeft: RTL } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: 32, bold: true, color: MAROON }, paragraph: { spacing: { before: 240, after: 160 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: 25, bold: true, color: NAVY }, paragraph: { spacing: { before: 200, after: 100 }, outlineLevel: 1 } },
    ] },
  numbering: { config: numConfigs },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1440, bottom: 1300, left: 1440, right: 1440 } }, bidi: RTL },
    headers: { default: new Header({ children: [para(C.header, { size: 16, color: GREY, align: AlignmentType.END, after: 0 })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ bidirectional: RTL, alignment: AlignmentType.CENTER, children: [run(C.footer + " · ", { size: 16, color: GREY }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16, color: GREY })] })] }) },
    children,
  }],
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync(OUT, b); console.log("ok", OUT); });
