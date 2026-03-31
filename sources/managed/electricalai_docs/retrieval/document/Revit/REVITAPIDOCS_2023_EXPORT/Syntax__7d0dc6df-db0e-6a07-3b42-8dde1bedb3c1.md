[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IExportContext Interface

---



|  |
| --- |
| [Members](00dd06f6-d262-fd7f-5886-6ae200cb64aa.htm)   [See Also](#seeAlsoToggle) |

An interface that is used in custom export to process a Revit model.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public interface IExportContext ``` |

 

| Visual Basic |
| --- |
| ``` Public Interface IExportContext ``` |

 

| Visual C++ |
| --- |
| ``` public interface class IExportContext ``` |

# Remarks

An instance of a class that implements this interface is passed in as a parameter of the  [CustomExporter](d2437433-9183-cbb1-1c67-dedd86db5b5a.htm)  constructor. The methods of the context are then called at times of exporting entities of the model.

This is a base class for two other interfaces derived from it:  [IPhotoRenderContext](d09d4ea2-1090-f2b9-8073-5fb8a796babf.htm)  and  [IModelExportContext](4309af43-f04e-4e42-2539-3fd1d64cdc6d.htm)  . This base class contains methods that are common to both the leaf interfaces. Although it is still possible to use classes deriving directly from this base interface (for backward compatibility), future applications should implement the new leaf interfaces only.

# See Also

[IExportContext Members](00dd06f6-d262-fd7f-5886-6ae200cb64aa.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)