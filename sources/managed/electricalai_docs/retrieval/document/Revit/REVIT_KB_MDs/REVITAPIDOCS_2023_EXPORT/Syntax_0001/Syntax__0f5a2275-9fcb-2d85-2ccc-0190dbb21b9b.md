[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFileName Method

---



|  |
| --- |
| [ImageExportOptions Class](c2e823a1-6eb0-2bf3-f07b-ed46d8f7b70a.htm)   [See Also](#seeAlsoToggle) |

Gets the file name that will be produced when exporting a view to an image.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static string GetFileName( 	Document aDoc, 	ElementId dbViewId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetFileName ( _ 	aDoc As Document, _ 	dbViewId As ElementId _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: static String^ GetFileName( 	Document^ aDoc,  	ElementId^ dbViewId ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document that owns the view.

dbViewId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     View which is to be exported as image.

#### Return Value

The generated exported image file name.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ImageExportOptions Class](c2e823a1-6eb0-2bf3-f07b-ed46d8f7b70a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)