# figma-snippets — 리허설(2026-09-05)에서 검증된 use_figma 코드

모든 스니펫은 `figma:figma-use` 스킬을 로드한 뒤 `use_figma`에 그대로 넣는다. 한 호출은 페이지를 최대 한 번만 설정한다. 여러 화면은 한 메시지에서 병렬 호출한다.

## 0. 공통 프렐류드 (모든 스크립트 맨 위)

```js
const page = figma.root.children.find(p => p.name === 'PAGE_NAME'); await figma.setCurrentPageAsync(page);
for (const s of ['Bold','Medium','Regular']) await figma.loadFontAsync({ family: 'Noto Sans KR', style: s });
const vars = await figma.variables.getLocalVariablesAsync(); const V = n => vars.find(v => v.name === n);
const fillVar = (node, n, op) => { const p = figma.variables.setBoundVariableForPaint({ type: 'SOLID', color: { r: 0, g: 0, b: 0 } }, 'color', V(n)); node.fills = [op != null ? { ...p, opacity: op } : p]; };
const strokeVar = (node, n, w) => { node.strokes = [figma.variables.setBoundVariableForPaint({ type: 'SOLID', color: { r: 0, g: 0, b: 0 } }, 'color', V(n))]; node.strokeWeight = w || 1; };
const text = (chars, size, style, colorVar) => { const t = figma.createText(); t.fontName = { family: 'Noto Sans KR', style }; t.characters = chars; t.fontSize = size; fillVar(t, colorVar); return t; };
const row = (gap) => { const r = figma.createFrame(); r.layoutMode = 'HORIZONTAL'; r.itemSpacing = gap; r.fills = []; r.primaryAxisSizingMode = 'AUTO'; r.counterAxisSizingMode = 'AUTO'; return r; };
```

## 1. 페이지 생성 + 변수 컬렉션 (F3 첫 호출)

```js
for (const name of ['Library', 'Screens/PROJECT', 'Presentation']) if (!figma.root.children.find(p => p.name === name)) { const p = figma.createPage(); p.name = name; }
let col = (await figma.variables.getLocalVariableCollectionsAsync()).find(c => c.name === 'PROJECT tokens') || figma.variables.createVariableCollection('PROJECT tokens');
const mode = col.modes[0].modeId;
const hex = h => ({ r: parseInt(h.slice(1,3),16)/255, g: parseInt(h.slice(3,5),16)/255, b: parseInt(h.slice(5,7),16)/255 });
const colors = { 'color/bg': ['#F3F0FF', ['FRAME_FILL','SHAPE_FILL']], 'color/primary': ['#5F33E1', ['FRAME_FILL','SHAPE_FILL','TEXT_FILL','STROKE_COLOR']], /* F2 표에서 채운다 */ };
const existing = await figma.variables.getLocalVariablesAsync('COLOR');
for (const [name, [h, scopes]] of Object.entries(colors)) { let v = existing.find(x => x.name === name && x.variableCollectionId === col.id) || figma.variables.createVariable(name, col, 'COLOR'); v.scopes = scopes; v.setValueForMode(mode, hex(h)); }
return { collectionId: col.id };
```

## 2. 배리언트 세트 — 자식이 잘리지 않게 (필수)

`combineAsVariants` 직후 세트 사이징을 AUTO로 두고 자식을 HUG로 바꾸지 않으면 세트가 자식을 잘라 렌더한다.

**실측 함정(2026-09-05)**: `figma.createComponent()`로 만든 컴포넌트에 속성만 잔뜩 설정하고 자식 노드를 다 붙인 다음에야 `combineAsVariants`를 부르면 `Error: in combineAsVariants: Grouped nodes must be in the same page as the parent`가 난다 — 새로 만든 노드가 어느 페이지에도 속하지 않은 상태로 남아있을 수 있기 때문. **해법**: `figma.createComponent()` 직후, 다른 속성을 만지기 전에 `page.appendChild(component)`부터 호출한다. 자식 노드(텍스트, 벡터, 프레임)도 각각 `createXxx()` 직후 즉시 `parent.appendChild(child)`부터 하고 그다음에 속성을 설정하는 순서를 지킨다 — "다 만들고 마지막에 한 번에 붙이기"가 아니라 "만들자마자 붙이고, 그다음 속성"이 안전한 순서다.

