[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ColorFillScheme Class

---



|  |
| --- |
| [Members](84fa2422-2777-e09e-f438-84976b7c8390.htm)   [See Also](#seeAlsoToggle) |

Represents a color scheme could be used to colorfy elements in floor plan views and section views.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public class ColorFillScheme : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ColorFillScheme _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ColorFillScheme : public Element ``` |

# Remarks

A color scheme is based on element category and one of the category parameter, it contains a set of  [ColorFillSchemeEntry](065ddef3-065a-8bd5-9d34-4d2efd126e43.htm)  which stores parameter value, color, fill pattern and other entry data. The entry paramater values may be a range or a single value, based on the  [IsByRange](2e6a3c32-a3f8-a6dd-6552-7ba7a901d9fb.htm)  property. Then elements with the specified category could be colored with the color and fill pattern of matching entry whose parameter value or value range matches the element parameter value.

You can retrieve the entries with  [GetEntries](bb3b650c-2718-28b7-c4bb-be3f80fb3e32.htm)  , or modify entries with  [AddEntry(ColorFillSchemeEntry)](8c7f6d04-66ab-19ef-d00c-445aa4570f82.htm)  ,  [RemoveEntry(ColorFillSchemeEntry)](e7441d50-0e17-21be-8ff6-aadadacad417.htm)  ,  [UpdateEntry(ColorFillSchemeEntry)](47fece43-de9a-e343-62be-e6907c584933.htm)  and  [M:Autodesk.Revit.DB.ColorFillScheme.SetEntries(System.Collections.Generic.IList`1{Autodesk.Revit.DB.ColorFillSchemeEntry})]  .

Unlike most of the other elements, the color scheme works in an "asynchronous" way in UI:

1. If document elements change, the color scheme will not be updated immediately.
2. If color schemes changes, the document elements will not be updated immediately too.

API works slightly different with UI:

1. [GetEntries](bb3b650c-2718-28b7-c4bb-be3f80fb3e32.htm)  will return the entries corresponding to the latest document elements status immediately.
2. The entries modification operation will retrieve the latest entries with  [GetEntries](bb3b650c-2718-28b7-c4bb-be3f80fb3e32.htm)  at first, and then modify those entries by request, but document elements will still not be updated immediately.
3. To modify multiple entries, it's better to use  [M:Autodesk.Revit.DB.ColorFillScheme.SetEntries(System.Collections.Generic.IList`1{Autodesk.Revit.DB.ColorFillSchemeEntry})]  but not modify them one by one with other methods for better performance.

Notes:

* To apply a color scheme whose  [CategoryId](7f1d0a3c-4194-f165-0203-5aba9431a1b8.htm)  property is OST\_Areas to an area plan view, the  [AreaSchemeId](e24d76dd-38fb-c951-7ae4-d10101b4981b.htm)  property must be the same as the view if it is not used as a template.
* To generate a new color scheme, you have to use  [Duplicate(String)](095596ae-d215-bf22-ccfa-fae85109d1a0.htm)  method to duplicate form an existing one.
* There should not exist two entries values that are the same in a color scheme. if the  [StorageType](41c8e61c-fa40-0d69-9c5c-d955baaddbf5.htm)  property is Double, then the value accuracy should be based on  [FormatOptions](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)  property.

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB ColorFillScheme

# See Also

[ColorFillScheme Members](84fa2422-2777-e09e-f438-84976b7c8390.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)