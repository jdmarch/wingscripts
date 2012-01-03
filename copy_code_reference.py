"""
From: Wingware Support <support@wingware.com>
Date: Tue, Jan 3, 2012 at 12:25 PM
Subject: Re: Copy code reference to clipboard
"""

import wingapi

def copy_reference(include_text=True):
 """Copy filename, lineno (context): followed by the current line or selected
 lines to the clipboard"""

 app = wingapi.gApplication
 editor = app.GetActiveEditor()
 if editor is None:
   return
 doc = editor.GetDocument()
 filename = doc.GetFilename()
 ana = app.GetAnalysis(filename)
 start, end = editor.GetSelection()
 startline = doc.GetLineNumberFromPosition(start)
 endline = doc.GetLineNumberFromPosition(end)
 startpos = doc.GetLineStart(startline)
 endpos = doc.GetLineEnd(endline)
 txt = doc.GetCharRange(startpos, endpos)
 scope = ana.FindScopeContainingLine(startline)

 clip_txt = filename + '\n'
 if startline == endline:
   clip_txt += 'line %i' % startline
 else:
   clip_txt += 'lines %i-%i' % (startline, endline)
 if scope:
   clip_txt += ' (%s)' % scope
 if include_text:
   clip_txt += ':' + editor.GetEol() + txt

 app.SetClipboard(clip_txt)