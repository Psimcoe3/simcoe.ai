[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewSheetSet Class

---



|  |
| --- |
| [Members](07f33056-4b5e-e796-7c85-deef8ecaf72c.htm)   [See Also](#seeAlsoToggle) |

Represents ViewSheetSets stored in a document. ViewSheetSets can be stored so that the same printing task can be executed multiple times.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public class ViewSheetSet : Element,  	IViewSheetSet ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ViewSheetSet _ 	Inherits Element _ 	Implements IViewSheetSet ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ViewSheetSet : public Element,  	IViewSheetSet ``` |

# Remarks

For the in-session ViewSheetSet, see the class  [InSessionViewSheetSet](61a44d58-c862-5fb6-6a06-dd3d3abac585.htm)  . Changes of ViewSheetSet would be effiective after  [!:Autodesk::Revit::DB::ViewSheetSetting::Save]

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB ViewSheetSet

# See Also

[ViewSheetSet Members](07f33056-4b5e-e796-7c85-deef8ecaf72c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)