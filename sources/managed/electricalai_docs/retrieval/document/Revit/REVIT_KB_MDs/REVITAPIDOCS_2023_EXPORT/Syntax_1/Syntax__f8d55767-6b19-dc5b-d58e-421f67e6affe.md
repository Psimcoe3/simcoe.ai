[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsProductListEntryCompatibleSize Method

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

Checks to see if this part can be changed to the specified product entry without altering any connected dimensions.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016 Subscription Release

# Syntax

| C# |
| --- |
| ``` public bool IsProductListEntryCompatibleSize( 	int productEntry ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsProductListEntryCompatibleSize ( _ 	productEntry As Integer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsProductListEntryCompatibleSize( 	int productEntry ) ``` |

#### Parameters

productEntry
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The product entry index.

#### Return Value

Returns true if the part can be changed to the specified product entry without altering any connected dimensions.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The product entry index is not larger than 0 and less than GetProductCount. |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)