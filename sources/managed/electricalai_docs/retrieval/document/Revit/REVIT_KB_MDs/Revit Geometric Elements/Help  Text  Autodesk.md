---
created: 2026-01-28T21:00:37 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Annotation_Elements_Text_html
author: 
---

# Help | Text | Autodesk

> ## Excerpt
> Text and associated leaders can be accessed from the TextNote class.
Note

---
Text and associated leaders can be accessed from the TextNote class. Note

A TextNote can have plain text or formatted text. The overloaded TextNote.Create() method provides options for creating unwrapped and line-wrapping text note elements. The width for the area of the text content can be specified on creation, but is restricted by a minimum and maximum width that is based on properties of the text and its type. The overloaded methods GetMinimumAllowedWidth() and GetMaximumAllowedWidth(), inherited from TextElement, return the constraints for either a specific TextNote or for a given document and text type id.

The following example creates a new TextNote at a user specified point and with a given width and TextNoteOptions.

<table summary="" id="GUID-20EA0F3C-7EAD-44DD-96A6-DB2933741561__TABLE_E9824E5167E64B28B657C8145321BEE4"><tbody><tr><td><b>Code Region: Create a TextNote</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>TextNote</span><span> </span><span>AddNewTextNote</span><span>(</span><span>UIDocument</span><span> uiDoc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> uiDoc</span><span>.</span><span>Document</span><span>;</span><span>
    XYZ textLoc </span><span>=</span><span> uiDoc</span><span>.</span><span>Selection</span><span>.</span><span>PickPoint</span><span>(</span><span>"Pick a point for sample text."</span><span>);</span><span>
    </span><span>ElementId</span><span> defaultTextTypeId </span><span>=</span><span> doc</span><span>.</span><span>GetDefaultElementTypeId</span><span>(</span><span>ElementTypeGroup</span><span>.</span><span>TextNoteType</span><span>);</span><span>
    </span><span>double</span><span> noteWidth </span><span>=</span><span> </span><span>.</span><span>2</span><span>;</span><span>

    </span><span>// make sure note width works for the text type</span><span>
    </span><span>double</span><span> minWidth </span><span>=</span><span> </span><span>TextNote</span><span>.</span><span>GetMinimumAllowedWidth</span><span>(</span><span>doc</span><span>,</span><span> defaultTextTypeId</span><span>);</span><span>
    </span><span>double</span><span> maxWidth </span><span>=</span><span> </span><span>TextNote</span><span>.</span><span>GetMaximumAllowedWidth</span><span>(</span><span>doc</span><span>,</span><span> defaultTextTypeId</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>noteWidth </span><span>&lt;</span><span> minWidth</span><span>)</span><span>
    </span><span>{</span><span>
        noteWidth </span><span>=</span><span> minWidth</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>noteWidth </span><span>&gt;</span><span> maxWidth</span><span>)</span><span>
    </span><span>{</span><span>
        noteWidth </span><span>=</span><span> maxWidth</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>TextNoteOptions</span><span> opts </span><span>=</span><span> </span><span>new</span><span> </span><span>TextNoteOptions</span><span>(</span><span>defaultTextTypeId</span><span>);</span><span>
    opts</span><span>.</span><span>HorizontalAlignment</span><span> </span><span>=</span><span> </span><span>HorizontalTextAlignment</span><span>.</span><span>Left</span><span>;</span><span>
    opts</span><span>.</span><span>Rotation</span><span> </span><span>=</span><span> </span><span>Math</span><span>.</span><span>PI </span><span>/</span><span> </span><span>4</span><span>;</span><span>

    </span><span>TextNote</span><span> textNote </span><span>=</span><span> </span><span>TextNote</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> doc</span><span>.</span><span>ActiveView</span><span>.</span><span>Id</span><span>,</span><span> textLoc</span><span>,</span><span> noteWidth</span><span>,</span><span> </span><span>"New sample text"</span><span>,</span><span> opts</span><span>);</span><span>

    </span><span>return</span><span> textNote</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Whether a TextNote has plain or formatted text, the unformatted text can always be retrieved from the TextNote.Text property.

## FormattedText

When first created, the TextNote will have plain text. Use the TextNote.GetFormattedText() method to get a FormattedText object for the TextNote. The FormattedText class can be used to apply various formatting to the text such as bold, underline, superscript or all caps. The TextNote is not updated until SetFormattedText() is called with the modified FormattedText.

The text in the FormattedText can be formatted in whole or in part using a TextRange. A TextRange specifies a start index and length based on the text in the FormattedText object. When the overload of a formatting method (such as SetItalicStatus() or SetAllCapsStatus()) uses a TextRange, only the characters within the range will be modified. A TextRange can be defined explicitly using its constructor, or can be retrieved using the FormattedText.Find() method to get the range for a given search string. The Find() method specifies a start index for the search, as well as whether to match the case of the search string or whether to do a whole word search. If the text in the search string is not found or if the given start index is beyond the end of the length of the entire text, an empty TextRange will be returned. Before using the returned range to set formatting on the text, ensure that it is not empty to avoid an exception.

The following example demonstrates how to format text from a TextNote and set it back to the TextNote. It uses the Find() method to bold and underline specific words in the text.

<table summary="" id="GUID-20EA0F3C-7EAD-44DD-96A6-DB2933741561__TABLE_D876E5F2B13B43758BA1616D20458D9A"><tbody><tr><td><b>Code Region: Format text in a TextNote</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>FormatText</span><span>(</span><span>TextNote</span><span> textNote</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// TextNote created with "New sample text"</span><span>
    </span><span>FormattedText</span><span> formatText </span><span>=</span><span> textNote</span><span>.</span><span>GetFormattedText</span><span>();</span><span>

    </span><span>// italicize "New"</span><span>
    </span><span>TextRange</span><span> range </span><span>=</span><span> </span><span>new</span><span> </span><span>TextRange</span><span>(</span><span>0</span><span>,</span><span> </span><span>3</span><span>);</span><span>
    formatText</span><span>.</span><span>SetItalicStatus</span><span>(</span><span>range</span><span>,</span><span> </span><span>true</span><span>);</span><span>

    </span><span>// make "sample" bold</span><span>
    range </span><span>=</span><span> formatText</span><span>.</span><span>Find</span><span>(</span><span>"sample"</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>false</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>range</span><span>.</span><span>Length</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
        formatText</span><span>.</span><span>SetBoldStatus</span><span>(</span><span>range</span><span>,</span><span> </span><span>true</span><span>);</span><span>

    </span><span>// make "text" underlined</span><span>
    range </span><span>=</span><span> formatText</span><span>.</span><span>Find</span><span>(</span><span>"text"</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>false</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>range</span><span>.</span><span>Length</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
        formatText</span><span>.</span><span>SetUnderlineStatus</span><span>(</span><span>range</span><span>,</span><span> </span><span>true</span><span>);</span><span>

    </span><span>// make all text uppercase</span><span>
    formatText</span><span>.</span><span>SetAllCapsStatus</span><span>(</span><span>true</span><span>);</span><span>

    textNote</span><span>.</span><span>SetFormattedText</span><span>(</span><span>formatText</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

New text can be added to existing text in a FormattedText object. The SetPlainText() method will either replace some existing text if the overload that has a TextRange parameter is used, or will replace the entire text if not. To insert text without replacing existing text, use a TextRange with a Length of 0. The new text will be inserted at the index specified by the TextRange.Start property. Note that when inserting text, it may pick up the formatting of the adjacent text, similar to how pasting unformatted text into a Word document will result in text with the current formatting for the insertion point. If formatting has been applied to the entire FormattedText as in the case of the SetAllCapsStatus(true) call in the example above, that formatting will be applied to any new text that is inserted.

In the following example, new text is appended to the end of existing text by first finding the end of the current text and setting that as the Start of the range to be added. It also demonstrates how to create a list (which can be bulleted, numbered or lettered). Note that it also calls GetAllCapsStatus() for the range of the new text and turns off caps if the status is not FormatStatus.None (other options are All and Mixed).

<table summary="" id="GUID-20EA0F3C-7EAD-44DD-96A6-DB2933741561__TABLE_22EAB389169945059F11CCED3E82C731"><tbody><tr><td><b>Code Region: Inserting new text</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>AppendText</span><span>(</span><span>TextNote</span><span> textNote</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FormattedText</span><span> formatText </span><span>=</span><span> textNote</span><span>.</span><span>GetFormattedText</span><span>();</span><span>

    </span><span>TextRange</span><span> range </span><span>=</span><span> formatText</span><span>.</span><span>AsTextRange</span><span>();</span><span>

    range</span><span>.</span><span>Start</span><span> </span><span>=</span><span> range</span><span>.</span><span>End</span><span> </span><span>-</span><span> </span><span>1</span><span>;</span><span>
    </span><span>// set Length to 0 to insert</span><span>
    range</span><span>.</span><span>Length</span><span> </span><span>=</span><span> </span><span>0</span><span>;</span><span>
    </span><span>string</span><span> someNewText </span><span>=</span><span> </span><span>"\rThis is a new paragraph\vThis is a new line without a paragraph break\r"</span><span>;</span><span>
    formatText</span><span>.</span><span>SetPlainText</span><span>(</span><span>range</span><span>,</span><span> someNewText</span><span>);</span><span>

    </span><span>// get range for entire text</span><span>
    range </span><span>=</span><span> formatText</span><span>.</span><span>AsTextRange</span><span>();</span><span>
    range</span><span>.</span><span>Start</span><span> </span><span>=</span><span> range</span><span>.</span><span>End</span><span> </span><span>-</span><span> </span><span>1</span><span>;</span><span>
    range</span><span>.</span><span>Length</span><span> </span><span>=</span><span> </span><span>0</span><span>;</span><span>
    </span><span>string</span><span> someListText </span><span>=</span><span> </span><span>"\rBulleted List item 1\rItem 2\vSecond line for Item 2\rThird bullet point"</span><span>;</span><span>
    formatText</span><span>.</span><span>SetPlainText</span><span>(</span><span>range</span><span>,</span><span> someListText</span><span>);</span><span>
    range</span><span>.</span><span>Start</span><span>++;</span><span>
    range</span><span>.</span><span>Length</span><span> </span><span>=</span><span> someListText</span><span>.</span><span>Length</span><span>;</span><span>
    formatText</span><span>.</span><span>SetListType</span><span>(</span><span>range</span><span>,</span><span> </span><span>ListType</span><span>.</span><span>Bullet</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>formatText</span><span>.</span><span>GetAllCapsStatus</span><span>(</span><span>range</span><span>)</span><span> </span><span>!=</span><span> </span><span>FormatStatus</span><span>.</span><span>None</span><span>)</span><span>
    </span><span>{</span><span>
        formatText</span><span>.</span><span>SetAllCapsStatus</span><span>(</span><span>range</span><span>,</span><span> </span><span>false</span><span>);</span><span>
    </span><span>}</span><span>

    textNote</span><span>.</span><span>SetFormattedText</span><span>(</span><span>formatText</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The code above shows how to use \\r to create a line break, and \\v for a vertical tab that does not break the paragraph. In the text for the bulleted list, a "\\v" is used to create a two line bullet point. A new bullet is only inserted when using "\\r".

## Text Editor

The TextEditorOptions class can be used to control the appearance and functionality of the text editor in Revit. These settings are saved in the Revit.ini file and are not tied to the document.

The Revit.ini file is in the folder returned by the property Autodesk.Revit.ApplicationServices.Application.CurrentUsersDataFolderPath (such as %appdata%\\Autodesk\\Revit\\Autodesk Revit 2019)

<table summary="" id="GUID-20EA0F3C-7EAD-44DD-96A6-DB2933741561__TABLE_2E781709FC9148A4AA725B45242F3C38"><tbody><tr><td><b>Code Region: Setting text editor options</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SetEditorOptions</span><span>()</span><span>
</span><span>{</span><span>
    </span><span>TextEditorOptions</span><span> editorOptions </span><span>=</span><span> </span><span>TextEditorOptions</span><span>.</span><span>GetTextEditorOptions</span><span>();</span><span>
    editorOptions</span><span>.</span><span>ShowBorder</span><span> </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    editorOptions</span><span>.</span><span>ShowOpaqueBackground</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Leaders

Revit supports two kinds of Leaders: straight leaders and arc leaders. Leaders can be added to a TextNote using the AddLeader() method, specifying the leader type using the TextNoteLeaderType enumerated type:

**Table 39: Leader Types**

Note: Straight leaders and arc leaders cannot be added to a Text type at the same time.

The TextNote.LeaderCount property returns the number of leaders and the GetLeaders() method returns all leaders currently attached to the text component. LeaderLeftAttachment and LeaderRightAttachment indicate the attachment position of the leaders on the corresponding side of the TextNote. Options for the LeaderAttachment are TopLine, MidPoint, and BottomLine. Use the RemoveLeaders() method to remove all leaders from the TextNote.
