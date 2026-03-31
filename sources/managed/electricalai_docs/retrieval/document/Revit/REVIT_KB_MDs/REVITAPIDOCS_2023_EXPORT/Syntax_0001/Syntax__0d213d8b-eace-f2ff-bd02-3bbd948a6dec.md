[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ITransientElementMaker Interface

---



|  |
| --- |
| [Members](ca5ba0a1-1e7a-e60d-576d-40344ce6cc78.htm)   [See Also](#seeAlsoToggle) |

The interface to be implemented by an application that creates transient element(s) in Revit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public interface ITransientElementMaker ``` |

 

| Visual Basic |
| --- |
| ``` Public Interface ITransientElementMaker ``` |

 

| Visual C++ |
| --- |
| ``` public interface class ITransientElementMaker ``` |

# Remarks

An instance of the implemented interface is passed as an argument to the Document.MakeTransientElements() method, which will call back the Execute method of the interface.

During the execution of the method Revit will allow creation of certain elements, such as DirectShape, and will make them automatically transient . See (  [IsTransient](f391d235-555f-6651-99c6-895fc443f8d8.htm)  for more details about transient elements.)

The code within the Execute method is not allowed to modify the model in any other way. An attempt to change the model or create elements of other kinds will result in an exception. This indirectly means that methods using a transaction internally are not allowed either. Such methods include document Save and SaveAs, certain import and export methods, creating links, syncing with central, etc.

Regenerating the model is also not allowed for the entire duration of the Execute method.

This interface is passed to  [MakeTransientElements(ITransientElementMaker)](0decdddc-ae4a-d46d-d141-9d37e7973e05.htm)  which does the actual transient element creation.

# See Also

[ITransientElementMaker Members](ca5ba0a1-1e7a-e60d-576d-40344ce6cc78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)