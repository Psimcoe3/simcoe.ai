[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RadioButtonGroup Class

---



|  |
| --- |
| [Members](7d0c88ee-2c6e-3a99-1ec3-2a54cf19ddd0.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Represents a group of related buttons in the Ribbon.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class RadioButtonGroup : RibbonItem ``` |

 

| Visual Basic |
| --- |
| ``` Public Class RadioButtonGroup _ 	Inherits RibbonItem ``` |

 

| Visual C++ |
| --- |
| ``` public ref class RadioButtonGroup : public RibbonItem ``` |

# Remarks

This class contains a collection of ToggleButtons. Only one of the ToggleButtons will appear active at a given time. When a different button is clicked in the UI the current ToggleButton will be changed, and the ToggleButton's external command will be invoked. Use of this class is not supported in Revit Macros.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void AddRadioGroup(RibbonPanel panel)
{
    // add radio button group
    RadioButtonGroupData radioData = new RadioButtonGroupData("radioGroup");
    RadioButtonGroup radioButtonGroup = panel.AddItem(radioData) as RadioButtonGroup;

    // create toggle buttons and add to radio button group
    ToggleButtonData tb1 = new ToggleButtonData("toggleButton1", "Red");
    tb1.ToolTip = "Red Option";
    tb1.LargeImage = new BitmapImage(new Uri(@"D:\Sample\HelloWorld\bin\Debug\Red.bmp"));
    ToggleButtonData tb2 = new ToggleButtonData("toggleButton2", "Green");
    tb2.ToolTip = "Green Option";
    tb2.LargeImage = new BitmapImage(new Uri(@"D:\Sample\HelloWorld\bin\Debug\Green.bmp"));
    ToggleButtonData tb3 = new ToggleButtonData("toggleButton3", "Blue");
    tb3.ToolTip = "Blue Option";
    tb3.LargeImage = new BitmapImage(new Uri(@"D:\Sample\HelloWorld\bin\Debug\Blue.bmp"));
    radioButtonGroup.AddItem(tb1);
    radioButtonGroup.AddItem(tb2);
    radioButtonGroup.AddItem(tb3);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub AddRadioGroup(panel As RibbonPanel)
    ' add radio button group
    Dim radioData As New RadioButtonGroupData("radioGroup")
    Dim radioButtonGroup As RadioButtonGroup = TryCast(panel.AddItem(radioData), RadioButtonGroup)

    ' create toggle buttons and add to radio button group
    Dim tb1 As New ToggleButtonData("toggleButton1", "Red")
    tb1.ToolTip = "Red Option"
    tb1.LargeImage = New BitmapImage(New Uri("D:\Sample\HelloWorld\bin\Debug\Red.bmp"))
    Dim tb2 As New ToggleButtonData("toggleButton2", "Green")
    tb2.ToolTip = "Green Option"
    tb2.LargeImage = New BitmapImage(New Uri("D:\Sample\HelloWorld\bin\Debug\Green.bmp"))
    Dim tb3 As New ToggleButtonData("toggleButton3", "Blue")
    tb3.ToolTip = "Blue Option"
    tb3.LargeImage = New BitmapImage(New Uri("D:\Sample\HelloWorld\bin\Debug\Blue.bmp"))
    radioButtonGroup.AddItem(tb1)
    radioButtonGroup.AddItem(tb2)
    radioButtonGroup.AddItem(tb3)
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.UI RibbonItem](79225f03-1633-3722-15b0-752c91a3740d.htm)    
  Autodesk.Revit.UI RadioButtonGroup

# See Also

[RadioButtonGroup Members](7d0c88ee-2c6e-3a99-1ec3-2a54cf19ddd0.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)