```js
const finishSet = (set, name, x, y) => {
  set.name = name; set.layoutMode = 'HORIZONTAL'; set.itemSpacing = 16;
  set.paddingLeft = set.paddingRight = set.paddingTop = set.paddingBottom = 16;
  set.primaryAxisSizingMode = 'AUTO'; set.counterAxisSizingMode = 'AUTO'; set.clipsContent = false; set.x = x; set.y = y;
  for (const c of set.children) c.layoutSizingVertical = 'HUG';
};
// 예: 버튼
const btns = [];
for (const type of ['primary','secondary']) for (const state of ['default','pressed']) {
  const c = figma.createComponent(); c.name = `type=${type}, state=${state}`; c.layoutMode = 'HORIZONTAL';
  c.primaryAxisAlignItems = 'CENTER'; c.counterAxisAlignItems = 'CENTER'; c.paddingLeft = c.paddingRight = 20; c.paddingTop = c.paddingBottom = 14;
  c.cornerRadius = 999; c.resize(200, 48); c.primaryAxisSizingMode = 'FIXED'; c.counterAxisSizingMode = 'AUTO';
  fillVar(c, type === 'primary' ? 'color/primary' : 'color/surface'); if (type === 'secondary') strokeVar(c, 'color/line');
  const t = text('예약하기', 15, 'Bold', type === 'primary' ? 'color/text-on-primary' : 'color/primary'); c.appendChild(t); t.name = 'label'; btns.push(c);
}
const set = figma.combineAsVariants(btns, page); finishSet(set, 'Button', 0, 0);
return { variants: set.children.map(c => ({ name: c.name, id: c.id })) };  // 화면 조립에 이 ID를 쓴다
```

## 3. 하단 네비 5칸이 390에 들어가게

padding 12, 아이템 고정폭 64, 중앙 FAB 52. 마지막 아이템 우측 끝이 378 ≤ 390.

```js
const nav = figma.createComponent(); nav.name = 'BottomNav'; nav.layoutMode = 'HORIZONTAL'; nav.counterAxisAlignItems = 'CENTER'; nav.primaryAxisAlignItems = 'SPACE_BETWEEN';
nav.paddingLeft = nav.paddingRight = 12; nav.paddingTop = 10; nav.paddingBottom = 12; nav.resize(390, 72); nav.primaryAxisSizingMode = 'FIXED'; nav.counterAxisSizingMode = 'FIXED';
fillVar(nav, 'color/nav-bar'); nav.topLeftRadius = nav.topRightRadius = 24;
for (let i = 0; i < 5; i++) {
  if (i === 2) { const fab = figma.createFrame(); fab.name = 'fab'; fab.layoutMode = 'HORIZONTAL'; fab.primaryAxisAlignItems = 'CENTER'; fab.counterAxisAlignItems = 'CENTER'; fab.resize(52, 52); fab.primaryAxisSizingMode = 'FIXED'; fab.counterAxisSizingMode = 'FIXED'; fab.cornerRadius = 26; fillVar(fab, 'color/primary'); fab.appendChild(text('+', 26, 'Regular', 'color/text-on-primary')); nav.appendChild(fab); continue; }
  const item = figma.createFrame(); item.name = 'nav/' + LABELS[i]; item.layoutMode = 'VERTICAL'; item.counterAxisAlignItems = 'CENTER'; item.itemSpacing = 4; item.fills = []; item.resize(64, 40); item.primaryAxisSizingMode = 'AUTO'; item.counterAxisSizingMode = 'FIXED'; item.resize(64, 40);
  item.appendChild(ICON(i)); item.appendChild(text(LABELS[i], 10, 'Medium', i === 0 ? 'color/primary' : 'color/text-secondary')); nav.appendChild(item);
}
```

## 4. 화면 골격 + 인스턴스 텍스트 오버라이드

