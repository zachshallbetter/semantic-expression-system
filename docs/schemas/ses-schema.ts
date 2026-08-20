export type ID = string;
export type TokenRef = `--${string}` | `{${string}}` | string;

export type SemanticState =
  | "default" | "hover" | "focus" | "pressed" | "selected" | "active"
  | "disabled" | "loading" | "error" | "success" | "warning"
  | "read" | "unread" | "owned" | "locked" | string;

export type InvarianceRequirement = "required" | "bounded" | "free";

export interface ElementDefinition {
  id: ID;
  kind: string;
  role?: string;
  variants?: string[];
  states?: SemanticState[];
  operations?: ID[];
  accessibility?: {
    role?: string;
    labelRequired?: boolean;
    keyboardInteractive?: boolean;
  };
}

export interface SlotDefinition {
  id: ID;
  name: string;
  semanticRole: string;
  cardinality: "one" | "optional" | "many";
  content:
    | { type: "element"; accepts?: ID[] }
    | { type: "block"; accepts?: ID[] }
    | { type: "content"; accepts?: string[] }
    | { type: "any" };
  priority?: number;
  fallback?: unknown;
}

export interface BlockDefinition {
  id: ID;
  name: string;
  kind: string;
  semanticRole: string;
  slots: SlotDefinition[];
  variants?: string[];
  states?: SemanticState[];
  operations?: ID[];
  behavior?: {
    interactive?: boolean;
    selectable?: boolean;
    navigable?: boolean;
    expandable?: boolean;
    dismissible?: boolean;
  };
  constraints?: {
    requiredSlots?: ID[];
    mutuallyExclusiveSlots?: ID[][];
    minItems?: number;
    maxItems?: number;
  };
}

export interface SocketAcceptedBlock {
  block: ID;
  variants?: string[];
  capabilities?: string[];
}

export interface InvarianceProfile {
  semantic?: InvarianceRequirement;
  behavioral?: InvarianceRequirement;
  actionIdentity?: InvarianceRequirement;
  structural?: InvarianceRequirement;
  morphological?: InvarianceRequirement;
  visual?: InvarianceRequirement;
}

export interface ProjectionContract {
  preserve?: string[];
  transform?: string[];
  mayOmit?: string[];
  mayIntroduce?: string[];
  failureConditions?: string[];
  tolerance?: Record<string, unknown>;
}

export interface OperationContract {
  required?: ID[];
  optional?: ID[];
  requireExposure?: boolean;
  requireSignaling?: boolean;
}

export interface SocketDefinition {
  id: ID;
  name: string;
  semanticRole: string;
  accepts: Array<ID | SocketAcceptedBlock>;
  multiplicity: "single" | "optional" | "repeat";
  importance?: "primary" | "secondary" | "tertiary";
  order?: number;
  constraints?: {
    min?: number;
    max?: number;
    preferredSpan?: "narrow" | "medium" | "wide" | "full";
    overflow?: "wrap" | "scroll" | "clip" | "paginate" | "none";
    required?: boolean;
  };
  invariance?: InvarianceProfile;
  projection?: ProjectionContract;
  operations?: OperationContract;
  responsive?: {
    priority?: number;
    collapseInto?: ID;
    hideBelow?: string;
    reorderAllowed?: boolean;
    preserveRequiredOperations?: boolean;
  };
}

export interface CompositionDefinition {
  id: ID;
  name: string;
  type: "screen" | "page" | "flow" | "shell" | "section";
  sockets: SocketDefinition[];
  hierarchy?: CompositionNode[];
}

export interface CompositionNode {
  socket: ID;
  children?: CompositionNode[];
  relation?: "sequence" | "group" | "parallel" | "aside" | "overlay";
  priority?: number;
}

export interface MorphologyRecipe {
  hierarchy?: string;
  topology?: string;
  density?: string;
  rhythm?: string;
  alignment?: string;
  symmetry?: string;
  enclosure?: string;
  continuity?: string;
  direction?: string;
  overlap?: string;
  fragmentation?: string;
  visualWeight?: Record<string, number>;
}

export type BackgroundLayer =
  | { type: "color"; value: string; opacity?: number; blendMode?: string }
  | { type: "gradient"; value: string; opacity?: number; blendMode?: string }
  | { type: "texture"; source: ID; opacity?: number; blendMode?: string; mask?: string }
  | { type: "pattern"; source: ID; opacity?: number; blendMode?: string; mask?: string }
  | { type: "image"; source: ID; fit?: string; position?: string; opacity?: number; blendMode?: string }
  | { type: "custom"; source: ID; props?: Record<string, unknown> };

