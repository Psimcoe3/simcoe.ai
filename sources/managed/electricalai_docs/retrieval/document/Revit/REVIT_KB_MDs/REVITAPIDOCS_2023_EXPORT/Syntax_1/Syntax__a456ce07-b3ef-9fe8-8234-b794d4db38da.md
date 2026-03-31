[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddSlideOut Method

---



|  |
| --- |
| [RibbonPanel Class](544c0af7-6124-4f64-a25d-46e81ac5300f.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Adds a slideout to the current panel.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void AddSlideOut() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddSlideOut ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddSlideOut() ``` |

# Remarks

The slideout part of the panel can be shown by clicking on the arrow at the bottom of the panel. After calling AddSlideOut(), any subsequent calls to add new items will add the new item(s) to the slideout. The slideout part of the panel will be shown only if items are added after this call.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private static void AddSlideOut(RibbonPanel panel)
{
    string assembly = @"D:\Sample\HelloWorld\bin\Debug\HelloWorld.dll";

    panel.AddSlideOut();

    // create some controls for the slide out
    PushButtonData b1 = new PushButtonData("ButtonName1", "Button 1",
        assembly, "Hello.HelloButton");
    b1.LargeImage = new BitmapImage(new Uri(@"D:\Sample\HelloWorld\bin\Debug\39-Globe_32x32.png"));
    PushButtonData b2 = new PushButtonData("ButtonName2", "Button 2",
        assembly, "Hello.HelloTwo");
    b2.LargeImage = new BitmapImage(new Uri(@"D:\Sample\HelloWorld\bin\Debug\39-Globe_16x16.png"));

    // items added after call to AddSlideOut() are added to slide-out automatically
    panel.AddItem(b1);
    panel.AddItem(b2);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Shared Sub AddSlideOut(panel As RibbonPanel)
    Dim assembly As String = "D:\Sample\HelloWorld\bin\Debug\HelloWorld.dll"

    panel.AddSlideOut()

    ' create some controls for the slide out
    Dim b1 As New PushButtonData("ButtonName1", "Button 1", assembly, "Hello.HelloButton")
    b1.LargeImage = New BitmapImage(New Uri("D:\Sample\HelloWorld\bin\Debug\39-Globe_32x32.png"))
    Dim b2 As New PushButtonData("ButtonName2", "Button 2", assembly, "Hello.HelloTwo")
    b2.LargeImage = New BitmapImage(New Uri("D:\Sample\HelloWorld\bin\Debug\39-Globe_16x16.png"))

    ' items added after call to AddSlideOut() are added to slide-out automatically
    panel.AddItem(b1)
    panel.AddItem(b2)
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when a slide out panel is already added. |

# See Also

[RibbonPanel Class](544c0af7-6124-4f64-a25d-46e81ac5300f.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)