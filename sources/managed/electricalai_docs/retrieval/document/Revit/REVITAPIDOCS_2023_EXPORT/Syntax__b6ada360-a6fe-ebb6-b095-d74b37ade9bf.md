[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FailureDefinitionId Class

---



|  |
| --- |
| [Members](57ee1d47-c340-ce31-a736-548b3aa912e3.htm)   [See Also](#seeAlsoToggle) |

The unique identifier of a FailureDefinition.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class FailureDefinitionId : GuidEnum ``` |

 

| Visual Basic |
| --- |
| ``` Public Class FailureDefinitionId _ 	Inherits GuidEnum ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FailureDefinitionId : public GuidEnum ``` |

# Remarks

Each possible failure in Revit must be defined and registered during Revit application startup by creating a FailureDefinition object. Unique FailureDefinitionId must be used as a key to register FailureDefinition. Those unique FailureDefinitionId should be created using GUID generation tool. Later FailureDefinitionId can be used to lookup FailureDefinition in FailureDefinitionRegistry, and create and post FailureMessages.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB GuidEnum](36623d19-ba65-63c0-337a-f43c593a9931.htm)    
  Autodesk.Revit.DB FailureDefinitionId

# See Also

[FailureDefinitionId Members](57ee1d47-c340-ce31-a736-548b3aa912e3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)