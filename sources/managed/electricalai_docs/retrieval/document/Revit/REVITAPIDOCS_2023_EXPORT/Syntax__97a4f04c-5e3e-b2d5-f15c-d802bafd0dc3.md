[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ShowElements Method (ElementSet)

---



|  |
| --- |
| [UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)   [See Also](#seeAlsoToggle) |

Shows the elements by zoom to fit.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void ShowElements( 	ElementSet elements ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ShowElements ( _ 	elements As ElementSet _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ShowElements( 	ElementSet^ elements ) ``` |

#### Parameters

elements
:   Type:  [Autodesk.Revit.DB ElementSet](48b47759-c441-ded2-5d8c-5c541c3eab01.htm)    
     The set of elements that will be shown.

# Remarks

Places all the elements on the screen by moving the view.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Elements is null. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Member of elements is null. |

# See Also

[UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)

[ShowElements Overload](52ac2a55-1397-3d05-311f-de3443421ae6.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)