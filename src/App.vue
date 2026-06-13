<script setup>
import { computed, onMounted, reactive, ref, watch } from "vue";

const navItems = [
  { key: "workbench", label: "工作台", icon: "desktop" },
  { key: "account", label: "账号档案", icon: "user" },
  { key: "assets", label: "素材中心", icon: "grid" },
  { key: "editor", label: "镜头剪辑", icon: "video" },
  { key: "tasks", label: "任务中心", icon: "play" },
  { key: "publish", label: "发布账号管理", icon: "card" },
  { key: "schedule", label: "发布排期", icon: "calendar" },
  { key: "settings", label: "系统设置", icon: "gear" }
];

const stats = [
  { value: 0, label: "已生成视频", icon: "video", theme: "blue" },
  { value: 0, label: "正在生成任务", icon: "spark", theme: "green" },
  { value: 0, label: "本月已发布视频", icon: "calendar", theme: "gold" },
  { value: 0, label: "异常任务", icon: "warning", theme: "red" }
];

const themeOptions = [
  { key: "skyline", label: "云海蓝" },
  { key: "sunrise", label: "暖日橙" },
  { key: "mint", label: "青岚绿" }
];

const themeStorageKey = "aishiping-theme";
const activeNav = ref("publish");
const activeTheme = ref("skyline");
const isSidebarCollapsed = ref(false);
const profiles = ref([
  {
    id: 1,
    name: "默认人设",
    summary: "15 项信息"
  }
]);

const accountForm = reactive({
  profileName: "默认人设",
  nickname: "大家叫我江姐",
  birthYear: "八四年出生",
  gender: "女",
  hometown: "江苏南京人",
  brandName: "江姐做电商",
  businessType: "电商",
  address: "深圳市福田区",
  investmentStory: "花了50万在福田开了一家电商公司",
  yearsInBusiness: "15年",
  setbackStory:
    "刚开始做的时候，也走过不少弯路，选品、供应链、运营都踩过坑，前期投入了很多成本但效果并不理想。后来我们重新梳理产品和用户需求，只专注把核心产品做好，从品质、发货、售后到复购体验一点点优化，才慢慢把口碑和销量做起来。",
  trustReason:
    "我们一直坚持以用户体验为核心，认真做好每一个产品细节，从选品标准、品质把控到售后服务都尽量做到稳定和透明。不是只追求短期销量，而是更看重复购率和用户口碑，让顾客买得放心、用得满意。",
  targetGoal:
    "希望把真正高性价比、实用、靠谱的产品带给更多消费者，让大家在电商平台上也能更省心地买到值得信赖的好东西。",
  audience:
    "注重品质和性价比的消费人群，尤其是日常有网购习惯、重视实用性、关注购物体验和售后服务的用户。",
  sellingPoint:
    "精选产品、品质稳定、价格合理、发货及时、售后完善，兼顾实用性与性价比，帮助消费者减少踩坑成本，提升购买体验。",
  productPricing:
    "主营高性价比优选商品，覆盖日常消费和实用需求场景。价格设置坚持实在透明，兼顾品质与预算，让用户花更合适的钱买到更合适的产品。"
});

const accountBasicFields = [
  [
    { key: "nickname", label: "别人怎么称呼你" },
    { key: "birthYear", label: "出生年份" }
  ],
  [
    { key: "gender", label: "性别" },
    { key: "hometown", label: "哪里人" }
  ],
  [
    { key: "brandName", label: "门店或品牌名称" },
    { key: "businessType", label: "行业或主营业务" }
  ]
];

const accountLongFields = [
  { key: "address", label: "门店地址或商圈", type: "input" },
  { key: "investmentStory", label: "投了多少钱干了什么事", type: "textarea", rows: 2 },
  { key: "yearsInBusiness", label: "做了多少年", type: "input" },
  { key: "setbackStory", label: "遇到过什么挫折怎么解决的", type: "textarea", rows: 3 },
  { key: "trustReason", label: "我为什么值得信赖", type: "textarea", rows: 3 },
  { key: "targetGoal", label: "目标或者期望", type: "textarea", rows: 3 },
  { key: "audience", label: "目标客群", type: "textarea", rows: 2 },
  { key: "sellingPoint", label: "特色卖点", type: "textarea", rows: 2 },
  { key: "productPricing", label: "产品介绍和价格", type: "textarea", rows: 2 }
];

