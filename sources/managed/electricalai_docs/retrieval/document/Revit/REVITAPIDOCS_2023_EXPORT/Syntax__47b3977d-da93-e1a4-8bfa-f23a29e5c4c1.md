[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewDimension Method (View, Line, ReferenceArray)

---



|  |
| --- |
| [ItemFactoryBase Class](cba2c84a-22c0-e6e7-a99c-67656901853a.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates a new linear dimension object using the default dimension style.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public Dimension NewDimension( 	View view, 	Line line, 	ReferenceArray references ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewDimension ( _ 	view As View, _ 	line As Line, _ 	references As ReferenceArray _ ) As Dimension ``` |

 

| Visual C++ |
| --- |
| ``` public: Dimension^ NewDimension( 	View^ view,  	Line^ line,  	ReferenceArray^ references ) ``` |

#### Parameters

view
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view in which the dimension is to be visible. The view must be    a null reference (  Nothing  in Visual Basic)  if the document is in  [!:Autodesk::Revit::DB::SketchEditScope]  .

line
:   Type:  [Autodesk.Revit.DB Line](e7329450-434a-918b-661c-65e15e0585a5.htm)    
     The line drawn for the dimension.

references
:   Type:  [Autodesk.Revit.DB ReferenceArray](bc9192b5-6666-a8de-0128-87dae479fd6a.htm)    
     An array of geometric references to which the dimension is to be bound.

#### Return Value

If successful a new dimension object, otherwise    a null reference (  Nothing  in Visual Basic)  .

# Remarks

The currently user set default style is used for the created dimension.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
Dimension CreateNewDimensionAlongLine(Autodesk.Revit.DB.Document document, Line line)
{
    // Use the Start and End points of our line as the references  
    // Line must come from something in Revit, such as a beam
    ReferenceArray references = new ReferenceArray();
    references.Append(line.GetEndPointReference(0));
    references.Append(line.GetEndPointReference(1));

    // create the new dimension
    Dimension dimension = document.Create.NewDimension(document.ActiveView,
                                                        line, references);
    return dimension;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Function CreateNewDimensionAlongLine(document As Autodesk.Revit.DB.Document, line As Line) As Dimension
    ' Use the Start and End points of our line as the references  
    ' Line must come from something in Revit, such as a beam
    Dim references As New ReferenceArray()
    references.Append(line.GetEndPointReference(0))
    references.Append(line.GetEndPointReference(1))

    ' create the new dimension
    Dim dimension As Dimension = document.Create.NewDimension(document.ActiveView, line, references)
    Return dimension
End Function
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when references are not geometric references. |

# See Also

[ItemFactoryBase Class](cba2c84a-22c0-e6e7-a99c-67656901853a.htm)

[NewDimension Overload](454df2e4-5ccb-b00d-434b-f3e7fdb75e8e.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)