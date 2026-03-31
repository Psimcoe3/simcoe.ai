[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewDisplayDepthCueing Class

---



|  |
| --- |
| [Members](86be30af-5c94-1565-22d7-dd48b113ff7c.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Represents the settings for depth cueing.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public class ViewDisplayDepthCueing : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ViewDisplayDepthCueing _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ViewDisplayDepthCueing : IDisposable ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void AdjustDepthCueing(View view)
{
    if (view.CanUseDepthCueing())
    {
        using (Transaction t = new Transaction(view.Document, "Change depth cueing"))
        {
            t.Start();
            ViewDisplayDepthCueing depthCueing = view.GetDepthCueing();
            depthCueing.EnableDepthCueing = true;
            depthCueing.FadeTo = 50;    // set fade to percent
            depthCueing.SetStartEndPercentages(0, 75);
            view.SetDepthCueing(depthCueing);
            t.Commit();
        }
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub AdjustDepthCueing(view As View)
    If view.CanUseDepthCueing() Then
        Using t As New Transaction(view.Document, "Change depth cueing")
            t.Start()
            Dim depthCueing As ViewDisplayDepthCueing = view.GetDepthCueing()
            depthCueing.EnableDepthCueing = True
            depthCueing.FadeTo = 50
            ' set fade to percent
            depthCueing.SetStartEndPercentages(0, 75)
            view.SetDepthCueing(depthCueing)
            t.Commit()
        End Using
    End If
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ViewDisplayDepthCueing

# See Also

[ViewDisplayDepthCueing Members](86be30af-5c94-1565-22d7-dd48b113ff7c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)