export interface EdgeLayer {
  sides: "all" | Array<"top" | "right" | "bottom" | "left">;
  style: string;
  width?: string;
  color?: string;
  opacity?: number;
  source?: ID;
  offset?: string;
  inset?: boolean;
  start?: string;
  end?: string;
  repeat?: "stretch" | "repeat" | "round";
  mask?: string;
}

export interface TextureLayer {
  source: ID;
  opacity?: number;
  blendMode?: string;
  scale?: string | number;
  direction?: string;
  mask?: string;
}

export interface PatternLayer {
  source: ID;
  placement?: string;
  opacity?: number;
  blendMode?: string;
  scale?: string | number;
  rotation?: number;
  density?: number;
  mask?: string;
}

export interface DecorationLayer {
  id?: ID;
  type: string;
  source?: ID;
  anchor?: string;
  x?: string;
  y?: string;
  width?: string;
  height?: string;
  rotation?: number;
  opacity?: number;
  blendMode?: string;
  zIndex?: number;
  bleed?: Partial<Record<"top" | "right" | "bottom" | "left", string>>;
}

export interface AppearanceRecipe {
  background?: BackgroundLayer[];
  textures?: TextureLayer[];
  patterns?: PatternLayer[];
  edges?: EdgeLayer[];
  decorations?: DecorationLayer[];
  mask?: string | Record<string, unknown>;
  clip?: string | Record<string, unknown>;
  bleed?: Partial<Record<"top" | "right" | "bottom" | "left", string>>;
  overflow?: "visible" | "hidden" | "clip";
  opacity?: number;
  blendMode?: string;
  filter?: string;
  backdrop?: string;
}

export interface LayoutRecipe {
  display?: "block" | "flex" | "grid" | "overlay" | string;
  flow?: string;
  columns?: string;
  rows?: string;
  areas?: string[];
  align?: string;
  justify?: string;
  gap?: string;
  padding?: string;
  margin?: string;
  aspectRatio?: string;
  overflow?: string;
  position?: string;
  transform?: string;
}

export interface SlotPresentationRecipe {
  placement?: string;
  order?: number;
  gridArea?: string;
  width?: string;
  height?: string;
  margin?: string;
  padding?: string;
  typography?: ID;
  image?: ID;
  appearance?: AppearanceRecipe;
  visibility?: string;
}

export interface ExpressionRecipe {
  layout?: LayoutRecipe;
  morphology?: MorphologyRecipe;
  appearance?: AppearanceRecipe;
  typography?: ID | Record<string, ID>;
  image?: ID;
  slots?: Record<ID, SlotPresentationRecipe>;
  state?: Record<SemanticState, Partial<ExpressionRecipe>>;
  variants?: Record<string, Partial<ExpressionRecipe>>;
  responsive?: Record<string, Partial<ExpressionRecipe>>;
}

export interface TokenRegistry {
  primitives?: Record<string, string | number>;
  semantic?: Record<string, string | number>;
  roles?: Record<string, string | number>;
}

export interface AssetRegistry {
  fonts?: Record<ID, unknown>;
  icons?: Record<ID, unknown>;
  textures?: Record<ID, unknown>;
  patterns?: Record<ID, unknown>;
  masks?: Record<ID, unknown>;
  edges?: Record<ID, unknown>;
  backgrounds?: Record<ID, unknown>;
  ornaments?: Record<ID, unknown>;
  images?: Record<ID, unknown>;
  custom?: Record<ID, unknown>;
}

export interface VisualLanguage {
  id: ID;
  name: string;
  description?: string;
  philosophy?: string;
  defaultTheme: ID;
  tokens: TokenRegistry;
  assets?: AssetRegistry;
  foundations?: Record<string, unknown>;
  recipes: {
    elements?: Record<ID, ExpressionRecipe>;
    blocks?: Record<ID, ExpressionRecipe>;
    sockets?: Record<ID, ExpressionRecipe>;
    compositions?: Record<ID, ExpressionRecipe>;
  };
}

export interface ThemeDefinition {
  id: ID;
  name: string;
  language: ID;
  mode?: string;
  tokenOverrides?: Record<string, string | number>;
  assetOverrides?: Partial<AssetRegistry>;
  recipeOverrides?: VisualLanguage["recipes"];
}

export interface UIExpressionState {
  visualLanguage: ID;
  theme: ID;
  styleOptions?: Record<string, unknown>;
  viewport?: string;
  reducedMotion?: boolean;
  highContrast?: boolean;
}