const materialDirectory = ref("C:\\videomix_data\\混剪素材");
const materialSearch = ref("");
const materialStats = [
  { value: 0, label: "已接入文件夹", theme: "blue" },
  { value: 0, label: "可用片段总数", theme: "green" },
  { value: 0, label: "不支持的文件", theme: "orange" },
  { value: 0, label: "素材不足类别", theme: "red" }
];
const editorTemplateCategories = [
  { key: "store", label: "实体店" },
  { key: "enterprise", label: "工厂或企业" },
  { key: "delivery", label: "带货" },
  { key: "custom", label: "自定义模板" }
];
const selectedTemplateCategory = ref("enterprise");
const editorTemplates = [
  { id: 1, title: "工厂", tag: "工厂或企业", count: "共 9 个镜头文案位" },
  { id: 2, title: "保险", tag: "工厂或企业", count: "共 8 个镜头文案位" },
  { id: 3, title: "财税", tag: "工厂或企业", count: "共 8 个镜头文案位" },
  { id: 4, title: "教培", tag: "工厂或企业", count: "共 9 个镜头文案位" },
  { id: 5, title: "金融", tag: "工厂或企业", count: "共 9 个镜头文案位" },
  { id: 6, title: "律所", tag: "工厂或企业", count: "共 8 个镜头文案位" }
];
const selectedTemplateId = ref(6);
const editorPersona = ref("默认人设");
const editorVoice = ref("选择音色");
const editorShotSeed = ref(4);
const editorShots = ref([
  {
    id: 1,
    title: "镜头1",
    templateText: "我在南京干12年律师了",
    rewriteText: "",
    materialType: "人物"
  },
  {
    id: 2,
    title: "镜头2",
    templateText: "从大律所辞职，自己开了个小律所",
    rewriteText: "",
    materialType: "门头"
  },
  {
    id: 3,
    title: "镜头3",
    templateText: "这十几年里，接触了很多婚姻家事和经济纠纷案件",
    rewriteText: "",
    materialType: "办公环境"
  }
]);
const batchStorage = reactive({
  cacheDir: "C:\\videomix_data\\工作缓存",
  outputDir: "C:\\videomix_data\\成片"
});
const batchTasks = ref([]);
const publishPlatforms = ["抖音", "小红书", "视频号", "快手"];
const selectedPublishPlatform = ref("抖音");
const publishSearch = ref("");
const publishStats = [
  { value: 0, label: "当前平台账号", theme: "blue" },
  { value: 0, label: "已登录账号", theme: "green" },
  { value: 0, label: "待登录账号", theme: "orange" }
];
const scheduleStats = [
  { value: 0, label: "待排期视频", theme: "blue" },
  { value: 0, label: "排期中", theme: "green" },
  { value: 0, label: "待补标题 / 话题", theme: "orange" },
  { value: 0, label: "已有发布结果", theme: "purple" }
];
const scheduleTabs = ["未排期", "排期中", "已有结果"];
const selectedScheduleTab = ref("未排期");
const schedulePublishMode = ref("自动发布");
const isRewriteSettingsOpen = ref(true);
const isLogsOpen = ref(true);
const systemSettings = reactive({
  resolution: "1080 × 1920（竖屏）",
  frameRate: 30,
  encoder: "快速剪辑（GPU）",
  quality: "中档（3M）",
  minimaxKey: "",
  aliyunKey: "",
  rewritePrompt: "更像真实本地商家口播，语言自然接地气，不要太广告腔，避免夸张承诺。"
});
const systemSettingsOptions = {
  resolutions: ["1080 × 1920（竖屏）", "720 × 1280（竖屏）", "1920 × 1080（横屏）"],
  encoders: ["快速剪辑（GPU）", "平衡编码（CPU）", "高质量编码（GPU）"],
  qualities: ["低档（2M）", "中档（3M）", "高清（5M）"]
};
const defaultRewritePrompt = "更像真实本地商家口播，语言自然接地气，不要太广告腔，避免夸张承诺。";
const systemLogs = ref([
  '[2026-06-12 17:54:08] [WARN] main.fs.readDir.missing',
  '{',
  '  "dirPath": "C:\\\\videomix_data\\\\混剪素材\\\\教案试卷展示",',
  '  "code": "ENOENT"',
  '}',
  "",
  '[2026-06-12 17:54:07] [WARN] main.fs.readDir.missing',
  '{',
  '  "dirPath": "C:\\\\videomix_data\\\\混剪素材\\\\办公环境",',
  '  "code": "ENOENT"',
  '}'
]);

const referenceRows = [
  { label: "账号档案名称", key: "profileName" },
  { label: "别人怎么称呼你", key: "nickname" },
  { label: "出生年份", key: "birthYear" },
  { label: "性别", key: "gender" },
  { label: "哪里人", key: "hometown" },
  { label: "门店或品牌名称", key: "brandName" },
  { label: "行业或主营业务", key: "businessType" },
  { label: "门店地址或商圈", key: "address" },
  { label: "投了多少钱干了什么事", key: "investmentStory" },
  { label: "做了多少年", key: "yearsInBusiness" },
  { label: "遇到过什么挫折怎么解决的", key: "setbackStory" },
  { label: "我为什么值得信赖", key: "trustReason" },
  { label: "目标或者期望", key: "targetGoal" },
  { label: "目标客群", key: "audience" },
  { label: "特色卖点", key: "sellingPoint" },
  { label: "产品介绍和价格", key: "productPricing" }
];

const accountReference = computed(() =>
  referenceRows
    .map(({ label, key }) => ({
      label,
      value: accountForm[key]?.trim() || "未填写"
    }))
);
const activeNavMeta = computed(
  () => navItems.find((item) => item.key === activeNav.value) || navItems[0]
);
const selectedTemplateTitle = computed(
  () => editorTemplates.find((template) => template.id === selectedTemplateId.value)?.title || "未命名模板"
);

function applyTheme(themeKey) {
  if (typeof document === "undefined") {
    return;
  }

  document.documentElement.dataset.theme = themeKey;
}

