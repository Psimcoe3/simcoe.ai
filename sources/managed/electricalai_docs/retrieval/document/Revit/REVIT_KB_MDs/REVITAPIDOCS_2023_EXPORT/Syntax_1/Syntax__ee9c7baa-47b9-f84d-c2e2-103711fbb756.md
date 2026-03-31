[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsDrivenByFormula Property

---



|  |
| --- |
| [GlobalParameter Class](b0e53a4a-84ad-abb4-358d-9797870f101b.htm)   [See Also](#seeAlsoToggle) |

Indicates whether this parameter is driven by a formula or not.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016 Subscription Update

# Syntax

| C# |
| --- |
| ``` public bool IsDrivenByFormula { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsDrivenByFormula As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsDrivenByFormula { 	bool get (); } ``` |

# Remarks

Note that the value of this property is always the opposite of the  [IsDrivenByDimension](201f3932-eece-37b0-be27-3e74ce0c3fb9.htm)  property. It is so because a parameter of which value is evaluated by a formula cannot be driven by a dimension, and vice versa.

# See Also

[GlobalParameter Class](b0e53a4a-84ad-abb4-358d-9797870f101b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)