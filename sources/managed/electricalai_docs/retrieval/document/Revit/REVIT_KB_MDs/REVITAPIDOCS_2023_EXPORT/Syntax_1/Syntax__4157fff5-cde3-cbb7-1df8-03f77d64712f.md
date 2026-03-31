[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Symbol Property

---



|  |
| --- |
| [FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Returns or changes the FamilySymbol object that represents the type of the instance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FamilySymbol Symbol { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Symbol As FamilySymbol 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property FamilySymbol^ Symbol { 	FamilySymbol^ get (); 	void set (FamilySymbol^ value); } ``` |

# Remarks

Setting this property will result in the type of the instance being changed. Related types can be found by examining the Family to which the symbol belongs.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void GetInfo_FamilyInstance_Symbol(FamilyInstance familyInstance)
{
    string message = "FamilyInstance symbol: ";
    if (familyInstance.Symbol != null)
    {
        // Get FamilyInstance structural symbol
        message += "\nFamilyInstance structural symbol name is : " + familyInstance.Symbol.Name;

        // Rename the Symbol used by this FamilyInstance
        familyInstance.Symbol.Name = "TestFamilyInstanceSymbolName";

        // Get FamilyInstance structural symbol
        message += "\nFamilyInstance structural symbol name after set is : " + familyInstance.Symbol.Name;
    }
    TaskDialog.Show("Revit",message);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub GetInfo_FamilyInstance_Symbol(familyInstance As FamilyInstance)
    Dim message As String = "FamilyInstance symbol: "
    If familyInstance.Symbol IsNot Nothing Then
        ' Get FamilyInstance structural symbol
        message += vbLf & "FamilyInstance structural symbol name is : " & Convert.ToString(familyInstance.Symbol.Name)

        ' Rename the Symbol used by this FamilyInstance
        familyInstance.Symbol.Name = "TestFamilyInstanceSymbolName"

        ' Get FamilyInstance structural symbol
        message += vbLf & "FamilyInstance structural symbol name after set is : " & Convert.ToString(familyInstance.Symbol.Name)
    End If
    TaskDialog.Show("Revit", message)
End Sub
```

# See Also

[FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)