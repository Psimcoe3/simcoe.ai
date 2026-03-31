[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OverrideResult Method

---



|  |
| --- |
| [DialogBoxData Class](41f22b16-a68b-8c19-53f6-de079feb756c.htm)   [See Also](#seeAlsoToggle) |

Call this method to cause the Autodesk Revit dialog to be dismissed with the specified return value.

**Namespace:**   [Autodesk.Revit.UI.Events](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool OverrideResult( 	int result ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function OverrideResult ( _ 	result As Integer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool OverrideResult( 	int result ) ``` |

#### Parameters

result
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The result code you wish the Revit dialog to return.

#### Return Value

Returns true if the result code was accepted.

# See Also

[DialogBoxData Class](41f22b16-a68b-8c19-53f6-de079feb756c.htm)

[Autodesk.Revit.UI.Events Namespace](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)