function toggleSidebar() {
  isSidebarCollapsed.value = !isSidebarCollapsed.value;
}

function renumberEditorShots() {
  editorShots.value.forEach((shot, index) => {
    shot.title = `镜头${index + 1}`;
  });
}

function addEditorShot() {
  editorShots.value.push({
    id: editorShotSeed.value++,
    title: `镜头${editorShots.value.length + 1}`,
    templateText: "",
    rewriteText: "",
    materialType: ""
  });
}

function removeEditorShot(id) {
  if (editorShots.value.length === 1) {
    return;
  }

  editorShots.value = editorShots.value.filter((shot) => shot.id !== id);
  renumberEditorShots();
}

function createBatchTask() {
  batchTasks.value.push({
    id: Date.now(),
    sequence: batchTasks.value.length + 1,
    templateType: selectedTemplateTitle.value,
    shotCount: editorShots.value.length,
    status: "待生成",
    result: "--"
  });
  activeNav.value = "tasks";
}

function removeBatchTask(id) {
  batchTasks.value = batchTasks.value
    .filter((task) => task.id !== id)
    .map((task, index) => ({
      ...task,
      sequence: index + 1
    }));
}

function clearAccountForm() {
  for (const key of Object.keys(accountForm)) {
    accountForm[key] = "";
  }
}

function changeFrameRate(delta) {
  systemSettings.frameRate = Math.min(60, Math.max(1, systemSettings.frameRate + delta));
}

function restoreRewriteDefault() {
  systemSettings.rewritePrompt = defaultRewritePrompt;
}

function clearSystemLogs() {
  systemLogs.value = [];
}

function setTheme(themeKey) {
  activeTheme.value = themeKey;
}

onMounted(() => {
  try {
    const savedTheme = window.localStorage.getItem(themeStorageKey);

    if (themeOptions.some((item) => item.key === savedTheme)) {
      activeTheme.value = savedTheme;
    }
  } catch {
    // Ignore storage failures and keep the default theme.
  }

  applyTheme(activeTheme.value);
});

watch(activeTheme, (themeKey) => {
  applyTheme(themeKey);

  try {
    window.localStorage.setItem(themeStorageKey, themeKey);
  } catch {
    // Ignore storage failures and still let the theme work for this session.
  }
});

function iconMarkup(name) {
  const icons = {
    arrow: `
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round">
        <path d="M14.5 6.5 9 12l5.5 5.5" />
      </svg>
    `,
    desktop: `
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <rect x="4" y="5" width="16" height="11" rx="2"></rect>
        <path d="M10 19h4M8 16h8"></path>
      </svg>
    `,
    user: `
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 13a4 4 0 1 0 0-8a4 4 0 0 0 0 8Z"></path>
        <path d="M5 20a7 7 0 0 1 14 0"></path>
      </svg>
    `,
    grid: `
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <path d="M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z"></path>
      </svg>
    `,
    video: `
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <rect x="3.5" y="6.5" width="11" height="11" rx="2"></rect>
        <path d="m15 10 5-3v10l-5-3"></path>
      </svg>
    `,
    play: `
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="8"></circle>
        <path d="m10 8 6 4-6 4z"></path>
      </svg>
    `,
    card: `
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <rect x="4" y="6" width="16" height="12" rx="2"></rect>
        <path d="M8 10h8M8 14h4"></path>
      </svg>
    `,
    calendar: `
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <rect x="4" y="5" width="16" height="15" rx="2"></rect>
        <path d="M8 3v4M16 3v4M4 10h16M8 13h.01M12 13h.01M16 13h.01M8 17h.01M12 17h.01"></path>
      </svg>
    `,
    gear: `
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 8.5A3.5 3.5 0 1 0 12 15.5A3.5 3.5 0 1 0 12 8.5Z"></path>
        <path d="M19.4 15a1 1 0 0 0 .2 1.1l.1.1a2 2 0 0 1-2.8 2.8l-.1-.1a1 1 0 0 0-1.1-.2 1 1 0 0 0-.6.9V20a2 2 0 0 1-4 0v-.2a1 1 0 0 0-.6-.9 1 1 0 0 0-1.1.2l-.1.1a2 2 0 0 1-2.8-2.8l.1-.1a1 1 0 0 0 .2-1.1 1 1 0 0 0-.9-.6H4a2 2 0 0 1 0-4h.2a1 1 0 0 0 .9-.6 1 1 0 0 0-.2-1.1l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1 1 0 0 0 1.1.2 1 1 0 0 0 .6-.9V4a2 2 0 0 1 4 0v.2a1 1 0 0 0 .6.9 1 1 0 0 0 1.1-.2l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1 1 0 0 0-.2 1.1 1 1 0 0 0 .9.6H20a2 2 0 0 1 0 4h-.2a1 1 0 0 0-.4 1.9"></path>
      </svg>
    `,
    spark: `
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M18.4 5.6l-2.8 2.8M8.4 15.6l-2.8 2.8"></path>
      </svg>
    `,
    warning: `
      <svg viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 2.8a9.2 9.2 0 1 0 0 18.4a9.2 9.2 0 0 0 0-18.4Zm-.9 4.9h1.8v6.1h-1.8V7.7Zm0 8h1.8v1.8h-1.8v-1.8Z"></path>
      </svg>
    `,
    folder: `
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <path d="M3.5 7.5A2.5 2.5 0 0 1 6 5h4l1.8 2H18a2.5 2.5 0 0 1 2.5 2.5v7A2.5 2.5 0 0 1 18 19H6a2.5 2.5 0 0 1-2.5-2.5v-9Z"></path>
      </svg>
    `,
    refresh: `
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <path d="M20 11a8 8 0 0 0-14.8-4M4 13a8 8 0 0 0 14.8 4"></path>
        <path d="M4 4v4h4M20 20v-4h-4"></path>
      </svg>
    `,
    plusSquare: `
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <rect x="4" y="4" width="16" height="16" rx="2"></rect>
        <path d="M12 8v8M8 12h8"></path>
      </svg>
    `,
    search: `
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="11" cy="11" r="6"></circle>
        <path d="m20 20-4.2-4.2"></path>
      </svg>
    `,
    logout: `
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <path d="M9 20H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h3"></path>
        <path d="M16 17l5-5-5-5"></path>
        <path d="M21 12H9"></path>
      </svg>
    `
  };

  return icons[name] || icons.desktop;
}
</script>