```js
const inst = async (id, ov) => { const c = await figma.getNodeByIdAsync(id); const i = c.createInstance(); for (const [k, v] of Object.entries(ov || {})) { const t = i.findOne(n => n.type === 'TEXT' && n.name === k); if (t) t.characters = v; } return i; };
const s = figma.createFrame(); s.name = 'Screen/NAME'; s.layoutMode = 'VERTICAL'; s.resize(390, 844); s.primaryAxisSizingMode = 'FIXED'; s.counterAxisSizingMode = 'FIXED'; s.resize(390, 844); fillVar(s, 'color/bg'); s.x = X; s.y = 0; s.clipsContent = true;
const tb = await inst(TOPBAR_ID, { title: '화면 제목' }); s.appendChild(tb); tb.layoutSizingHorizontal = 'FILL';
const ct = figma.createFrame(); ct.name = 'Section/Content'; ct.layoutMode = 'VERTICAL'; ct.itemSpacing = 12; ct.paddingLeft = ct.paddingRight = 16; ct.paddingTop = 8; ct.paddingBottom = 16; ct.fills = []; ct.clipsContent = true;
s.appendChild(ct); ct.layoutSizingHorizontal = 'FILL'; ct.layoutSizingVertical = 'FILL';
const cell = await inst(CELL_ID, { meta: '…', title: '…', time: '…' }); ct.appendChild(cell); cell.layoutSizingHorizontal = 'FILL';
const nav = await inst(NAV_ID); s.appendChild(nav); nav.layoutSizingHorizontal = 'FILL';
// 장식 블롭: 소스 수준으로 절제(불투명도 0.45, 상단 1/3)
const e = figma.createEllipse(); e.name = 'deco/blob'; e.resize(190, 190); fillVar(e, 'color/tint-pink', 0.9); e.opacity = 0.45; e.effects = [{ type: 'LAYER_BLUR', radius: 70, visible: true }]; s.insertChild(0, e); e.layoutPositioning = 'ABSOLUTE'; e.x = -60; e.y = 40;
return { createdNodeIds: [s.id] };
```

## 5. 화면별 하단 네비 활성 탭 지정 (G2)

```js
const paint = (n) => figma.variables.setBoundVariableForPaint({ type: 'SOLID', color: { r: 0, g: 0, b: 0 } }, 'color', V(n));
const active = { 'Screen/Home': '홈', 'Screen/Hospitals': '병원' /* … */ };
for (const s of page.children.filter(n => n.name.startsWith('Screen/'))) {
  const nav = s.findOne(n => n.type === 'INSTANCE' && n.name === 'BottomNav'); if (!nav) continue;
  for (const item of nav.findAll(n => n.name && n.name.startsWith('nav/'))) {
    const on = item.name === 'nav/' + active[s.name];
    const t = item.findOne(n => n.type === 'TEXT'); const ic = item.findOne(n => n.type === 'ELLIPSE' || n.type === 'RECTANGLE');
    if (t) t.fills = [paint(on ? 'color/primary' : 'color/text-secondary')]; if (ic) ic.fills = [paint(on ? 'color/primary' : 'color/text-secondary')];
  }
}
```

## 6. 프레젠테이션 페이지 (G3)

```js
const board = figma.createFrame(); board.name = 'Presentation/PROJECT'; board.resize(3400, 1180); fillVar(board, 'color/bg');
// 커버 카드(보라, 520×844) + 화면 클론을 x = 660부터 450 간격으로, 라벨 text 위에, 화면 사이 '→'
const src = await figma.getNodeByIdAsync(SCREEN_ID); const c = src.clone(); board.appendChild(c); c.x = 660; c.y = 160; c.cornerRadius = 28; c.clipsContent = true;
c.effects = [{ type: 'DROP_SHADOW', color: { r: 0.33, g: 0.29, b: 0.44, a: 0.18 }, offset: { x: 24, y: 24 }, radius: 50, visible: true, blendMode: 'NORMAL' }];
```
화면을 고친 뒤에는 클론을 지우고 다시 클론한다(클론은 라이브 링크가 아니다).

## 7. A단계 측정 스크립트

