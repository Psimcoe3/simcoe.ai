[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDiscipline Method

---



|  |
| --- |
| [UnitUtils Class](128dd879-fea8-5d7b-1eb2-d64f87753990.htm)   [See Also](#seeAlsoToggle) |

Gets the discipline for a given measurable spec.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId GetDiscipline( 	ForgeTypeId specTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetDiscipline ( _ 	specTypeId As ForgeTypeId _ ) As ForgeTypeId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ForgeTypeId^ GetDiscipline( 	ForgeTypeId^ specTypeId ) ``` |

#### Parameters

specTypeId
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)    
     Identifier of the measurable spec.

#### Return Value

Identifier of the discipline.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | specTypeId is not a measurable spec identifier. See UnitUtils.IsMeasurableSpec(ForgeTypeId). |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[UnitUtils Class](128dd879-fea8-5d7b-1eb2-d64f87753990.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)