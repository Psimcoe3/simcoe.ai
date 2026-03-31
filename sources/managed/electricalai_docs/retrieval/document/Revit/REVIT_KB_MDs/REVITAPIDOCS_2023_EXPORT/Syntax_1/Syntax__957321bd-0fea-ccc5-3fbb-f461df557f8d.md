[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBuiltInCategoryTypeId Method

---



|  |
| --- |
| [Category Class](d390ecf6-e5db-d7c1-d7f2-766c0686e975.htm)   [See Also](#seeAlsoToggle) |

Gets the ForgeTypeId identifying the given built-in category.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId GetBuiltInCategoryTypeId( 	BuiltInCategory categoryId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetBuiltInCategoryTypeId ( _ 	categoryId As BuiltInCategory _ ) As ForgeTypeId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ForgeTypeId^ GetBuiltInCategoryTypeId( 	BuiltInCategory categoryId ) ``` |

#### Parameters

categoryId
:   Type:  [Autodesk.Revit.DB BuiltInCategory](ba1c5b30-242f-5fdc-8ea9-ec3b61e6e722.htm)    
     The built-in category.

#### Return Value

The identifier of the given built-in category.

# Remarks

The given BuiltInCategory value must be valid according to  [Category.IsBuiltInCategoryValid(BuiltInCategory)](15f903ae-3cdf-52b0-4891-fa2d1002e481.htm)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | categoryId is not a valid built-in category. See Category.IsBuiltInCategoryValid(BuiltInCategory). |

# See Also

[Category Class](d390ecf6-e5db-d7c1-d7f2-766c0686e975.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)