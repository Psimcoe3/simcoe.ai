[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidDataType Method

---



|  |
| --- |
| [SpecUtils Class](21c660df-947f-4aa4-29f0-f3cd78f62d6c.htm)   [See Also](#seeAlsoToggle) |

Returns true if the given ForgeTypeId identifies a valid parameter data type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public static bool IsValidDataType( 	ForgeTypeId dataType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidDataType ( _ 	dataType As ForgeTypeId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidDataType( 	ForgeTypeId^ dataType ) ``` |

#### Parameters

dataType
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)    
     The identifier to check.

#### Return Value

True if the ForgeTypeId identifies either a spec or a category, false otherwise.

# Remarks

A ForgeTypeId is acceptable as a parameter data type if it identifies either a spec or a category. When a category identifier is used as a parameter data type, it indicates a Family Type parameter of that category.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SpecUtils Class](21c660df-947f-4aa4-29f0-f3cd78f62d6c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)