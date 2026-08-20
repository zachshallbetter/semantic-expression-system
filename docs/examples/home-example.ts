import type {
  BlockDefinition,
  CompositionDefinition,
  ExpressionRecipe,
  VisualLanguage,
} from "../schemas/ses-schema";

export const MediaCard: BlockDefinition = {
  id: "media-card",
  name: "Media Card",
  kind: "content",
  semanticRole: "media-content-summary",
  states: ["default", "hover", "focus", "selected", "disabled"],
  operations: ["open-media"],
  slots: [
    { id: "media", name: "Media", semanticRole: "media", cardinality: "one", content: { type: "element", accepts: ["image"] } },
    { id: "badge", name: "Badge", semanticRole: "annotation", cardinality: "optional", content: { type: "element", accepts: ["badge"] } },
    { id: "title", name: "Title", semanticRole: "title", cardinality: "one", content: { type: "element", accepts: ["heading", "label"] } },
    { id: "subtitle", name: "Subtitle", semanticRole: "subtitle", cardinality: "optional", content: { type: "element", accepts: ["text", "label"] } },
    { id: "meta", name: "Meta", semanticRole: "meta", cardinality: "optional", content: { type: "any" } },
    { id: "action", name: "Action", semanticRole: "action", cardinality: "optional", content: { type: "element", accepts: ["button", "icon-button"] } },
  ],
  behavior: { interactive: true, navigable: true },
};

export const Home: CompositionDefinition = {
  id: "home",
  name: "Home",
  type: "screen",
  sockets: [
    {
      id: "home.hero",
      name: "Hero",
      semanticRole: "primary-introduction",
      accepts: ["hero"],
      multiplicity: "single",
      importance: "primary",
      invariance: {
        semantic: "required",
        behavioral: "required",
        actionIdentity: "required",
        structural: "bounded",
        morphological: "free",
        visual: "free",
      },
      projection: {
        preserve: ["identity", "primary-action", "accessibility-order"],
        transform: ["orientation", "media-placement", "enclosure", "background", "edges", "texture", "pattern", "ornament"],
        mayIntroduce: ["decorative-art", "background-art"],
        failureConditions: ["primary-action-unexposed", "required-content-unreachable"],
      },
      operations: {
        required: ["enter-world"],
        requireExposure: true,
      },
    },
    {
      id: "home.trending",
      name: "Trending",
      semanticRole: "content-discovery",
      accepts: ["media-rail", "media-grid", "ranked-collection"],
      multiplicity: "single",
      importance: "primary",
      invariance: {
        semantic: "required",
        behavioral: "required",
        actionIdentity: "required",
        structural: "bounded",
        morphological: "free",
        visual: "free",
      },
      projection: {
        preserve: ["content-identity", "content-priority", "view-all-operation"],
        transform: ["orientation", "card-topology", "spacing", "alignment", "enclosure"],
        mayIntroduce: ["texture", "pattern", "section-decoration"],
      },
      operations: {
        required: ["open-media", "view-all"],
        requireExposure: true,
      },
    },
  ],
};

export const NeoEdoMediaCard: ExpressionRecipe = {
  layout: {
    display: "grid",
    columns: "minmax(0, 1fr) 42%",
    overflow: "visible",
  },
  morphology: {
    hierarchy: "editorial",
    density: "compact",
    rhythm: "asymmetric",
    enclosure: "soft",
    overlap: "subtle",
  },
  appearance: {
    background: [
      { type: "color", value: "{surface.washi}" },
      { type: "texture", source: "washi-fiber", opacity: 0.28, blendMode: "multiply" },
    ],
    patterns: [
      { source: "seigaiha", placement: "bottom", opacity: 0.06 },
    ],
    edges: [
      { sides: ["top"], style: "brush", source: "dry-brush-edge", width: "4px" },
      { sides: ["left"], style: "solid", color: "{color.vermilion}", width: "2px" },
    ],
    decorations: [
      { type: "seal", source: "seal-small", anchor: "bottom-left", opacity: 0.85 },
    ],
    overflow: "visible",
  },
  slots: {
    media: { placement: "right", image: "sumi-wash" },
    badge: { placement: "top-left", appearance: { background: [{ type: "color", value: "{color.vermilion}" }] } },
    title: { placement: "left", typography: "display.brush" },
    subtitle: { placement: "left", typography: "body.editorial" },
    meta: { placement: "left", typography: "meta.compact" },
  },
};

export const NeoEdo: VisualLanguage = {
  id: "neo-edo",
  name: "Neo-Edo",
  defaultTheme: "neo-edo.ink",
  tokens: {
    primitives: {
      "color.ink": "#0b0b0d",
      "color.parchment": "#d8c7a1",
      "color.vermilion": "#b9382d",
    },
    semantic: {
      "surface.canvas": "{color.ink}",
      "surface.washi": "{color.parchment}",
      "accent.primary": "{color.vermilion}",
    },
  },
  assets: {
    textures: { "washi-fiber": { src: "textures/washi-fiber" } },
    patterns: { seigaiha: { src: "patterns/seigaiha" } },
    edges: { "dry-brush-edge": { src: "edges/dry-brush" } },
    ornaments: { "seal-small": { src: "ornaments/seal-small" } },
  },
  recipes: {
    blocks: {
      "media-card": NeoEdoMediaCard,
    },
  },
};