<template>
      <div
        class="page-shell"
        :class="{ 'sidebar-collapsed': isSidebarCollapsed }"
      >
    <aside class="sidebar">
      <div class="sidebar-card">
        <div class="brand-card">
          <div class="brand-icon" aria-hidden="true">
            <span class="brand-icon-core" />
            <span class="brand-icon-orbit" />
          </div>
          <div v-if="!isSidebarCollapsed" class="brand-sub">AI创舰学院</div>
        </div>

        <button
          class="menu-button icon-shell"
          :class="{ collapsed: isSidebarCollapsed }"
          type="button"
          :aria-label="isSidebarCollapsed ? '展开侧栏' : '折叠侧栏'"
          @click="toggleSidebar"
          v-html="iconMarkup('arrow')"
        />

        <nav class="nav-list">
          <button
            v-for="item in navItems"
            :key="item.key"
            class="nav-item"
            :class="{ active: activeNav === item.key }"
            type="button"
            @click="activeNav = item.key"
          >
            <span class="icon-shell nav-icon" v-html="iconMarkup(item.icon)" />
            <span v-if="!isSidebarCollapsed">{{ item.label }}</span>
          </button>
        </nav>

      </div>
    </aside>

    <main class="dashboard">
      <header class="topbar panel">
        <div class="topbar-copy">
          <h1>{{ activeNavMeta.label }}</h1>
        </div>

        <div class="topbar-tools">
          <div class="theme-switcher">
            <div class="theme-switcher-buttons">
              <button
                v-for="theme in themeOptions"
                :key="theme.key"
                type="button"
                class="theme-button"
                :class="{ active: activeTheme === theme.key }"
                @click="setTheme(theme.key)"
              >
                <span class="theme-button-swatch" :class="`theme-swatch-${theme.key}`" />
                <span>{{ theme.label }}</span>
              </button>
            </div>
          </div>

        </div>
      </header>

      <section v-if="activeNav === 'workbench'" class="content-area">
        <div class="content-main">
          <h2 class="section-title">工作台</h2>

          <div class="stats-grid">
            <article
              v-for="stat in stats"
              :key="stat.label"
              class="stat-card panel"
              :class="`theme-${stat.theme}`"
            >
              <div class="stat-icon icon-shell" v-html="iconMarkup(stat.icon)" />
              <div class="stat-copy">
                <div class="stat-value">{{ stat.value }}</div>
                <div class="stat-label">{{ stat.label }}</div>
              </div>
            </article>
          </div>

          <section class="task-panel panel">
            <div class="panel-head">
              <h3>最近任务</h3>
              <button type="button" class="text-link">查看全部</button>
            </div>
            <div class="task-empty">
              <h4>暂无混剪任务</h4>
              <p>请先在镜头剪辑中配置模板与素材，创建任务后到任务中心合成。</p>
              <button type="button" class="primary-button">去镜头剪辑</button>
            </div>
          </section>

          <div class="ghost-action-wrap">
            <button type="button" class="ghost-button">新建一个月的视频任务</button>
          </div>
        </div>

        <aside class="content-side">
          <section class="publish-panel panel">
            <div class="publish-head">
              <span class="icon-shell publish-icon" v-html="iconMarkup('card')" />
              <div>
                <h3>暂无发布账号</h3>
                <p>添加账号后会在这里显示登录检测结果</p>
              </div>
            </div>
            <div class="publish-meta">0 个账号　最近检测：未检测</div>
            <button type="button" class="secondary-button">发布账号管理</button>
          </section>
        </aside>
      </section>

      <section v-else-if="activeNav === 'account'" class="account-page">
        <h2 class="section-title">账号档案</h2>

        <div class="account-shell panel">
          <aside class="account-sidebar">
            <div class="account-list panel">
              <div class="account-list-head">
                <div>
                  <h3>账号档案</h3>
                  <p>共 {{ profiles.length }} 个</p>
                </div>
                <button type="button" class="mini-primary-button">+ 新建</button>
              </div>

              <button
                v-for="profile in profiles"
                :key="profile.id"
                type="button"
                class="profile-card"
                :class="{ active: accountForm.profileName === profile.name }"
              >
                <span class="profile-card-title">{{ profile.name }}</span>
                <span class="profile-card-meta">{{ profile.summary }}</span>
              </button>
            </div>
          </aside>

          <div class="account-editor panel">
            <div class="account-editor-head">
              <div>
                <h3>人设信息填写</h3>
                <p>用于镜头剪辑一键改写文案时的“人设/口吻”参考。</p>
              </div>
              <div class="account-editor-actions">
                <button type="button" class="mini-ghost-button" @click="clearAccountForm">清空内容</button>
                <button type="button" class="mini-danger-button">删除档案</button>
              </div>
            </div>

            <div class="account-form">
              <label class="field-block">
                <span class="field-label">档案名称</span>
                <input v-model="accountForm.profileName" class="field-input" type="text" />
              </label>

              <div class="field-tip">
                可以为不同门店、账号、老板人设建立独立档案，镜头剪辑页改写时可直接选择。
              </div>

              <div
                v-for="(row, rowIndex) in accountBasicFields"
                :key="'row-' + rowIndex"
                class="field-grid"
              >
                <label v-for="field in row" :key="field.key" class="field-block">
                  <span class="field-label">({{ field.label }})</span>
                  <input v-model="accountForm[field.key]" class="field-input" type="text" />
                </label>
              </div>

              <label
                v-for="field in accountLongFields"
                :key="field.key"
                class="field-block"
              >
                <span class="field-label">({{ field.label }})</span>
                <input
                  v-if="field.type === 'input'"
                  v-model="accountForm[field.key]"
                  class="field-input"
                  type="text"
                />
                <textarea
                  v-else
                  v-model="accountForm[field.key]"
                  class="field-textarea"
                  :rows="field.rows"
                />
              </label>

              <section class="reference-panel">
                <h4>当前改写参考</h4>
                <div class="reference-list">
                  <p v-for="row in accountReference" :key="row.label" class="reference-item">
                    <span class="reference-label">{{ row.label }}：</span>
                    <span class="reference-value">{{ row.value }}</span>
                  </p>
                </div>
              </section>
            </div>
          </div>
        </div>
      </section>

      <section v-else-if="activeNav === 'assets'" class="assets-page">
        <h2 class="section-title">素材中心</h2>

        <div class="assets-shell panel">
          <div class="assets-tip">
            素材中心管理的是本地可重复使用的素材文件夹：请指定混剪根目录（例如
            <span>D:\混剪视频</span>），页面会优先显示上次扫描结果，点击“重新扫描”后再统计该目录下的视频片段。
          </div>

          <div class="assets-toolbar">
            <label class="assets-path-group">
              <span class="assets-path-label">混剪根目录</span>
              <input v-model="materialDirectory" class="assets-path-input" type="text" />
            </label>

            <div class="assets-actions">
              <button type="button" class="assets-button primary">
                <span class="assets-button-icon" v-html="iconMarkup('folder')" />
                <span>选择文件夹</span>
              </button>
              <button type="button" class="assets-button">
                <span class="assets-button-icon" v-html="iconMarkup('refresh')" />
                <span>重新扫描</span>
              </button>
              <button type="button" class="assets-button">
                <span class="assets-button-icon" v-html="iconMarkup('plusSquare')" />
                <span>新建文件夹</span>
              </button>
            </div>

            <label class="assets-search">
              <span class="assets-search-icon" v-html="iconMarkup('search')" />
              <input
                v-model="materialSearch"
                class="assets-search-input"
                type="text"
                placeholder="按类别名或路径搜索"
              />
            </label>
          </div>

          <div class="assets-stats-wrap">
            <article
              v-for="stat in materialStats"
              :key="stat.label"
              class="assets-stat-card"
              :class="`theme-${stat.theme}`"
            >
              <div class="assets-stat-value">{{ stat.value }}</div>
              <div class="assets-stat-label">{{ stat.label }}</div>
            </article>
          </div>
        </div>
      </section>

      <section v-else-if="activeNav === 'editor'" class="editor-page">
        <h2 class="section-title">镜头剪辑</h2>

        <div class="editor-shell panel">
          <div class="editor-tip">
            左侧选择模板大类与子模板，中间编辑各镜头文案与素材，右侧为成片示例预览；在下方配置背景音乐与标题字幕后，点击创建任务进入批量生成页合成。
          </div>

          <div class="editor-layout">
            <aside class="editor-sidebar-panel panel">
              <h3>模板选择</h3>
              <p>先选模板大类，再选具体子模板</p>

              <div class="editor-category-grid">
                <button
                  v-for="category in editorTemplateCategories"
                  :key="category.key"
                  type="button"
                  class="editor-category-button"
                  :class="{ active: selectedTemplateCategory === category.key }"
                  @click="selectedTemplateCategory = category.key"
                >
                  {{ category.label }}
                </button>
              </div>

              <div class="editor-template-list">
                <button
                  v-for="template in editorTemplates"
                  :key="template.id"
                  type="button"
                  class="editor-template-card"
                  :class="{ active: selectedTemplateId === template.id }"
                  @click="selectedTemplateId = template.id"
                >
                  <div class="editor-template-title-row">
                    <span class="editor-template-title">{{ template.title }}</span>
                    <span class="editor-template-tag">{{ template.tag }}</span>
                  </div>
                  <span class="editor-template-meta">{{ template.count }}</span>
                </button>
              </div>
            </aside>

            <div class="editor-main panel">
              <div class="editor-main-head">
                <div>
                  <h3>模板创作区</h3>
                  <p>选定模板后，所有创作动作都在这里完成</p>
                </div>
                <div class="editor-main-tools">
                  <button type="button" class="editor-text-link active">逐句编辑</button>
                  <button type="button" class="editor-add-shot-button" @click="addEditorShot">新增镜头</button>
                  <div class="editor-persona-select">
                    <span>人设档案</span>
                    <select v-model="editorPersona" class="editor-select">
                      <option>默认人设</option>
                      <option>江姐做电商</option>
                    </select>
                  </div>
                  <button type="button" class="mini-primary-button">一键改写文案</button>
                </div>
              </div>

              <div class="editor-shot-list">
                <article v-for="shot in editorShots" :key="shot.id" class="editor-shot-card">
                  <div class="editor-shot-head">
                    <div class="editor-shot-badge">{{ shot.title }}</div>
                    <button
                      type="button"
                      class="editor-delete-shot-button"
                      :disabled="editorShots.length === 1"
                      @click="removeEditorShot(shot.id)"
                    >
                      删除镜头
                    </button>
                  </div>
                  <div class="editor-shot-grid">
                    <label class="editor-field-block">
                      <span class="editor-field-label">模板原句</span>
                      <textarea v-model="shot.templateText" class="editor-textarea" rows="2" />
                    </label>
                    <label class="editor-field-block">
                      <span class="editor-field-label">改写文案</span>
                      <textarea
                        v-model="shot.rewriteText"
                        class="editor-textarea"
                        rows="2"
                        placeholder="编辑当前镜头口播文案"
                      />
                    </label>
                  </div>
                  <div class="editor-shot-foot">
                    <span class="editor-field-label">素材类别</span>
                    <input v-model="shot.materialType" class="editor-mini-input" type="text" />
                  </div>
                </article>
              </div>

              <div class="editor-config panel">
                <div class="editor-config-row">
                  <span class="editor-config-label">背景音乐</span>
                  <label class="editor-switch">
                    <input type="checkbox" />
                    <span class="editor-switch-track" />
                  </label>
                  <span class="editor-config-copy">开启后使用下方文件夹中的音乐；可选择固定曲目或随机一条</span>
                </div>

                <div class="editor-config-row">
                  <span class="editor-config-label">智能配音</span>
                  <span class="editor-status-pill">已开启</span>
                  <span class="editor-config-copy">固定模板默认配音</span>
                  <span class="editor-config-copy">音色</span>
                  <select v-model="editorVoice" class="editor-select wide">
                    <option>选择音色</option>
                    <option>稳重男声</option>
                    <option>温和女声</option>
                  </select>
                </div>

                <div class="editor-config-row">
                  <span class="editor-config-label">声音配置</span>
                  <button type="button" class="editor-outline-button">声音配置</button>
                </div>

                <div class="editor-config-row">
                  <span class="editor-config-label">标题/字幕</span>
                  <button type="button" class="editor-outline-button">顶部标题及字幕设置</button>
                  <button type="button" class="mini-primary-button editor-create-button" @click="createBatchTask">
                    创建任务
                  </button>
                </div>
              </div>
            </div>

            <aside class="editor-preview panel">
              <h3>成片预览</h3>
              <div class="preview-phone">
                <div class="preview-phone-screen">
                  <div class="preview-play" v-html="iconMarkup('play')" />
                  <div class="preview-empty-title">暂无成片示例</div>
                  <div class="preview-empty-copy">请在模板配置中填写预览视频链接</div>
                </div>
                <div class="preview-phone-footer">律所 - 成片效果示例</div>
              </div>

              <div class="preview-note">
                <strong>说明：</strong>
                <span>此处展示当前模板的固定成片示例视频，用于参考最终效果风格。</span>
              </div>
            </aside>
          </div>
        </div>
      </section>

      <section v-else-if="activeNav === 'tasks'" class="batch-page">
        <h2 class="section-title">批量生成</h2>

        <div class="batch-shell panel">
          <div class="batch-tip">以下为当前混剪任务列表，与「新建任务」页任务数据共用。</div>

          <section class="batch-storage panel">
            <div class="batch-storage-head">存储设置</div>
            <div class="batch-storage-body">
              <div class="batch-storage-row">
                <span class="batch-storage-label">工作缓存目录</span>
                <input v-model="batchStorage.cacheDir" class="batch-storage-input" type="text" />
                <button type="button" class="batch-outline-button">选择目录</button>
                <button type="button" class="batch-danger-button">清空</button>
              </div>
              <div class="batch-storage-note">
                配音音频会写入该目录下的 minimax音频夹，字幕 SRT 会写入 srt字幕，不设置则回退到应用缓存目录。
              </div>

              <div class="batch-storage-row">
                <span class="batch-storage-label">成片目录</span>
                <input v-model="batchStorage.outputDir" class="batch-storage-input" type="text" />
                <button type="button" class="batch-outline-button">选择目录</button>
                <button type="button" class="batch-danger-button">清空</button>
              </div>
              <div class="batch-storage-note">成片目录用于保存最终导出的视频文件；开始合成前必须先配置该目录。</div>
            </div>
          </section>

          <div class="batch-content">
            <section class="batch-table panel">
              <div class="batch-table-head">
                <span>序号</span>
                <span>模板类型</span>
                <span>镜头数</span>
                <span>状态</span>
                <span>结果</span>
                <span>操作</span>
              </div>

              <div v-if="batchTasks.length" class="batch-table-body">
                <div v-for="task in batchTasks" :key="task.id" class="batch-table-row">
                  <span>{{ task.sequence }}</span>
                  <span>{{ task.templateType }}</span>
                  <span>{{ task.shotCount }}</span>
                  <span>{{ task.status }}</span>
                  <span>{{ task.result }}</span>
                  <button type="button" class="batch-row-link" @click="removeBatchTask(task.id)">删除</button>
                </div>
              </div>

              <div v-else class="batch-empty">暂无任务</div>
            </section>

            <aside class="batch-preview panel">
              <div class="batch-preview-head">
                <span class="batch-preview-icon" v-html="iconMarkup('play')" />
                <span>成片预览</span>
              </div>

              <div class="batch-preview-phone">
                <div class="batch-preview-phone-inner">
                  <div class="batch-preview-phone-icon" v-html="iconMarkup('video')" />
                  <div class="batch-preview-phone-copy">合成成功后将自动在此播放</div>
                </div>
              </div>
            </aside>
          </div>
        </div>
      </section>

      <section v-else-if="activeNav === 'publish'" class="publish-page">
        <h2 class="section-title">发布账号管理</h2>

        <div class="publish-shell panel">
          <div class="publish-tip">
            这里负责账号建档、账号登录、登录状态检测。添加账号只会创建账号卡片和独立浏览器目录
          </div>

          <div class="publish-stats">
            <article
              v-for="stat in publishStats"
              :key="stat.label"
              class="publish-stat-card"
              :class="`theme-${stat.theme}`"
            >
              <div class="publish-stat-value">{{ stat.value }}</div>
              <div class="publish-stat-label">{{ stat.label }}</div>
            </article>
          </div>

          <div class="publish-toolbar panel">
            <div class="publish-platform-tabs">
              <button
                v-for="platform in publishPlatforms"
                :key="platform"
                type="button"
                class="publish-tab"
                :class="{ active: selectedPublishPlatform === platform }"
                @click="selectedPublishPlatform = platform"
              >
                {{ platform }}
              </button>
            </div>

            <div class="publish-toolbar-actions">
              <label class="publish-search">
                <span class="assets-search-icon" v-html="iconMarkup('search')" />
                <input
                  v-model="publishSearch"
                  class="publish-search-input"
                  type="text"
                  placeholder="搜索账号名称 / 平台 / 状态说明"
                />
              </label>
              <button type="button" class="publish-action-button secondary">检测当前平台</button>
              <button type="button" class="publish-action-button primary">添加账号</button>
            </div>
          </div>

          <div class="publish-empty-state">
            <div class="empty-box-illustration" aria-hidden="true">
              <span class="box-top" />
              <span class="box-left" />
              <span class="box-right" />
              <span class="box-bottom" />
            </div>
            <p>当前平台下还没有账号，先添加一个吧。</p>
          </div>
        </div>
      </section>

      <section v-else-if="activeNav === 'schedule'" class="schedule-page">
        <h2 class="section-title">发布排期</h2>

        <div class="schedule-shell panel">
          <div class="schedule-main">
            <div class="schedule-tip">
              批量生成成功的成片会自动出现在本页。精细化发布保留原有逐条配置逻辑；批量发布会按平台和账号轮询规则，为多条视频一次性完成分配与排期。
            </div>

            <div class="schedule-stats">
              <article
                v-for="stat in scheduleStats"
                :key="stat.label"
                class="schedule-stat-card"
                :class="`theme-${stat.theme}`"
              >
                <div class="schedule-stat-value">{{ stat.value }}</div>
                <div class="schedule-stat-label">{{ stat.label }}</div>
              </article>
            </div>

            <div class="schedule-filters">
              <div class="schedule-tabs">
                <button
                  v-for="tab in scheduleTabs"
                  :key="tab"
                  type="button"
                  class="schedule-tab"
                  :class="{ active: selectedScheduleTab === tab }"
                  @click="selectedScheduleTab = tab"
                >
                  {{ tab }}
                </button>
              </div>

              <div class="schedule-mode">
                <span class="schedule-mode-label">立即发布方式</span>
                <button
                  type="button"
                  class="schedule-mode-button"
                  :class="{ active: schedulePublishMode === '自动发布' }"
                  @click="schedulePublishMode = '自动发布'"
                >
                  自动发布
                </button>
                <button
                  type="button"
                  class="schedule-mode-button"
                  :class="{ active: schedulePublishMode === '手动确认' }"
                  @click="schedulePublishMode = '手动确认'"
                >
                  手动确认
                </button>
              </div>
            </div>

            <div class="schedule-list-title">排期列表</div>

            <div class="schedule-empty-state">
              <div class="empty-box-illustration" aria-hidden="true">
                <span class="box-top" />
                <span class="box-left" />
                <span class="box-right" />
                <span class="box-bottom" />
              </div>
              <p>当前还没有可发布的成片，先去任务中心完成混剪生成。</p>
            </div>
          </div>

          <aside class="schedule-preview-card panel">
            <h3>通用预览</h3>
            <div class="schedule-preview-phone">
              <div class="schedule-preview-copy">点击卡片上的“预览视频”在此播放成片</div>
            </div>
          </aside>
        </div>
      </section>

      <section v-else-if="activeNav === 'settings'" class="settings-page">
        <h2 class="section-title">系统设置</h2>

        <div class="settings-shell panel">
          <div class="settings-top-grid">
            <section class="settings-card panel">
              <div class="settings-card-head">剪辑设置</div>
              <div class="settings-card-body">
                <div class="settings-form-row">
                  <span class="settings-label">预设分辨率</span>
                  <select v-model="systemSettings.resolution" class="settings-select">
                    <option v-for="item in systemSettingsOptions.resolutions" :key="item">{{ item }}</option>
                  </select>
                </div>

                <div class="settings-form-row">
                  <span class="settings-label">帧率</span>
                  <div class="settings-stepper">
                    <button type="button" class="settings-stepper-button" @click="changeFrameRate(-1)">−</button>
                    <span class="settings-stepper-value">{{ systemSettings.frameRate }}</span>
                    <button type="button" class="settings-stepper-button" @click="changeFrameRate(1)">＋</button>
                  </div>
                </div>

                <div class="settings-form-row">
                  <span class="settings-label">编码器</span>
                  <select v-model="systemSettings.encoder" class="settings-select">
                    <option v-for="item in systemSettingsOptions.encoders" :key="item">{{ item }}</option>
                  </select>
                </div>

                <div class="settings-form-row">
                  <span class="settings-label">视频质量</span>
                  <select v-model="systemSettings.quality" class="settings-select">
                    <option v-for="item in systemSettingsOptions.qualities" :key="item">{{ item }}</option>
                  </select>
                </div>
              </div>
            </section>

            <section class="settings-card panel">
              <div class="settings-card-head">文案配音设置</div>
              <div class="settings-card-body">
                <div class="settings-form-row">
                  <span class="settings-label">MiniMax Key</span>
                  <input
                    v-model="systemSettings.minimaxKey"
                    class="settings-input"
                    type="text"
                    placeholder="MiniMax API Key"
                  />
                  <button type="button" class="settings-link-button">去配置</button>
                </div>

                <div class="settings-form-row">
                  <span class="settings-label">音色管理</span>
                  <button type="button" class="settings-outline-button">音色管理</button>
                  <span class="settings-row-copy">查看已保存音色，或添加新的复制音色。</span>
                </div>

                <div class="settings-form-row">
                  <span class="settings-label">阿里云百炼 Key</span>
                  <input
                    v-model="systemSettings.aliyunKey"
                    class="settings-input"
                    type="text"
                    placeholder="阿里云百炼 API Key"
                  />
                  <button type="button" class="settings-link-button">去配置</button>
                </div>
              </div>
            </section>
          </div>

          <button type="button" class="settings-collapse-row" @click="isRewriteSettingsOpen = !isRewriteSettingsOpen">
            <span>大模型改写配置 <em>只配置可调整的改写要求，底层规则由系统自动处理</em></span>
            <span :class="{ open: isRewriteSettingsOpen }">⌄</span>
          </button>

          <section v-if="isRewriteSettingsOpen" class="settings-expand-card panel">
            <div class="settings-expand-card-head">
              <span>可填写语气、行业表达、禁用词等补充要求；行数、格式和变量规则不需要手动设置。</span>
              <button type="button" class="settings-outline-button" @click="restoreRewriteDefault">恢复默认</button>
            </div>
            <textarea v-model="systemSettings.rewritePrompt" class="settings-large-textarea" rows="4" />
          </section>

          <button type="button" class="settings-collapse-row" @click="isLogsOpen = !isLogsOpen">
            <span>日志 <em>（默认收起，可展开查看/复制）</em></span>
            <span :class="{ open: isLogsOpen }">⌄</span>
          </button>

          <section v-if="isLogsOpen" class="settings-expand-card panel">
            <div class="settings-log-actions">
              <button type="button" class="settings-outline-button">刷新</button>
              <button type="button" class="settings-outline-button">复制</button>
              <button type="button" class="settings-danger-button" @click="clearSystemLogs">清空</button>
            </div>
            <div class="settings-log-panel">
              <pre v-if="systemLogs.length" class="settings-log-pre">{{ systemLogs.join('\n') }}</pre>
              <div v-else class="settings-log-empty">暂无日志</div>
            </div>
          </section>
        </div>
      </section>
    </main>
  </div>
</template>
