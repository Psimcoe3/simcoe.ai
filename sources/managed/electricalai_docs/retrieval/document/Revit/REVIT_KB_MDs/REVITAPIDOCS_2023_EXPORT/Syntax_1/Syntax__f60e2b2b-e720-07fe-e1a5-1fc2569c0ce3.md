[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Erase Method

---



|  |
| --- |
| [BindingMap Class](4ce777fb-ab30-6d15-d019-5b430223ac62.htm)   [See Also](#seeAlsoToggle) |

This method is used to erase one item in the map.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public override int Erase( 	Definition key ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overrides Function Erase ( _ 	key As Definition _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual int Erase( 	Definition^ key ) override ``` |

#### Parameters

key
:   Type:  [Autodesk.Revit.DB Definition](8fe04f37-04e1-9e93-ffdb-e3900908e42a.htm)

# Remarks

The method Erase inherited from base class is not permitted for this class. A Autodesk::Revit::Exceptions::InvalidOperationException will be thrown. Use Remove() instead to remove the binding from the Revit session and from the map.

# See Also

[BindingMap Class](4ce777fb-ab30-6d15-d019-5b430223ac62.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)