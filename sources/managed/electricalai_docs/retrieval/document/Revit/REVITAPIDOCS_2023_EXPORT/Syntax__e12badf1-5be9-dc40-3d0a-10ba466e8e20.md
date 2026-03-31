[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetConnectedProperty Method (Int32)

---



|  |
| --- |
| [AssetProperty Class](7be89499-d011-ab43-4715-0ee6f9335970.htm)   [See Also](#seeAlsoToggle) |

Gets one connected property with specified index.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public AssetProperty GetConnectedProperty( 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetConnectedProperty ( _ 	index As Integer _ ) As AssetProperty ``` |

 

| Visual C++ |
| --- |
| ``` public: AssetProperty^ GetConnectedProperty( 	int index ) ``` |

#### Parameters

index
:   Type:  System Int32

#### Return Value

The AProperty of that index.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | index is out of range. |

# See Also

[AssetProperty Class](7be89499-d011-ab43-4715-0ee6f9335970.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)