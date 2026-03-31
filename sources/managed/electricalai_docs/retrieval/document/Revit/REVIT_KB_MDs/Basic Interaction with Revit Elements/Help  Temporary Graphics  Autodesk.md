---
created: 2026-01-28T20:53:21 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_Temporary_Graphics_html
author: 
---

# Help | Temporary Graphics | Autodesk

> ## Excerpt
> The TemporaryGraphicsManager class allows you to create temporary graphics in Revit views. The graphics created by this class are not subject to undo and are not saved. The Revit API developer should manage their lifetime, creation and destruction, though Revit will destroy all of them when closing the model.

---
The `TemporaryGraphicsManager` class allows you to create temporary graphics in Revit views. The graphics created by this class are not subject to undo and are not saved. The Revit API developer should manage their lifetime, creation and destruction, though Revit will destroy all of them when closing the model.

The `AddControl` method creates a control in a specified view based on an instance of the `InCanvasControlData` class which defines the image path and location in model coordinates of the control. Additional functionality exists in the methods:

-   RemoveControl
-   SetVisibility
-   UpdateControl

This code sample creates a temporary control at the center of a wall. The website [www.autodesk.com](http://www.autodesk.com/) is opened When the user clicks on the control. The `OnClick` method is implemented in a server class that derives from `ITemporaryGraphicsHandler`.

**Code Region: Creating a Temporary Control**

```
private void TemporaryGraphicsControl(Wall wall)
{
    Document doc = wall.Document;

    MultiServerService externalService = ExternalServiceRegistry.GetService(
        ExternalServices.BuiltInExternalServices.TemporaryGraphicsHandlerService) as MultiServerService;
    MyGraphicsService myGraphicsService = new MyGraphicsService();
    externalService.AddServer(myGraphicsService);
    externalService.SetActiveServers(
        new List<Guid> {myGraphicsService.GetServerId()});

    TemporaryGraphicsManager mgr = TemporaryGraphicsManager.GetTemporaryGraphicsManager(doc);
    XYZ controlPoint = ((LocationCurve)wall.Location).Curve.Evaluate(0.5, true);
    InCanvasControlData data = new InCanvasControlData(
        @"C:/Autodesk/image32.bmp",
        controlPoint);
    mgr.AddControl(data, doc.ActiveView.Id);
}

public class MyGraphicsService: ITemporaryGraphicsHandler
{
    public void OnClick(TemporaryGraphicsCommandData data)
    {
        Process.Start("https://www.autodesk.com");
    }
    public string GetName()
    { return "My Graphics Service"; }
    public string GetDescription()
    { return "This is a graphics service"; }
    public string GetVendorId()
    { return "ADSK"; }
    public ExternalServiceId GetServiceId()
    { return ExternalServices.BuiltInExternalServices.TemporaryGraphicsHandlerService; }
    public Guid GetServerId()
    { return new Guid("a8debc37-19fe-4198-1198-01a891ff1a7f"); }
}
```
