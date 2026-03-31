[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsSpec Method

---



|  |
| --- |
| [SpecUtils Class](21c660df-947f-4aa4-29f0-f3cd78f62d6c.htm)   [See Also](#seeAlsoToggle) |

Checks whether a ForgeTypeId identifies a spec.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public static bool IsSpec( 	ForgeTypeId specTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsSpec ( _ 	specTypeId As ForgeTypeId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsSpec( 	ForgeTypeId^ specTypeId ) ``` |

#### Parameters

specTypeId
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)    
     The identifier to check.

#### Return Value

True if the ForgeTypeId identifies a spec, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SpecUtils Class](21c660df-947f-4aa4-29f0-f3cd78f62d6c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)