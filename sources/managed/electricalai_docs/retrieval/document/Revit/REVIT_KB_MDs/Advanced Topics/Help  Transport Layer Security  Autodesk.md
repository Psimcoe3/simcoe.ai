---
created: 2026-01-28T21:19:47 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_TransportLayerSecurity_html
author: 
---

# Help | Transport Layer Security | Autodesk

> ## Excerpt
> When your add-on requires Internet communications and a specific security protocol is involved, if the protocol is TLS 1.0, 1.1 or 1.2 do not write any setting in the add-on. Instead take advantage of the native TLS support in Revit and its target .NET Framework. The complexities due to variety of Windows versions as well as .NET Framework versions have been handled in Revit.

---
When your add-on requires Internet communications and a specific security protocol is involved, if the protocol is TLS 1.0, 1.1 or 1.2 do not write any setting in the add-on. Instead take advantage of the native TLS support in Revit and its target .NET Framework. The complexities due to variety of Windows versions as well as .NET Framework versions have been handled in Revit.

If the add-on needs to specify a security protocol or its version, do not hard-code it exclusively, e.g. by directly assigning the protocol/version to the application-wide property `ServicePointManager.SecurityProtocol`. This will override Revit's native TLS configuration, which is critical for Revit to communicate with various Autodesk cloud services.

A **problematic** usage is `System.Net.ServicePointManager.SecurityProtocol = System.Net.SecurityProtocolType.Tls12;`

Instead, specify the protocol/version inclusively, e.g. by using bitwise OR (logical OR) on the application-wide property ServicePointManager.SecurityProtocol.

A **correct** usage is `System.Net.ServicePointManager.SecurityProtocol |= System.Net.SecurityProtocolType.Tls12;`
