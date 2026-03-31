[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateRibbonPanel Method (String)

---



|  |
| --- |
| [UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Create a new RibbonPanel on the Add-Ins tab.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual RibbonPanel CreateRibbonPanel( 	string panelName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function CreateRibbonPanel ( _ 	panelName As String _ ) As RibbonPanel ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual RibbonPanel^ CreateRibbonPanel( 	String^ panelName ) ``` |

#### Parameters

panelName
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The name of the panel to be created.

# Remarks

This method will create a custom panel appending to the Revit AddIns tab. This method is not supported in Macros.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public Result OnStartup(UIControlledApplication application)
{
    // add new ribbon panel
    RibbonPanel ribbonPanel = application.CreateRibbonPanel("NewRibbonPanel");

    //Create a push button in the ribbon panel “NewRibbonPanel”
    //the add-in application “HelloWorld” will be triggered when button is pushed

    PushButton pushButton = ribbonPanel.AddItem(new PushButtonData("HelloWorld", 
        "HelloWorld", @"D:\HelloWorld.dll", "HelloWorld.CsHelloWorld")) as PushButton;

    // Set the large image shown on button
    Uri uriImage = new Uri(@"D:\Sample\HelloWorld\bin\Debug\39-Globe_32x32.png");
    BitmapImage largeImage = new BitmapImage(uriImage);
    pushButton.LargeImage = largeImage;


    return Result.Succeeded;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Function OnStartup(application As UIControlledApplication) As Autodesk.Revit.UI.Result Implements IExternalApplication.OnStartup
    ' add new ribbon panel
    Dim ribbonPanel As RibbonPanel = application.CreateRibbonPanel("NewRibbonPanel")

    'Create a push button in the ribbon panel “NewRibbonPanel”
    'the add-in application “HelloWorld” will be triggered when button is pushed


    Dim pushButton As PushButton = TryCast(ribbonPanel.AddItem(New PushButtonData("HelloWorld", "HelloWorld", "D:\HelloWorld.dll", "HelloWorld.CsHelloWorld")), PushButton)

    ' Set the large image shown on button
    Dim uriImage As New Uri("D:\Sample\HelloWorld\bin\Debug\39-Globe_32x32.png")
    Dim largeImage As New BitmapImage(uriImage)
    pushButton.LargeImage = largeImage


    Return Result.Succeeded
End Function
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | panelName is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | panelName is Empty. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | If more than 100 panels were created. |

# See Also

[UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)

[CreateRibbonPanel Overload](f10d6cf3-0e12-ccaa-e368-e32eef3ec088.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)