```js
const screens = page.children.filter(n => n.name.startsWith('Screen/'));
const forbidden = ['Task','To-do','Project','할 일','프로젝트' /* 소스 도메인 단어 */];
let inst = 0, drawn = 0, boundFills = 0, totalFills = 0, hits = [], off = [];
for (const s of screens) for (const n of s.findAll(() => true)) {
  const inInst = (() => { let p = n.parent; while (p && p.id !== s.id) { if (p.type === 'INSTANCE') return true; p = p.parent; } return false; })();
  if (n.type === 'INSTANCE' && !inInst) inst++;
  if (!inInst && n.type !== 'INSTANCE' && ['FRAME','RECTANGLE','ELLIPSE','POLYGON'].includes(n.type) && !n.name.startsWith('deco/')) drawn++;
  if ('fills' in n && Array.isArray(n.fills) && !inInst) for (const f of n.fills) if (f.type === 'SOLID' && f.visible !== false) { totalFills++; if (f.boundVariables && f.boundVariables.color) boundFills++; }
  if (n.type === 'TEXT') for (const w of forbidden) if (n.characters.includes(w)) hits.push({ screen: s.name, text: n.characters });
  if (!inInst && n.type !== 'INSTANCE' && 'layoutMode' in n && n.layoutMode !== 'NONE') for (const k of ['paddingLeft','paddingRight','paddingTop','paddingBottom','itemSpacing']) if (n[k] % 4 !== 0) off.push({ screen: s.name, node: n.name, k, v: n[k] });
}
return { reuse: +(inst / (inst + drawn)).toFixed(2), tokens: +(boundFills / totalFills).toFixed(2), forbidden: hits, offGrid: off.length };
```
게이트: reuse ≥ 0.70, tokens ≥ 0.90, forbidden 0건.

## 8. 알려진 함정

- Manrope·Inter에는 한글이 없다. 한글 텍스트는 Noto Sans KR로 만든다.
- `figma.currentPage = page`는 안 된다. 항상 `await figma.setCurrentPageAsync(page)`.
- `layoutSizingHorizontal = 'FILL'`은 `appendChild` 이후에만 된다.
- 텍스트를 만들거나 바꾸기 전에 그 폰트를 `loadFontAsync`로 로드한다.
- 배리언트 세트는 §2 `finishSet` 없이 두면 자식이 잘린다.
- 페이지 전체 렌더는 `get_screenshot(페이지 ID)`. 화면 6장이 한 이미지로 온다.
- **실측(2026-09-05)**: `figma.createFrame()`은 기본 높이가 100px이다. 오토레이아웃 프레임에 `counterAxisSizingMode = 'FIXED'`를 (기본값 그대로든 실수로든) 남겨두고 `resize()`나 `layoutSizingVertical = 'HUG'`를 안 하면, 내용이 텍스트 한 줄뿐이어도 프레임이 100px로 남아 빈 공간이 크게 생긴다 — 배경색이 있는 배너·태그 프레임에서 특히 눈에 띈다("텍스트는 위쪽에 있고 아래 3/4는 배경색만 있는 이상한 박스"). **해법**: 컨텐츠에 맞춰 줄어들어야 하는 프레임은 생성 직후 `counterAxisSizingMode = 'AUTO'`(부모 기준) 또는 `layoutSizingVertical = 'HUG'`(자식 기준, `appendChild` 이후)를 명시적으로 설정한다. 스크린샷에서 "박스 크기가 내용보다 이상하게 크다"가 보이면 제일 먼저 이 sizing 모드부터 확인한다.
- **실측(2026-09-05)**: `node.opacity = 0.15`를 프레임에 걸면 그 프레임의 **자식까지 전부** 반투명해진다(텍스트 포함). 배경만 옅게 하고 싶으면 프레임의 `opacity`가 아니라 `fills` 배열의 paint 객체 자체에 `opacity: 0.15`를 넣는다(`{ type: 'SOLID', color: {...}, opacity: 0.15 }` 또는 `setBoundVariableForPaint(..., { opacity: 0.15 })`로 만든 paint). 텍스트는 별도로 완전 불투명하게 색만 진하게 준다.
