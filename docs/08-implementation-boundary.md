# 8. Protocol and Implementation Boundary

SES defines interface semantics and expression. It intentionally does not define a transport or synchronization protocol.

A separate protocol may define how SES definitions, instances, assets, state changes, or resolved expressions move between processes, repositories, tools, runtimes, or devices.

## 8.1 SES owns

- canonical semantic types
- Slot and Socket contracts
- Block and Composition definitions
- Visual Language structure
- Theme structure
- Recipe model
- Morphology model
- Appearance model
- token semantics
- asset references
- projection contracts
- resolver semantics
- conformance rules

## 8.2 A separate protocol may own

- serialization format
- transport
- remote references
- capability negotiation
- version negotiation
- patching and deltas
- persistence
- synchronization
- authoring messages
- asset delivery
- cache policy
- signatures
- authentication and authorization

## 8.3 IV implementation boundary

IV should be treated as a downstream implementation of SES, not the definition of SES.

The recommended relationship is:

```text
SES Specification
      |
SES Protocol
      |
IV Adapter / Runtime
      |
IV Components and Screens
```

The implementation may expose optimizations or host-specific extensions, but those extensions should be namespaced and must not silently redefine canonical SES semantics.

## 8.4 Versioning

Version independently:

```text
SES semantic schema
SES expression schema
SES protocol
Visual Languages
Themes
Renderer
IV implementation
```

Equal version numbers do not imply compatibility. Compatibility should be declared explicitly.
