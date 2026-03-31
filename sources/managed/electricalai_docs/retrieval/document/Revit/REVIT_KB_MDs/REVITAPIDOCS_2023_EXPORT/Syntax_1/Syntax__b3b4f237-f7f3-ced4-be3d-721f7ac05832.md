[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportFontTable Class

---



|  |
| --- |
| [Members](8f3793ac-5239-5de8-84fa-671bfe411356.htm)   [See Also](#seeAlsoToggle) |

A table supporting a mapping of Revit font names to font names that will be set in the target export format.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class ExportFontTable : IEnumerable<KeyValuePair<ExportFontKey, ExportFontInfo>>,  	IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ExportFontTable _ 	Implements IEnumerable(Of KeyValuePair(Of ExportFontKey, ExportFontInfo)),  _ 	IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ExportFontTable : IEnumerable<KeyValuePair<ExportFontKey^, ExportFontInfo^>>,  	IDisposable ``` |

# Remarks

This table is structured as a mapping from  [ExportFontKey](bd33456d-7898-f32c-312e-b94af14c0007.htm)  to  [ExportFontInfo](c3dc100c-0e4d-419d-5cbd-1d59f149490c.htm)  members. The  [ExportFontKey](bd33456d-7898-f32c-312e-b94af14c0007.htm)  contains the identification information for the font table: the Revit font name. The  [ExportFontInfo](c3dc100c-0e4d-419d-5cbd-1d59f149490c.htm)  contains the font name to use in the export format.

The table can be accessed via direct iteration as a collection of KeyValuePairs, or by traversal of the stored keys obtained from GetKeys(), or via specific lookup of a key constructed externally. In all cases, the  [ExportFontInfo](c3dc100c-0e4d-419d-5cbd-1d59f149490c.htm)  returned will be a copy of the  [ExportFontInfo](c3dc100c-0e4d-419d-5cbd-1d59f149490c.htm)  from the table. In order to make changes to the  [ExportFontInfo](c3dc100c-0e4d-419d-5cbd-1d59f149490c.htm)  and use those settings during export, set the modified  [ExportFontInfo](c3dc100c-0e4d-419d-5cbd-1d59f149490c.htm)  back into the table using the same key.

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB ExportFontTable

# See Also

[ExportFontTable Members](8f3793ac-5239-5de8-84fa-671bfe411356.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)