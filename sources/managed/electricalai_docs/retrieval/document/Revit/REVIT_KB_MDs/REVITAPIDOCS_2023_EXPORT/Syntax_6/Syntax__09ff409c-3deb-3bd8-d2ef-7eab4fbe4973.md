[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLabelForDiscipline Method

---



|  |
| --- |
| [LabelUtils Class](39d096e3-6f2f-13ac-237b-7549d9841ef5.htm)   [See Also](#seeAlsoToggle) |

Gets the user-visible name for a discipline.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public static string GetLabelForDiscipline( 	ForgeTypeId disciplineTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetLabelForDiscipline ( _ 	disciplineTypeId As ForgeTypeId _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: static String^ GetLabelForDiscipline( 	ForgeTypeId^ disciplineTypeId ) ``` |

#### Parameters

disciplineTypeId
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)    
     Identifier of the discipline.

# Remarks

The name is obtained in the current Revit language.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Discipline must have a definition. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[LabelUtils Class](39d096e3-6f2f-13ac-237b-7549d9841ef5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)