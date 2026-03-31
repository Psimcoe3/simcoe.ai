[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetIndentLevel Method

---



|  |
| --- |
| [FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)   [See Also](#seeAlsoToggle) |

Sets the number of tab stops that the paragraph should be indented.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void SetIndentLevel( 	TextRange textRange, 	int level ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetIndentLevel ( _ 	textRange As TextRange, _ 	level As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetIndentLevel( 	TextRange^ textRange,  	int level ) ``` |

#### Parameters

textRange
:   Type:  [Autodesk.Revit.DB TextRange](8a00baaf-8cb8-d9f0-e0a0-eaa5aa16e55e.htm)    
     The given text range.

level
:   Type:  System Int32    
     The level set on the paragraph.

# Remarks

The indent level is the number of tab stops by which each paragraph will be indented.

Note that adjoining paragraphs that have the same indent level and have a list type other than  [None](7163554f-3446-22eb-afa4-5490d5df29c8.htm)  are considered part of a numbered list. Changing the indent level of paragraphs that are bulleted or numbered (i.e. paragraphs that have a list type other than  [None](7163554f-3446-22eb-afa4-5490d5df29c8.htm)  ) may cause other changes to the document as the changed paragraphs may join or leave a list. Which will cause the other paragraphs in those lists to be renumbered.

This function applies the nesting level to all paragraphs contained in the given range. The level set on the paragraph cannot be negative and cannot be larger than the value returned by  [GetMaximumIndentLevel](3f77a7ca-54e8-28b5-e1e6-cee57afd13e6.htm)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This start index of this text range is not within the text range identifying the entire text. -or- The end of this text range is not within the text range identifying the entire text. -or- This level is too large to set on a paragraph. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for level is negative. |

# See Also

[FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)